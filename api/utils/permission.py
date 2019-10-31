"""
权限组件 有权访问时返回 True  无权访问 False
"""
from rest_framework.permissions import BasePermission


# 当用户是svip时才有权访问
class VIPpermisssion(BasePermission):
    message = 'SVIP才能访问'

    def has_permission(self, request, view):
        if request.user.user_type == 3:
            return True
        else:
            return False
