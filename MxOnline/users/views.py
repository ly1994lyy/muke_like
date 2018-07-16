from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或者密码错误！'})
    else:
        return render(request, 'login.html')