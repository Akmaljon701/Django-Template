import os
import traceback
import requests
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


class SendErrorToBotMiddleware:
    def __init__(self, get_response, model=None):
        self.get_response = get_response
        self.model = model

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):

        token = os.getenv('BOT_TOKEN')
        chat_id = os.getenv('USER_ID')
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        traceback_info = traceback.format_exc()
        exception_type = type(exception).__name__
        message = f"Template\n{exception_type}: {str(exception)}\n\n{traceback_info}\n\nTemplate"
        data = {
            'chat_id': chat_id,
            'text': message
        }
        requests.post(url=url, params=data)


class DoesNotExistMiddleware:
    def __init__(self, get_response, model=None):
        self.get_response = get_response
        self.model = model

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, ObjectDoesNotExist):
            model = str(exception).split(" ")[0]
            return JsonResponse({"response": f"{model} not found!"}, status=400)

