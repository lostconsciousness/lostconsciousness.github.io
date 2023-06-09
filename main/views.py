from django.shortcuts import render
from main.models import Podik, NovaPost
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string
from .filters import PodFilter
from .forms import UpdatePriceForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django_filters.views import FilterView
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect
#localStorage = localStoragePy('general2286.pythonanywhere.com', 'db.sqlite3')


def my_views(request):

    if  request.method == 'POST':
        data = request.POST.get('price')
        print(f"data = {data}")
        # items = localStorage.getItem("ids")
        # for pod in Podik.objects.all():
        #     if pod.id in items:
        #         pod.price = data
        response_data = {'result': 'success'}
        #localStorage.clear()
        print(response_data)
        return JsonResponse(response_data)
    else:
        response_data = {'error': 'Invalid request'}
        #localStorage.clear()
        return JsonResponse(response_data)
    

def update_price(request):
    if request.method == 'POST':
        form = UpdatePriceForm(request.POST)
        if form.is_valid():

            data = {}
            for key in request.POST.keys():
                if key.startswith('id'):
                    data[key[2:]] = request.POST[key]
            print(data.values())
            temp = []
            for i in data.values():
                print(i)
                temp.append(i)
            new_price = request.POST.get('price')
            new_quantity = request.POST.get('quantity_in_stock')
            new_available = request.POST.get('available')
            messages.success(request, f'Successfully updated {len(temp)} products')
            print(f"new_price = {new_price}")
            res = Podik.objects.filter(id__in=temp)
            if(new_price != ""):
                res.update(price=new_price)
            if(new_quantity != ""):
                res.update(quantity_in_stock=new_quantity)
            res.update(available = new_available)
            return redirect(reverse('admin:index'))
    else:
        print("321")
        selected_ids = request.GET.getlist('selected_ids')
        products = Podik.objects.filter(id__in=selected_ids)
        initial_price = products.first().price if products.exists() else 0
        form = UpdatePriceForm(initial={'price': initial_price})

    return render(request, 'update_price.html', {'form': form})

def novaPost(request):
    novaPost = serializers.serialize('json', NovaPost.objects.all())
    context = {"novaPost":novaPost,}
    return JsonResponse(context)
   
def novaPosttest(request):
    novaPost = serializers.serialize('json', NovaPost.objects.all())
    context = {"novapost":novaPost,}
    return render(request, "main/homepage.html", context)

def filter_data(request):
    filtered_data = Podik.objects.all()
    filter = PodFilter(request.GET, queryset=filtered_data)
    data = list(filter.qs.values())
    return JsonResponse({'data': data})

class MyFilterView(FilterView):
  model = Podik
  filterset_class = PodFilter
  template_name = "homepage.html"

  def get(self, request, *args, **kwargs):
    self.object_list = self.get_queryset()
    self.object_list = self.filterset_class(request.GET, queryset=self.object_list).qs
    context = self.get_context_data(object_list=self.object_list)
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
      # Если запрос является AJAX-запросом, вернуть только часть шаблона
      return render(request, "main/homepage.html", context)
    else:
      # В противном случае, вернуть полный шаблон
      return self.render_to_response(context)

def heater(request):
    return render(request, 'main/heater.html', {})

def iqos(request):
    context = {
        "pods": Podik.objects.all().filter(categoryId = 208)
    }
    return render(request, 'main/iqos.html', context)

def glo(request):
    context = {
        "pods": Podik.objects.all().filter(categoryId = 282)
    }

def jouz(request):
    context = {
        "pods": Podik.objects.all().filter(categoryId = 282)
    }

def powerbanks(request):
    context = {
        "pods": Podik.objects.all().filter(categoryId = 282)
    }

def load_more(request):
    allObjects = Podik.objects
    podfilter = PodFilter(request.GET, queryset=Podik.objects.all())
    name = request.GET.get('name')
    total_item = int(request.GET.get('total_item'))
    print(name, total_item)

    offers = {
        'pod':list(podfilter.qs.values()[total_item:total_item+50]),
        'pods':list(allObjects.filter(categoryId=220).values()[total_item:total_item+50]),
        'devices':list(allObjects.filter(categoryId=221).values()[total_item:total_item+50]),
        'cartridges':list(allObjects.filter(categoryId=222).values()[total_item:total_item+50]),
        'disposable':list(allObjects.filter(categoryId=239).values()[total_item:total_item+50]),
        'elf_bar':list(allObjects.filter(categoryId=287).values()[total_item:total_item+50]),
        'hqd':list(allObjects.filter(categoryId=288).values()[total_item:total_item+50]),
        'liquids':list(allObjects.filter(categoryId=208).values()[total_item:total_item+50]),
        'ukrainian_salt':list(allObjects.filter(categoryId=236).values()[total_item:total_item+50]),
        'premium_salt':list(allObjects.filter(categoryId=237).values()[total_item:total_item+50]),
    }

    data = {
        "offer": offers[name],
    }
    return JsonResponse(data=data)

def homepage(request):
    podfilter = PodFilter(request.GET, queryset=Podik.objects.all())

    novaPost = serializers.serialize('json', NovaPost.objects.all())
    allObjects = Podik.objects.all()
    pods = serializers.serialize('json', podfilter.qs[:50])
    pod_system = serializers.serialize('json', allObjects.filter(categoryId = 220)[:50])
    devices = serializers.serialize('json', allObjects.filter(categoryId = 221)[:50])
    disposable = serializers.serialize('json', allObjects.filter(categoryId = 239)[:50])
    cartridges = serializers.serialize('json', allObjects.filter(categoryId = 222)[:50])
    liquids = serializers.serialize('json', allObjects.filter(categoryId = 208)[:50])
    elf_bar = serializers.serialize('json', allObjects.filter(categoryId = 287)[:50])
    hqd = serializers.serialize('json', allObjects.filter(categoryId = 288)[:50])
    ukrainian_salt = serializers.serialize('json', allObjects.filter(categoryId = 236)[:50])
    premium_salt = serializers.serialize('json', allObjects.filter(categoryId = 237)[:50])
    
    context = {
        "filter":podfilter.form,
        "pod": pods,
        "pod_system":pod_system,
        "devices":devices,
        "disposable":disposable,
        "cartridges":cartridges,
        "liquids":liquids,
        "elf_bar":elf_bar,
        "hqd":hqd,
        "ukrainian_salt":ukrainian_salt,
        "premium_salt":premium_salt,
        "novapost":novaPost,
    }
    return render(request, 'main/homepage.html', context)


def my_view(request):
    if request.method == 'GET':
        podfilter = PodFilter(request.GET, queryset=Podik.objects.all())
        pods = serializers.serialize('json', podfilter.qs[:50])
        context = {'filter': pods}
        return render(request, 'main/homepage.html', context)
    
from django.http import JsonResponse

def clear_filters(request):
    # Удаляем все параметры фильтров
    request.GET._mutable = True
    request.GET.clear()
    request.GET._mutable = False

    # Генерируем HTML для фильтров
    filters_html = render_to_string('homepage.html', {'filters': podfilter.form})
    podfilter = PodFilter(request.GET, queryset=Podik.objects.all())
    # Возвращаем данные в формате JSON
    return JsonResponse({'filters_html': filters_html})
