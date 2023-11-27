from django.shortcuts import render
# from .models import store

# Create your views here.
def index(request):
    return render(
        request,
        'store/index.html',
    )

# def home(request):
#     stores = store.objects.all
#     return render(request,'index.html',{'stores:stores'})