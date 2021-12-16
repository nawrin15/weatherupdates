from rest_framework import status
from library.error import errormessage as errorMessage

class InvalidRequest(Exception):
    def __init__(
        self,
        errorMessage=errorMessage.INVALID_REQUEST,
        code=status.HTTP_400_BAD_REQUEST
    ):
        self.code = code
        self.errorMessage = errorMessage

    def getErrorMessage(self):
        return {
            "errorMessage" : self.errorMessage,
            "statusName" : self.__class__.__name__,
            "statusCode": self.code
        }
