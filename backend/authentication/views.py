from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
import jwt
import datetime
from .models import Manege  # Add this line to import the Manege model
from django.views.decorators.csrf import csrf_exempt

class LoginView(APIView):
    @csrf_exempt
    def post(self, request):
        ret = {
            "data": {},
            "meta": {
                "status": 200,
                "msg": ""
            }
        }
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            value = int(request.data.get('value'))

            if value == 1:
                user = Manege.objects.filter(username=username, password=password)
                if user.count == 0:
                    ret['meta']['status'] = 500
                    ret['meta']['msg'] = "用户名或密码错误"
                    return Response(ret)
                elif user and user.first().password:
                    dct = {
                    "exp": datetime.datetime.now() + datetime.timedelta(days=7),
                    "iat": datetime.datetime.now(),
                    "id": user.first().id,
                        "username": user.first().username,
                    }
                    token = jwt.encode(dct, settings.SECRET_KEY, algorithm='HS256'),
                    ret['data']['token'] = token
                    ret['data']['username'] = username
                    ret['data']['user_id'] = user.first().id
                    ret['data']['isAdmin'] = 1
                    ret['data']['status'] = 200
                    ret['meta']['msg'] = "登录成功"
                    return Response(ret)
                else:
                    ret['meta']['status'] = 500
                    ret['meta']['msg'] = "用户名或密码错误"
                    return Response(ret)
        except Exception as e:
            ret['meta']['status'] = 500
            ret['meta']['msg'] = str(e)
            return Response(ret)
        
    def get(self, request):
        return Response("Hello World!")
    
    def put(self, request):
        return Response("Hello World!")
    
    def delete(self, request):
        return Response("Hello World!")
