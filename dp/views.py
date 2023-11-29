from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout(request):
    logout(request)
    return redirect('login')  # 로그아웃 후 리다이렉트할 페이지 지정

# Create your views here.

def store(request):
    return render(
        request,
        'dp/store.html'
    )


def main(request):
    return render(
        request,
        'dp/main.html'
    )

def review1(request):
    return render(
        request,
        'dp/review1.html'
    )
