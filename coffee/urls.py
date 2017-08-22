from django.conf.urls import url
from . import views

urlpatterns = [
  

    url(r'^signup/$', views.usersignup, name = 'signup'),
    url(r'^login/$', views.userlogin, name = 'login'),
    url(r'^logout/$', views.userlogout, name = 'logout'),

    url(r'^createCoffee/$', views.createCoffee, name = 'createCoffee'),
    url(r'^updateCoffee/(?P<coffee_id>[\d]+)/$', views.updateCoffee, name='updateCoffee'),
    url(r'^deleteCoffee/(?P<coffee_id>[\d]+)/$', views.deleteCoffee, name='deleteCoffee'),

    url(r'^createSyrup/$', views.createSyrup, name = 'createSyrup'),
    url(r'^updateSyrup/(?P<syrup_id>[\d]+)/$', views.updateSyrup, name='updateSyrup'),
    url(r'^deleteSyrup/(?P<syrup_id>[\d]+)/$', views.deleteSyrup, name='deleteSyrup'),


    url(r'^createPowder/$', views.createPowder, name = 'createPowder'),
    url(r'^updatePowder/(?P<powder_id>[\d]+)/$', views.updatePowder, name='updatePowder'),
    url(r'^deletePowder/(?P<powder_id>[\d]+)/$', views.deletePowder, name='deletePowder'),


    url(r'^createRoast/$', views.createRoast, name = 'createRoast'),
    url(r'^updateRoast/(?P<roast_id>[\d]+)/$', views.updateRoast, name='updateRoast'),
    url(r'^deleteRoast/(?P<roast_id>[\d]+)/$', views.deleteRoast, name='deleteRoast'),

    url(r'^createBeans/$', views.createBeans, name = 'createBeans'),
    url(r'^updateBeans/(?P<beans_id>[\d]+)/$', views.updateBeans, name='updateBeans'),
    url(r'^deleteBeans/(?P<beans_id>[\d]+)/$', views.deleteBeans, name='deleteBeans'),

    url(r'^userCoffeeList/$', views.coffeeList, name='userCoffeeList'),
    url(r'^userCoffeeDetails/(?P<details_id>[\d]+)/$', views.coffeeDetails, name='userCoffeeDetails'),
    url(r'^deleteCoffee/(?P<details_id>[\d]+)/$', views.deleteCoffee, name='deleteCoffee'),

    url(r'^addCities/$', views.addCities, name = 'addCities'),
    url(r'^updateCities/(?P<city_id>[\d]+)/$', views.updateCities, name='updateCities'),
    url(r'^deleteCities/(?P<city_id>[\d]+)/$', views.deleteCities, name='deleteCities'),

    url(r'^createAddress/$', views.createAddress, name = 'createAddress'),
    url(r'^updateAddress/(?P<address_id>[\d]+)/$', views.updateAddress, name='updateAddress'),
    url(r'^deleteAddress/(?P<address_id>[\d]+)/$', views.deleteAddress, name='deleteAddress'),

    url(r'^userCoffees/$', views.userCoffee, name='userCoffees'),

    url(r'^priceCalculation/$', views.priceCalculation, name = 'priceCalculation'),
    
    ]