from django.shortcuts import render
from django.views import View
from .models import Payment

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

