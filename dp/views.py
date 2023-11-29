from django.shortcuts import render
import json
import random
from .models import User
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout(request):
    logout(request)
    return redirect('login')  # 로그아웃 후 리다이렉트할 페이지 지정


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


#로그인,회원가입
class SignUpView(View):
    def get(self, request):
        image_list = ['image/image1.jpg', 'image/image2.jpg', 'image/image3.jpg', 'image/image4.jpg',
                      'image/image5.jpg', 'image/image6.jpg']
        random.shuffle(image_list)
        context = {'random_image': image_list[0]}
        return render(request, 'dp/signup.html', context)

    def post(self, request):
        data = request.POST

        # 이용약관 동의 여부 확인
        if not data.get('agreed'):
            return JsonResponse({'error': '이용약관에 동의해야 합니다.'}, status=400)



        return JsonResponse({'message': '회원가입 완료'}, status=200)


class SignUpView2(View):
    def get(self, request):
        image_list = ['image/image1.jpg', 'image/image2.jpg', 'image/image3.jpg', 'image/image4.jpg',
                      'image/image5.jpg', 'image/image6.jpg']
        random.shuffle(image_list)
        context = {'random_image': image_list[0]}
        return render(request, 'dp/signup2.html', context)

    def post(self, request):
        data = request.POST

        # 기타 필요한 사용자 정보 수집
        email = data.get('email')
        password = data.get('password')

        # 사용자 생성
        User.objects.create(
            email=email,
            password=password
            # 필요한 다른 필드들 추가
        )


class SignInView(View):
    def get(self, request):
        image_list = ['image/image1.jpg', 'image/image2.jpg', 'image/image3.jpg', 'image/image4.jpg',
                      'image/image5.jpg', 'image/image6.jpg']
        random.shuffle(image_list)
        context = {'random_image': image_list[0]}
        return render(request, 'dp/signin.html',context)

    def post(self, request):
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': f'{user.email}님 로그인 성공!'}, status=200)
        else:
            return JsonResponse({'message': '이메일 또는 비밀번호가 올바르지 않습니다.'}, status=400)


def review1(request):
    return render(
        request,
        'dp/review1.html'
    )
