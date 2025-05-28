import hashlib
import uuid
from datetime import datetime, timedelta

from lemon_service.core.api import ServiceException
from lemon_service.model import UserSession
from lemon_service.repository import UserRepository, UserSessionRepository
from lemon_service.schema.auth import LoginReqSchema, LoginRespSchema


class UserService:
    """
    用户业务
    """

    __user_repository = UserRepository()
    __user_session_repository = UserSessionRepository()

    def login(self, login_req: LoginReqSchema) -> LoginRespSchema:
        """
        用户登录
        :param login_req: 登录请求数据
        :return: 登录结果数据
        """
        user = self.__user_repository.get_user_by_number(login_req.number)
        if user is None:
            raise ServiceException(status_code=400, err_code="user_not_exist", message="用户不存在")
        password_secret_hash_object = hashlib.sha256(login_req.password.encode('utf-8'))
        password_secret = password_secret_hash_object.hexdigest()
        if password_secret != user.password:
            raise ServiceException(status_code=400, err_code="password_error", message="密码错误")
        # 密码校验成功，开始登录业务
        token = str(uuid.uuid4())
        now = datetime.now()
        expire_time = now + timedelta(days=30)
        session = UserSession(token=token, user_id=user.id, expire_time=expire_time)
        self.__user_session_repository.upsert(session)
        return LoginRespSchema(token=token)
