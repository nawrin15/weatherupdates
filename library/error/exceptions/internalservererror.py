from rest_framework import status
from library.error import errormessage as errorMessage

class InternalServerError(Exception):
    def __init__(
        self,
        errorMessage=errorMessage.INTERNAL_SERVER_ERROR,
        code=status.HTTP_500_INTERNAL_SERVER_ERROR
    ):
        self.code = code
        self.errorMessage = errorMessage

    def getErrorMessage(self):
        return {
            "errorMessage" : self.errorMessage,
            "statusName" : self.__class__.__name__,
            "statusCode": status.HTTP_500_INTERNAL_SERVER_ERROR
        }
