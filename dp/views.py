from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import User, Store, Menu, Review, Payment
import json
import random
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
import logging
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class OrderPayment(LoginRequiredMixin, View):
    template_name = 'dp/order_payment.html'
    login_url = '/signin/'

    def get(self, request, store_id, menu_id):
        try:
            menu_info = Menu.objects.get(pk=menu_id)
            store_info = Store.objects.get(pk=store_id)
        except (Menu.DoesNotExist, Store.DoesNotExist):
            # Handle the case when menu or store is not found
            return render(request, self.template_name, {'error_message': 'Menu or store not found'})

        user = request.user
        print(user, user.points)

        # Pass the menu and store objects to the template
        context = {'menu': menu_info, 'store': store_info, 'user': user}  # 'user':user
        return render(request, self.template_name, context)


class StoreMenu(View):
    def get(self, request, pk):
        store = get_object_or_404(Store, pk=pk)
        menus = store.menu_set.all()

        context = {
            'store': store,
            'menus': menus,
        }

        return render(
            request,
            'dp/store_menu.html',
            context
        )

def search(request):
    query = request.GET.get('query', '')
    stores = Store.objects.filter(name__icontains=query)

    context = {
        'stores': stores,
        'query': query,
    }
    return render(request, 'dp/store.html', context)


@login_required
def my_logout(request):
    auth_logout(request)
    return redirect('signin')


def store(request):
    stores = Store.objects.all()
    return render(
        request,
        'dp/store.html',
        {
            'stores': stores,
        }
    )

def main(request):
    return render(
        request,
        'dp/main.html'
    )

def mypage(request):
    return render(
        request,
        'dp/mypage.html'
    )


class MyPageView(View):
    template_name = 'dp/mypage.html'

    def get(self, request, *args, **kwargs):
        user_points = 8300
        payments = Payment.objects.all()[:10]
        context = {
            'user_points': user_points,
            'payments': payments,
        }
        return render(request, self.template_name, {'payments': payments})

@login_required
def mypage_detail_1(request):
    return render(request, 'dp/mypage_detail_1.html')


@login_required
def mypage_detail_2(request):
    return render(request, 'dp/mypage_detail_2.html')

# 비밀번호 변경 위해 유효성 확인
logger = logging.getLogger(__name__)

@login_required
def check_password_mypage(request):
    if request.method == 'POST':
        entered_password = request.POST.get('password', '')
        user = request.user

        # 비밀번호 확인
        try:
            if user.check_password(entered_password):
                # 비밀번호가 일치하면 mypage_detail_2 페이지로 리디렉션
                return JsonResponse({'success': True})
            else:
                # 비밀번호가 일치하지 않으면 에러 메시지를 JSON으로 반환
                return JsonResponse({'error': '비밀번호가 일치하지 않습니다.'}, status=400)
        except Exception as e:
            # 예외가 발생하면 에러 메시지를 JSON으로 반환
            logger.error(f"Error in check_password_mypage: {e}")
            return JsonResponse({'error': str(e)}, status=400)

# 비밀번호 변경
@login_required
def change_password_mypage(request):
    if request.method == 'POST':
        new_password = request.POST.get('new-password', '')
        confirm_password = request.POST.get('confirm-password', '')
        user = request.user

        if new_password == confirm_password:
            # 비밀번호가 일치하면 비밀번호 업데이트
            user.set_password(new_password)
            user.save()

            # 세션 업데이트
            update_session_auth_hash(request, user)

            # 비밀번호 변경 성공 시 어떤 페이지로 이동할지 정의
            return redirect('mypage')
        else:
            return JsonResponse({'error': '입력한 비밀번호가 일치하지 않습니다.'}, status=400)

    return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)

def mypage_detail_1(request) :
    return  render(
        request,
        'dp/mypage_detail_1.html'
    )

def mypage_detail_2(request) :
    return  render(
        request,
        'dp/mypage_detail_2.html'
    )


# 로그인,회원가입
class SignUpView(View):  # 회원가입 이용약관동의
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
        # return redirect('signup2')


class SignUpView2(View):  # 회원가입 이메일 입력
    def get(self, request):
        image_list = ['image/image1.jpg', 'image/image2.jpg', 'image/image3.jpg', 'image/image4.jpg',
                      'image/image5.jpg', 'image/image6.jpg']
        random.shuffle(image_list)
        context = {'random_image': image_list[0]}
        return render(request, 'dp/signup2.html', context)

    def post(self, request):
        try:
            email = request.POST.get('email')

            if email is None or email == '':
                raise ValidationError('이메일을 입력하세요.')
            if User.objects.filter(email=email).exists():
                raise ValidationError('이미 사용 중인 이메일입니다.')

            # 성공
            request.session['email'] = email
            return redirect('signup3')

        except ValidationError as e:
            # 이미 존재하는 이메일에 대한 에러를 알림
            messages.error(request, str(e))
            return redirect('signup2')



class SignUpView3(View):  # 회원가입 비밀번호 입력
    def get(self, request):
        image_list = ['image/image1.jpg', 'image/image2.jpg', 'image/image3.jpg', 'image/image4.jpg',
                      'image/image5.jpg', 'image/image6.jpg']
        random.shuffle(image_list)
        context = {'random_image': image_list[0]}
        return render(request, 'dp/signup3.html', context)

    def post(self, request):
        password=request.POST.get('password')
        email=request.session.get('email')
        request.session['password']=password
        return redirect('signup4')


class SignUpView4(View):  # 회원가입 이름 입력
    def get(self, request):
        image_list = ['image/image1.jpg', 'image/image2.jpg', 'image/image3.jpg', 'image/image4.jpg',
                      'image/image5.jpg', 'image/image6.jpg']
        random.shuffle(image_list)
        context = {'random_image': image_list[0]}
        return render(request, 'dp/signup4.html', context)

    def post(self, request):
        name=request.POST.get('name')
        email=request.session.get('email')
        password=request.session.get('password')

        user = User.objects.create_user(email=email, password=password)
        user.name=name
        user.save()
        request.session.clear()
        return redirect('signup_complete')


class SignUpView5(View):  # 회원가입 완료
    def get(self, request):
        image_list = ['image/image1.jpg', 'image/image2.jpg', 'image/image3.jpg', 'image/image4.jpg',
                      'image/image5.jpg', 'image/image6.jpg']
        random.shuffle(image_list)
        context = {'random_image': image_list[0]}
        return render(request, 'dp/signup_complete.html', context)


class SignInView(View):  # 로그인 페이지
    def get(self, request):
        if request.user.is_authenticated:
            # 다른 페이지(예: 홈 페이지)로 리디렉션
            return redirect('/')
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
            #messages.add_message(request, messages.INFO, f'{user.name}님 로그인 성공!')
            return redirect('/')

        else:
            messages.add_message(request, messages.INFO, '이메일 또는 비밀번호가 올바르지 않습니다.')
            return redirect('signin')


def review1(request):
    return render(
        request,
        'dp/review1.html'
    )
