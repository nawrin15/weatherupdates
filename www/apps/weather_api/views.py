import logging
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from library import requestmethod as requestMethod
from library.decorators.internalservererrorhandler import \
	InternalServerErrorHandler
from apps.weather_api import controller
from library.error.exceptions.invalidrequest import InvalidRequest

logger = logging.getLogger(__name__)

@csrf_exempt
@api_view([requestMethod.GET])
@permission_classes((AllowAny,))
@InternalServerErrorHandler
def weatherUpdates(request: object) -> object:
    """
    get current weather updateds of given city
    """
    try:
        return Response(controller.getWeatherUpdates(request.query_params))
    except (
        InvalidRequest,
    ) as exception:
        logger.exception(exception, exc_info=True)
        return Response(exception.getErrorMessage(), status=exception.code)


@csrf_exempt
@api_view([requestMethod.GET])
@permission_classes((AllowAny,))
@InternalServerErrorHandler
def cityInfo(request: object) -> object:
    """
    get the first 3 matched city names 
    """
    try:
        return Response(controller.getCityNames(request.query_params))
    except (
        InvalidRequest,
    ) as exception:
        logger.exception(exception, exc_info=True)
        return Response(exception.getErrorMessage(), status=exception.code)