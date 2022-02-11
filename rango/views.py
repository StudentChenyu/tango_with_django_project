from django.shortcuts import render
from django.http import HttpResponse
# from django.template import RequestContext
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from django.shortcuts import redirect
from rango.forms import PageForm
from django.urls import reverse
# from rango.forms import UserForm, UserProfileForm
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout
# from datetime import datetime


# Create your views here.

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['bloodmessage'] = 'Cruchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    
    return render(request, 'rango/index.html', context=context_dict)
    
    """
    request.session.set_test_cookie()
    
    pages_list = Page.objects.order_by('-views')[:5]

    context_dict = {
        'categories': category_list,
        'pages': pages_list,
    }

    
    context_dict['pages'] = pages_list

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'rango/index.html', context=context_dict)

    return response
 """


def about(request):
    print(request.method)
    
    print(request.user)
    return render(request, 'rango/about.html', {})
    """
    context_dict = {'boldmessage': "Rango says here is about page."}
    if request.session.get('visits'):
        visits = request.session.get('visits')
    else:
        visits = 0
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'rango/about.html', context_dict)
    return response
"""

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages

        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)

"""
@login_required
"""
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/rango/')
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})
"""

@login_required
"""
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('/rango/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category()
                page.views = 0
                page.save()

                return redirect(reverse('rango:show_category', 
                                        kwargs={'category_name_slug': 
                                                category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)



"""


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request, response):
    visits = int(request.COOKIES.get('visits', '1'))
    last_visit_cookie = request.COOKIES.get('last_visit',
                                            str(datetime.now()))
    last_visit_time = datetime.strprime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')
    if(datetime.now() - last_visit_time).days > 0:
        visits = visits+1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits


@login_required
def restricted(request):
    return HttpResponse("Since you are logged in, you can see this text!")

"""
