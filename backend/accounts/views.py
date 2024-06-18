from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

token = ''

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

@login_required
def social_login_redirect(request):
    try:
        user = User.objects.get(username=request.user.username)
        tokens = get_tokens_for_user(user)

        # res = redirect(f"https://urdu-dict-frontend-dot-cloud-work-314310.ew.r.appspot.com/", permanent=True)
        res = redirect(f"http://localhost:3000/", permanent=True)
        res.set_cookie("token", tokens["access"], max_age=60 * 60 * 4)
        global token
        token = tokens["access"]
        return res
    except Exception as e:
        print(e)
        return Response("Not allowed")
        
@api_view(('GET',))
def get_tokens(request):
    try:
        global token
        logout = request.query_params.get('logout')
        # print('LogOut Value',logout, 'end', type(logout))
        if logout == '1':
            print("inside logout if")
            token = ""
        # print('TOKEN VALUE', token)
        return Response(token)
    except Exception as e:
        print(e)
        return Response("Not allowed")
