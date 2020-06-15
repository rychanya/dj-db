from django.shortcuts import render
from phones.models import Phone
from django.http import Http404
from urllib.parse import urlencode
from django.urls import reverse


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {
        'phones': phones,
        'sort': {
            'name': f"{reverse('catalog')}?{urlencode({'sort': 'name'})}",
            'min_price': f"{reverse('catalog')}?{urlencode({'sort': 'min_price'})}",
            'max_price': f"{reverse('catalog')}?{urlencode({'sort': 'max_price'})}",
            }.items()
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__exact=slug).first()
    if not phone:
        raise Http404
    context = {'phone': phone}
    return render(request, template, context)