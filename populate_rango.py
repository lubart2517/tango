# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat('Пайтон',views=128,likes=64)

    add_page(cat=python_cat,
        title="Офіційний довідник Пайтон",
        url="http://docs.python.org/2/tutorial/", views=1)

    add_page(cat=python_cat,
        title="Як думати як компютерний науковець",
        url="http://www.greenteapress.com/thinkpython/", views=2)

    add_page(cat=python_cat,
        title="Пайтон за 10 хвилин",
        url="http://www.korokithakis.net/tutorials/python/", views=3)

    django_cat = add_cat("Джанго",views=64,likes=32)

    add_page(cat=django_cat,
        title="Офіційний довідник Джанго",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/", views=4)

    add_page(cat=django_cat,
        title="Джанго Рокс",
        url="http://www.djangorocks.com/", views=5)

    add_page(cat=django_cat,
        title="Як зтанцювати танго з Джанго",
        url="http://www.tangowithdjango.com/", views=6)

    frame_cat = add_cat("Інші фреймворки",views=32,likes=16)

    add_page(cat=frame_cat,
        title="Боттле",
        url="http://bottlepy.org/docs/dev/", views=1)

    add_page(cat=frame_cat,
        title="Фласк",
        url="http://flask.pocoo.org", views=1)

    # Print out what we have added to the user.
    #for c in Category.objects.all():
        #for p in Page.objects.filter(category=c):
            #print ("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name,views,likes):
	c = Category.objects.get_or_create(name=name)[0]
	c.views = views
	c.likes = likes
	c.save()
	return c

# Start execution here!
if __name__ == '__main__':
    print ("Starting Rango population script...")
    populate()