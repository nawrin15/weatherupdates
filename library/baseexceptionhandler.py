import logging
from rest_framework.response import Response
from rest_framework import status
from library.error.exceptions.internalservererror import InternalServerError

logger = logging.getLogger(__name__)

def baseExceptionHandler(exception, context):
    try:
        apiResponse = {"errorMessage" : str(exception)}
        apiResponseStatus = exception.status_code
        responseDict = {
            "errorMessage" : str(exception),
            "statusName" : str(exception.__class__.__name__),
            "statusCode" : apiResponseStatus
        }
        return Response(responseDict, status=apiResponseStatus)
    except Exception as exception:
        logger.exception(exception, exc_info=True)
        return Response(
            InternalServerError().getErrorMessage(),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
