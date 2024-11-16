import json
import requests
import logging

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from oauthgoogle.DTO.OauthResponse import OauthResponse
from oauthgoogle.models import UserInfo
from enum import Enum

LOGGER = logging.getLogger(__name__)

class UserInfoResponse(Enum):
    NEW_USER = 1
    ALREADY_REGISTERED = 2
    ERROR = 3

GOOGLE_OAUTH_DATA = {
        'grant_type': 'authorization_code',
        'code': '',
        'client_id': settings.GOOGLE_OAUTH_CLIENT_ID,
        'client_secret': settings.GOOGLE_OAUTH_CLIENT_SECRET,
        'redirect_uri': settings.GOOGLE_OAUTH_REDIRECT_URI,
    }

def save_user_info(user_info) -> UserInfoResponse :
    try:
        LOGGER.info("Salvo le informazioni dell'utente: " + user_info.name)
        user_info, created = UserInfo.objects.get_or_create(id=user_info.id, defaults={
            'email': user_info.email,
            'verified_email': user_info.verified_email,
            'name': user_info.name,
            'given_name': user_info.given_name,
            'family_name': user_info.family_name,
            'picture': user_info.picture,
        })
        if created:
            return UserInfoResponse.NEW_USER
        return UserInfoResponse.ALREADY_REGISTERED
    except Exception as e:
        LOGGER.error("Errore nel salvataggio delle informazioni dell'utente")
        LOGGER.error(e)
        return UserInfoResponse.ERROR

@require_POST
@csrf_exempt
def login_google(request):
    LOGGER.info("Recupero il codice di autorizzazione")
    code = json.loads(request.body)['code']
    GOOGLE_OAUTH_DATA['code'] = code
    response = requests.post(settings.GOOGLE_OAUTH_TOKEN_URI, data=GOOGLE_OAUTH_DATA)
    LOGGER.info("Response: " + str(response.json()))
    user_info_json = get_google_user_info(response.json()['access_token'])
    user_info = UserInfo.from_dict(user_info_json)
    user_saving_response : UserInfoResponse = save_user_info(user_info)
    oauth_response = OauthResponse(user_info,response.json()['access_token'])
    oauth_response.is_logged = True
    if user_saving_response == UserInfoResponse.NEW_USER:
        LOGGER.info("Utente creato : "+ str(oauth_response))
        return JsonResponse(oauth_response.to_dict(), status="201")
    if user_saving_response == UserInfoResponse.ALREADY_REGISTERED:
        LOGGER.info("Utente gia registrato : "+ str(oauth_response))
        oauth_response.is_new_user = False
        return JsonResponse(oauth_response.to_dict(), status="200")
    LOGGER.error("Errore durante il salvataggio dell'utente")
    return JsonResponse({"Error" : "errore durante il salvataggio dell utente" }, status="500")

def get_google_user_info(access_token):
    try:
        LOGGER.info("Recupero le informazioni dell'utente")
        url = settings.GOOGLE_OAUTH_USER_INFO_URI
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        LOGGER.warning("Non sono riuscito a recuperare le informazioni dell'utente " + str(e))
        raise ValueError("Failed to fetch user info from Google API")
