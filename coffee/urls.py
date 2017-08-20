from django.conf.urls import url
from . import views

urlpatterns = [
  

    url(r'^signup/$', views.usersignup, name = 'signup'),
    url(r'^login/$', views.userlogin, name = 'login'),

    url(r'^createCoffee/$', views.createCoffee, name = 'createCoffee'),
    url(r'^updateCoffee/(?P<coffee_id>[\d]+)/$', views.updateCoffee, name='updateCoffee'),

    url(r'^createSyrup/$', views.createSyrup, name = 'createSyrup'),
    url(r'^updateSyrup/(?P<syrup_id>[\d]+)/$', views.updateSyrup, name='updateSyrup'),


    url(r'^createPowder/$', views.createPowder, name = 'createPowder'),
    url(r'^updatePowder/(?P<powder_id>[\d]+)/$', views.updatePowder, name='updatePowder'),


    url(r'^createRoast/$', views.createRoast, name = 'createRoast'),
    url(r'^updateRoast/(?P<roast_id>[\d]+)/$', views.updateRoast, name='updateRoast'),

    url(r'^createBeans/$', views.createBeans, name = 'createBeans'),
    url(r'^updateBeans/(?P<beans_id>[\d]+)/$', views.updateBeans, name='updateBeans'),

    url(r'^userCoffeeList/$', views.coffeeList, name='userCoffeeList'),

    url(r'^userCoffeeDetails/(?P<details_id>[\d]+)/$', views.coffeeDetails, name='userCoffeeDetails'),

    ]