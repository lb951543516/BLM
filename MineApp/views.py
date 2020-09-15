from django.shortcuts import render

# Create your views here.
from UserApp.models import User


def mine(request):
    # 个人中心展示头像，手机，用户名
    username = request.session.get('username', '')
    if username:
        user = User.objects.filter(userName=username)[0]
        url_img = user.userImg
        user_phone = user.userPhone[0:3] + '****' + user.userPhone[7:]

        context = {
            'username': username,
            'user_phone': user_phone,
            'url_img': url_img,
        }

        return render(request, 'blm/main/mine/mine.html', context=context)
    else:
        return render(request, 'blm/main/mine/mine.html')
