
class CustomBaseException(Exception):
    def __init__(self, message=''):
        self.message = message

    def __str__(self):
        return self.message


class ApiKeyNotProvidedError(CustomBaseException):
    pass


class UnauthorizedError(CustomBaseException):
    pass


class NotFoundError(CustomBaseException):
    pass


class PlayerNotFoundError(CustomBaseException):
    pass


class ServerError(CustomBaseException):
    pass
