from django.db import models

class UserInfo(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField()
    verified_email = models.BooleanField()
    name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    picture = models.URLField()
    def __str__(self):
        return self.name

    @staticmethod
    def from_dict(info_user_dict):
        return UserInfo(
            id=info_user_dict.get('id'),
            email=info_user_dict.get('email'),
            verified_email=info_user_dict.get('verified_email'),
            name=info_user_dict.get('name'),
            given_name=info_user_dict.get('given_name'),
            family_name=info_user_dict.get('family_name'),
            picture=info_user_dict.get('picture')
        )