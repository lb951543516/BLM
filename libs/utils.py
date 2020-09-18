from functools import wraps

from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse

from CarApp.models import BlmCar
from UserApp.models import User, Address


# 登录验证
def login_required(func):
    @wraps(func)
    def check_session(request):
        username = request.session.get('username')
        if not username:
            return redirect(reverse('user:login'))
        else:
            return func(request)

    return check_session


# 邮件发送
def send_email(username, userrank, token, email):
    index = loader.get_template('blm/user/email.html')

    context = {
        'username': username,
        'userrank': userrank,
        'url': 'http://119.45.201.6:8000/user/beactive/?token=' + str(token),
    }
    index_value = index.render(context)

    # 主题
    subject = '饱了吗App注册激活'
    # 内容
    html_message = index_value
    # 发送者
    from_email = '13029868285@163.com'
    # 接受者
    recipient_list = [email]

    # 发送
    send_mail(subject=subject, message='', html_message=html_message, from_email=from_email,
              recipient_list=recipient_list)


# 检查是否设置默认地址
def check_addr(request):
    username = request.session.get('username')
    uid = User.objects.get(userName=username).id
    addr_used_num = Address.objects.filter(userId=uid).filter(isselect=1).count()

    if addr_used_num == 0:
        return False
    else:
        return True


# 算钱
def pay_money(request):
    username = request.session.get('username')
    u_id = User.objects.filter(userName=username)[0].id
    cars = BlmCar.objects.filter(c_user_id=u_id)

    money = 0
    for car in cars:
        if car.is_buy:
            money += car.c_good.price * car.g_num

    return round(money, 2)
