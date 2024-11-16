from oauthgoogle.models import UserInfo


class OauthResponse:
    def __init__(self, user_info: UserInfo, access_token: str):
        self.id = user_info.id
        self.email = user_info.email
        self.verified_email = user_info.verified_email
        self.name = user_info.name
        self.given_name = user_info.given_name
        self.family_name = user_info.family_name
        self.picture = user_info.picture
        self.access_token = access_token
        self.is_new_user = True
        self.is_logged = False

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'verified_email': self.verified_email,
            'name': self.name,
            'given_name': self.given_name,
            'family_name': self.family_name,
            'picture': self.picture,
            'access_token': self.access_token,
            'is_new_user' : self.is_new_user,
            'is_logged' : self.is_logged
        }

    def __str__(self):
        return str(self.to_dict())
