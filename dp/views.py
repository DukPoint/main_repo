from django.shortcuts import render
from .models import Store


# Create your views here.

def search(request):
    query = request.GET.get('query', '')
    stores = Store.objects.filter(name__icontains=query)

    context = {
        'stores': stores,
        'query': query,
    }
    return render(request, 'dp/store.html', context)


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
