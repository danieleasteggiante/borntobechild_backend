import json

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import requests


# Create your views here.
@require_POST
@csrf_exempt
def login_google(request):
    code = json.loads(request.body)['code']
    print(code)
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': settings.GOOGLE_OAUTH_CLIENT_ID,
        'client_secret': settings.GOOGLE_OAUTH_CLIENT_SECRET,
        'redirect_uri': settings.GOOGLE_OAUTH_REDIRECT_URI,
    }
    response = requests.post(settings.GGOGLE_OAUTH_TOKEN_URI, data=data)
    print(get_google_user_info(response.json()['access_token']))
    return JsonResponse(response.json(), status=response.status_code)


def save_user_info(param):
    pass


def get_google_user_info(access_token):
    url = settings.GOOGLE_OAUTH_USER_INFO_URI
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.get(url, headers=headers)
    save_user_info(response.json())
    if response.status_code == 200:
        return response.json()

    return response.status_code, response.text

