# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 19:08:23 2022

@author: Aluneth
"""

from rango.models import Category, Page
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

django.setup()


def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial',
         'views':24
         },
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython',
         'views':42,
         },
        {'title': 'learn Python in 10 Minutes',
         'url': 'http://www.kotokithakis.net/tutorials/python/',
         'views':22
         },
    ]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views':24
         },
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'views':42
         },
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views':22
         },
    ]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev',
        'views':24,
         },
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'views':42,
         },
    ]

    cats = {
        'python': {'pages': python_pages, 
                   'views': 128, 'likes': 64
                   },
        'Django': {'pages': django_pages, 
                   'views': 64, 'likes': 32
                   },
        'Other Frameworks': {'pages': other_pages,
                             'views': 32, 'likes': 16
                             },
        'Pascal': {'pages': [], 'views': 32, 'likes': 16},
        'Peter': {'pages': [], 'views': 32, 'likes': 16},
        'Phplip': {'pages': [], 'views': 32, 'likes': 16},
        'Programmer': {'pages': [], 'views': 32, 'likes': 16},
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'],
                     #p['views']
                     )

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')
           # print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
