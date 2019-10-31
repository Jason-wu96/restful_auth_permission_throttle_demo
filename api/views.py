from rest_framework.views import APIView
from django.http import JsonResponse
from api.models import *
import hashlib
import time


# token加密
def md5(user):
    ctime = str(time.time())
    m = hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()


from api.utils.throttles import VisitThrottle


# 登录生成token
class LoginView(APIView):
    authentication_classes = []       # 不做认证限制
    permission_classes = []             # 不做权限限制
    throttle_classes = [VisitThrottle]  # 做节流限制（每分钟3次）

    def post(self, request, *args, **kwargs):
        user = request._request.POST.get('username')
        pwd = request._request.POST.get('password')
        obj = UserInfo.objects.filter(username=user, password=pwd).first()
        ret = {'code': 1000, 'msg': None}
        try:
            if not obj:
                ret['code'] = 10001
                ret['msg'] = '用户或密码错误'
            else:
                token = md5(user)
                Token.objects.update_or_create(user=obj, defaults={'token': token})
        except Exception as e:
            pass
        return JsonResponse(ret)


ORDER_GOODS = {
    1: {'name': 'dog', 'price': 123},
    2: {'name': 'wawa', 'price': 8888}
}


# 用户认证
class IndexView(APIView):

    def get(self, request, *args ,**kwargs):
        ret = {'code': 1000,'msg': None,'data': None}
        print(request.user)
        print(request.auth)
        try:
            ret['data'] = ORDER_GOODS
        except Exception as e:
            pass
        return JsonResponse(ret)


