# 登录验证
from functools import wraps

from django.shortcuts import redirect
from django.urls import reverse


def login_required(func):
    @wraps(func)
    def check_session(request):
        username = request.session.get('username')
        if not username:
            return redirect(reverse('user:login'))
        else:
            return func(request)

    return check_session
