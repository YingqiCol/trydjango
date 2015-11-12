from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from laptop.forms import SignUpForm
from .models import *
from .search import *
# from .forms import *
# from django.db import connection
# from django.template import Template, Context
# from django.template.loader import get_template

import datetime


def hello(request):
    title = 'Welcome'
    context={}
    sti = 'yingqi'
    # if request.method == "POST":
    # print(request.POST)
    if 'j' in request.GET:
        if 'edu' not in request.GET['j']:
            context['violat'] = "Please use a valid EDU mail"
    if 'q' in request.GET and 'edu' in request.GET['j']:
                name = Users.objects.filter(name=request.GET['q']).values('name')
                uid = Users.objects.filter(name=request.GET['q']).values('uid')
                gender = Users.objects.filter(name=request.GET['q']).values('gender')
                jod = Users.objects.filter(name=request.GET['q']).values('job')
                favor = Users.objects.filter(name=request.GET['q']).values('favorite')
                Static.sti = request.GET['q']
                context = {
                "title": title,
                "name": name,
                "uid": uid,
                'gender': gender,
                'job': jod,
                'favor': favor,
                }

    if 'p' in request.GET:
        Users.objects.filter(name=Static.sti).update(favorite=request.GET['p'])
        favor = Users.objects.filter(name=Static.sti).values('favorite')
        context['favor'] = favor
    return render(request, "home.html", context)


def current_datetime(request):
    now = datetime.datetime.now()
    # t = get_template('current_date.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return render(request, 'current_date.html', {'current_date': now})


# def hours_ahead(request, offset):
# try:
#         offset = int(offset)
#     except ValueError:
#         raise Http404()
#     dt = datetime.datetime.now()+datetime.timedelta(hours = offset)
#     html = "<html><body> In %s hour(s), it will be %s </body></html>" % (offset, dt)
#     return HttpResponse(html)


# def home(request):
#     entries = Cpu.objects.all()
#     form = CpuForm(request.POST or None)
#
#     context = {
#         "Cpu": entries,
#         "form": form
#     }
#     return render(request, 'index.html', context)


# def get_name(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')
#     else:
#         form = NameForm()
#     return render(request, 'name.html', {'form': form})


def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['lmodel__lmodel','cmodel', 'hmodel', 'gmodel'])

        found_entries = Include.objects.filter(entry_query)   # . order_by('-pub_date')

    return render_to_response('search.html',
                              {'query_string': query_string, 'found_entries': found_entries},
                              context_instance=RequestContext(request))

class Static:
    static = 15
    sti = ''

def show(request):
    # entry = Laptop.objects.filter(lmodel='ASUS K501LX')
    lmo = Laptop.objects.filter(lmodel='ASUS K501LX').values('lmodel')
    ty = Laptop.objects.filter(lmodel='ASUS K501LX').values('type')
    wei = Laptop.objects.filter(lmodel='ASUS K501LX').values('weight')
    reso = Laptop.objects.filter(lmodel='ASUS K501LX').values('resolution')
    price = Sell.objects.filter(lmodel='ASUS K501LX').values('price')
    url = Sell.objects.filter(lmodel='ASUS K501LX').values('url')
    pair = list(zip(price,url))
    revi1 = Review.objects.filter(rid=7).values('description')
    revi2 = Review.objects.filter(rid=9).values('description')
    if 'q' in request.GET:
        r = Static.static
        revi1 = Review.objects.create(rid=r, description=request.GET['q'])
        revi1 = Review.objects.filter(rid=r).values('description')
        Static.static += 1
        r = Static.static
    context = {
        'content': lmo,
        'type': ty,
        'weight': wei,
        'reso': reso,
        'pair': pair,
        'revi1': revi1,
        'revi2': revi2,
    }
    return render_to_response('k501lx.html', context)



def show2(request):
    entry = Laptop.objects.filter(lmodel='DELL XPS 15')
    lmo = Laptop.objects.filter(lmodel='DELL XPS 15').values('lmodel')
    ty = Laptop.objects.filter(lmodel='DELL XPS 15').values('type')
    wei = Laptop.objects.filter(lmodel='DELL XPS 15').values('weight')
    reso = Laptop.objects.filter(lmodel='DELL XPS 15').values('resolution')
    price = Sell.objects.filter(lmodel='DELL XPS 15').values('price')
    url = Sell.objects.filter(lmodel='DELL XPS 15').values('url')
    pair = list(zip(price,url))
    revi1 = Review.objects.filter(rid=10).values('description')
    revi2 = Review.objects.filter(rid=6).values('description')

    if 'q' in request.GET:
        r = Static.static
        revi1 = Review.objects.create(rid=r, description=request.GET['q'])
        revi1 = Review.objects.filter(rid=r).values('description')
        Static.static += 1
        r = Static.static
    context = {
        'content': lmo,
        'type': ty,
        'weight': wei,
        'reso': reso,
        'pair': pair,
        'revi1': revi1,
        'revi2': revi2,
    }
    return render_to_response('xps15.html', context)


def compare(request):
    if 'q' in request.GET or 'p' in request.GET:
        name1 = request.GET['q']
        name2 = request.GET['p']
        lap1 = Laptop.objects.filter(lmodel=name1).values('lmodel')
        lap2 = Laptop.objects.filter(lmodel=name2).values('lmodel')
        cpu1 = Include.objects.filter(lmodel=name1).values('cmodel')
        cpu2 = Include.objects.filter(lmodel=name2).values('cmodel')
        gpu1 =  Include.objects.filter(lmodel=name1).values('gmodel')
        gpu2 =  Include.objects.filter(lmodel=name2).values('gmodel')
        hd1 =  Include.objects.filter(lmodel=name1).values('hmodel')
        hd2 =  Include.objects.filter(lmodel=name2).values('hmodel')
        context = {
            'lap1': lap1,
            'lap2': lap2,
            'cpu1': cpu1,
            'cpu2': cpu2,
            'gpu1': gpu1,
            'gpu2': gpu2,
            'hd1': hd1,
            'hd2': hd2,
        }
        return render_to_response('compare.html',context)
    context= {}
    return render_to_response('compare.html',context)


