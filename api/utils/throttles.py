from rest_framework.throttling import SimpleRateThrottle


# 对没有登录的用户进行节流
class VisitThrottle(SimpleRateThrottle):
    scope = 'LiLi'

    def get_cache_key(self, request, view):
        return self.get_ident(request)      # get_ident()用户的唯一辨识ip


# 对登陆过的用户进行节流
class UserThrottle(SimpleRateThrottle):
    scope = 'LiLiAn'

    def get_cache_key(self, request, view):
        return request.user.username





