"""
rest_framework 认证组件  认证成功返回一个元祖（request.user, request.auth)
"""
from rest_framework.authentication import BaseAuthentication
from api.models import *
from rest_framework import exceptions


class Myauthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request._request.GET.get('token')
        token_obj = Token.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        else:
            return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        pass
