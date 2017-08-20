from django.shortcuts import render, redirect
from .forms import SignUp, Login, CoffeeForm, SyrupForm, PowderForm, RoastForm, BeansForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from .models import Coffee, Syrup, Beans, Powder, Roast
from django.contrib import messages
from django.shortcuts import get_object_or_404
from decimal import Decimal


def usersignup(request):
    context = {}
    form = SignUp()
    context['form'] = form
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            password = user.password

            user.set_password(password)
            user.save()

            authUser = authenticate(username=username, password=password)
            login(request, authUser)

            return redirect('coffee:createCoffee')

        messages.error(request, form.errors)
        return redirect('coffee:signup')
    return render(request,'signup.html', context)

def userlogin(request):
    context = {}
    form = Login()
    context['form'] = form
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            authUser = authenticate(username=username, password=password)
            if authUser is not None:
                login(request, authUser)
                return redirect('coffee:createCoffee')


            messages.warning(request, 'Wrong Username/Password. Please Try Again.')
            return redirect('coffee:login')
    return render(request,'login.html', context)

def userlogout(request):
    logout(request)
    return redirect("coffee:login")

############################################# Syrup ###########################

def createSyrup(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    form = SyrupForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.user = request.user
        obj.save()
        messages.success(request, "Syrup Created")
        # return redirect('coffee:list')
    context = {
        'form':form,

    }
    return render(request, 'createSyrup.html', context)


def updateSyrup(request, syrup_id):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    syrup_object = get_object_or_404(Syrup, id=syrup_id)
    form = SyrupForm(request.POST or None, request.FILES or None, instance=syrup_object)
    if form.is_valid():
        form.save()
        messages.success(request, "Updated")
        # return redirect('coffee:updateSyrup')
    context = {
        'form':form,
        'instance':syrup_object,
    }
    return render(request, 'updateSyrup.html', context)

def deleteSyrup(request, syrup_id):
    syrup_object = Syrup.objects.get(syrup_id)
    syrup_object.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("coffee:createCoffee")

    ############################################# Powder ###########################

def createPowder(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    form = PowderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.user = request.user
        obj.save()
        messages.success(request, "Podwer Created")
        # return redirect('coffee:list')
    context = {
        'form':form,

    }
    return render(request, 'createPowder.html', context)

def updatePowder(request, powder_id):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    powder_object = get_object_or_404(Powder, id=powder_id)
    form = PowderForm(request.POST or None, request.FILES or None, instance=powder_object)
    if form.is_valid():
        form.save()
        messages.success(request, "Updated")
        # return redirect('coffee:updatePowder')
    context = {
        'form':form,
        'instance':powder_object,
    }
    return render(request, 'updatePowder.html', context)


def deletePowder(request, powder_id):
    powder_object = Powder.objects.get(powder_id)
    powder_object.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("coffee:createCoffee")

    ############################################# Roast ###########################

def createRoast(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    form = RoastForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.user = request.user
        obj.save()
        messages.success(request, "Roast Created")
        return redirect('coffee:createCoffee')
    context = {
        'form':form,

    }
    return render(request, 'createRoast.html', context)

def updateRoast(request, roast_id):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    roast_object = get_object_or_404(Roast, id=roast_id)
    form = RoastForm(request.POST or None, request.FILES or None, instance=roast_object)
    if form.is_valid():
        form.save()
        messages.success(request, "Updated")
        # return redirect('coffee:updateRoast')
    context = {
        'form':form,
        'instance':roast_object,
    }
    return render(request, 'updateRoast.html', context)

def deleteRoast(request, roast_id):
    roast_object = Roast.objects.get(roast_id)
    roast_object.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("coffee:createCoffee")

    ############################################# Baens ###########################


def createBeans(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    form = BeansForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.user = request.user
        obj.save()
        messages.success(request, "Beans Created")
        # return redirect('coffee:list')
    context = {
        'form':form,

    }
    return render(request, 'createBeans.html', context)


def updateBeans(request, beans_id):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    beans_object = get_object_or_404(Beans, id=beans_id)
    form = BeansForm(request.POST or None, request.FILES or None, instance=beans_object)
    if form.is_valid():
        form.save()
        messages.success(request, "Updated")
        # return redirect('coffee:updateBeans')
    context = {
        'form':form,
        'instance':beans_object,
    }
    return render(request, 'updateBeans.html', context)

def deleteBeans(request, beans_id):
    beans_object = Beans.objects.get(beans_id)
    beans_object.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("coffee:createCoffee")
    ############################################# Coffee ###########################

def createCoffee(request):
    form = CoffeeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user=request.user
        obj.save()
        form.save_m2m()
        obj_beans = obj.beans.price
        shots_price=0.200*obj.shots
        milk_price=0.100*obj.milk

        syrup_price=0
        for syrup in obj.syrup.all():
            syrup_price=syrup.price

        powder_price=0
        for powder in obj.powder.all():
           powder_price=powder.price

        obj.price=Decimal(obj_beans)+Decimal(shots_price)+Decimal(milk_price)+Decimal(syrup_price)+Decimal(powder_price)
        obj.save()

        # obj.save()
        messages.success(request, "Created")
        # return redirect('coffee:list')
    context = {
        'form':form,

    }

    return render(request, 'createCoffee.html', context)

def updateCoffee(request, coffee_id):
    # if not (request.user.is_staff or request.user.is_superuser):
    #     raise Http404
    coffee_object=Coffee.objects.filter(user=request.user, id=coffee_id)
    # coffee_object = get_object_or_404(Coffee, id=coffee_id)
    form = CoffeeForm(request.POST or None, request.FILES or None, instance=coffee_object)
    if form.is_valid():
        form.save()
        messages.success(request, "Updated")
        # return redirect('coffee:createCoffee')
    context = {
        'form':form,
        'instance':coffee_object,
    }
    return render(request, 'updateCoffee.html', context)

def deleteCoffee(request, coffee_id):
    coffee_object = Coffee.objects.get(coffee_id)
    coffee_object.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("coffee:createCoffee")
  
##################################################################################

def coffeeList(request):
    
    obj_list=Coffee.objects.filter(user=request.user)
    context={
    'obj_list':obj_list
    }
    return render(request,'userCoffeeList.html',context)
    # return redirect('coffee:userCoffeeList')


##################################################################################

def coffeeDetails(request, details_id):

    if request.user:
        obj_details=Coffee.objects.filter(user=request.user, id=details_id)
        context={
               'obj_details':obj_details

                }
    return render(request,"userCoffeeDetails.html", context)
    # return redirect('coffee:userCoffeeList')










