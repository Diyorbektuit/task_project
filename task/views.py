from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from task.models import Client, Product, SalesManager, ServiceDepartment, Driver, InstallationTeam, Order, OrderItem
from task.forms import (ClientForm, ProductForm, SalesManagerForm, ServiceDepartmentForm, DriverForm,
                        InstallationTeamForm, OrderForm, OrderItemForm)


def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Faqat admin kirishi mumkin!")

    return render(request, 'login.html')


def admin_logout(request):
    logout(request)
    return redirect('admin_login')


@login_required
def dashboard(request):
    user = request.user
    if user.is_anonymous:
        return redirect('admin_login')
    models = ['Clients', 'Products', 'SalesManagers', 'ServiceDepartment', 'Drivers', 'InstallationTeams', 'Orders', 'OrderItems']
    return render(request, 'dashboard.html', {'models': models})


@login_required
def model_list(request, model_name):
    user = request.user
    if user.is_anonymous:
        return redirect('admin_login')
    model_classes = {
        'Clients': (Client, ClientForm),
        'Products': (Product, ProductForm),
        'SalesManagers': (SalesManager, SalesManagerForm),
        'ServiceDepartment': (ServiceDepartment, ServiceDepartmentForm),
        'Drivers': (Driver, DriverForm),
        'InstallationTeams': (InstallationTeam, InstallationTeamForm),
        'Orders': (Order, OrderForm),
        'OrderItems': (OrderItem, OrderItemForm),
    }
    model, _ = model_classes.get(model_name, (None, None))
    if not model:
        return redirect('dashboard')

    fields = [field.name for field in model._meta.fields]

    objects = model.objects.all()
    return render(request, 'model_list.html', {
        'model_name': model_name,
        'objects': objects,
        'fields': fields,
    })


@login_required
def model_create(request, model_name):
    user = request.user
    if user.is_anonymous:
        return redirect('admin_login')
    model_classes = {
        'Clients': (Client, ClientForm),
        'Products': (Product, ProductForm),
        'SalesManagers': (SalesManager, SalesManagerForm),
        'ServiceDepartment': (ServiceDepartment, ServiceDepartmentForm),
        'Drivers': (Driver, DriverForm),
        'InstallationTeams': (InstallationTeam, InstallationTeamForm),
        'Orders': (Order, OrderForm),
        'OrderItems': (OrderItem, OrderItemForm),
    }
    _, form_class = model_classes.get(model_name, (None, None))
    if not form_class:
        return redirect('dashboard')

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model_list', model_name=model_name)
    else:
        form = form_class()
    return render(request, 'model_form.html', {'form': form, 'model_name': model_name})


@login_required
def model_update(request, model_name, pk):
    user = request.user
    if user.is_anonymous:
        return redirect('admin_login')
    model_classes = {
        'Clients': (Client, ClientForm),
        'Products': (Product, ProductForm),
        'SalesManagers': (SalesManager, SalesManagerForm),
        'ServiceDepartment': (ServiceDepartment, ServiceDepartmentForm),
        'Drivers': (Driver, DriverForm),
        'InstallationTeams': (InstallationTeam, InstallationTeamForm),
        'Orders': (Order, OrderForm),
        'OrderItems': (OrderItem, OrderItemForm),
    }
    model, form_class = model_classes.get(model_name, (None, None))
    if not model or not form_class:
        return redirect('dashboard')

    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        form = form_class(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('model_list', model_name=model_name)
    else:
        form = form_class(instance=obj)
    return render(request, 'model_form.html', {'form': form, 'model_name': model_name})


@login_required
def model_delete(request, model_name, pk):
    user = request.user
    if user.is_anonymous:
        return redirect('admin_login')
    model_classes = {
        'Clients': Client,
        'Products': Product,
        'SalesManagers': SalesManager,
        'ServiceDepartment': ServiceDepartment,
        'Drivers': Driver,
        'InstallationTeams': InstallationTeam,
        'Orders': Order,
        'OrderItems': OrderItem,
    }
    model = model_classes.get(model_name)
    if not model:
        return redirect('dashboard')
    obj = get_object_or_404(model, pk=pk)
    obj.delete()
    return redirect('model_list', model_name=model_name)