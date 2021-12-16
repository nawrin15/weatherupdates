import logging
from library.error.exceptions.internalservererror import InternalServerError
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

def InternalServerErrorHandler(method):
	def wrapper(request, *args, **kwargs):
		try:
			return method(request, *args, **kwargs)
		except Exception as exception:
			logger.exception(exception, exc_info=True)
			return Response(
	            InternalServerError().getErrorMessage(),
	            status=status.HTTP_500_INTERNAL_SERVER_ERROR
	        )
	return wrapper
