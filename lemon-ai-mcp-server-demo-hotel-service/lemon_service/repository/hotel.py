from lemon_service.base.base_repository import BaseRepository
from lemon_service.model.hotel import Hotel


class HotelRepository(BaseRepository[Hotel]):
    """
    酒店 数据访问
    """

    def __init__(self):
        super().__init__(Hotel)
