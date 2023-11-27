from django.shortcuts import render

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
        'mypage.html'
    )