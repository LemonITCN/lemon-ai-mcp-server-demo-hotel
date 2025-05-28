def api_public(func):
    func._api_public = True


def api_need_login(func):
    func._api_need_login = True
