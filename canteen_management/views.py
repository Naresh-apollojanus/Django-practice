from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib import messages

from .forms import AddFoodItem, ModelForm, CookForm, LoginForm

from .models import FoodItem, Cook, CookInfo


# Create your views here.
def home(request):
    return render(request, 'home.html')


def list_food(request):
    # food_item = FoodItem..all()
    # return render(request, 'listfood.html', context={'food_items': food_item})
    food_item = FoodItem.objects.all()
    return render(request, 'listfood.html', context={'food_items': food_item})


@login_required(login_url=reverse_lazy('login'))
def add_food(request):
    if request.method == 'GET':
        form = ModelForm()
        return render(request, 'addfooditem.html ', context={'forms': form})

    elif request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            # FoodItem.objects.create(
            #     name=request.POST['name'],
            #     qty=request.POST['qty'],
            #     price=request.POST['price'],
            #     discount=request.POST['discount']
            form.save(request.POST)
            return redirect('list_food')
        else:
            return render(request, 'addfooditem.html', context={'form': form})


@login_required(login_url=reverse_lazy('login'))
def edit_food(request, id):
    food = FoodItem.objects.get(id=id)
    if request.method == 'GET':
        form = ModelForm(instance=food)
        return render(request, 'editfood.html', {'form': form})

    elif request.method == 'POST':
        form = ModelForm(request.POST, instance=food)
        if form.is_valid():
            form.save(request.POST)
            return redirect('list_food')


def search_name(request):
    if request.method == 'GET':
        return render(request, 'search.html')

    elif request.method == 'POST':
        name = request.POST['name']
        a = Cook.objects.filter(name=name)
        return render(request, 'search.html', context={'a': a})


@login_required(login_url=reverse_lazy('login'))
def delete_food(request, id):
    food = FoodItem.objects.get(id=id)
    food.delete()

    return redirect('list_food')


class IndexGen(TemplateView):
    template_name = 'index.html'


class ListViewGen(ListView):
    model = Cook


class detail_view(DetailView):
    model = Cook


class create_view(CreateView):
    model = CookInfo
    fields = ('phone_no', 'pan_no')
    template_name = 'fooditem_create.html'
    success_url = reverse_lazy('list_food')


class update_view(UpdateView):
    model = CookInfo
    fields = ('phone_no', 'pan_no')
    template_name = 'update_view.html'
    success_url = reverse_lazy('list_food')

    def get_object(self, queryset=None):
        return CookInfo.objects.get(phone_no=self.kwargs.get('phone_no'))


# @login_required(login_url=reverse_lazy('login'))
class edit_cook(UpdateView):
    form_class = CookForm
    model = Cook
    template_name = 'update_view.html'
    success_url = reverse_lazy('list_food')

    def get_object(self, queryset=None):
        return Cook.objects.get(id=self.kwargs.get('id'))


class create_cook(CreateView):
    model = Cook
    fields = ('name', 'age', 'cook_info')
    template_name = 'fooditem_create.html'
    success_url = reverse_lazy('list_view')


def login_form(request):
    if request.method == 'GET':
        form = LoginForm
        return render(request, 'login_form.html', {'forms': form})

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username)
        print(password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                print(request.GET)
                if 'next' in request.GET.keys():
                    messages.success(request, ' login success')
                    return redirect(request.GET['next'])
                else:
                    return redirect('index')

            else:
                return redirect('login')
        else:

            messages.error(request, 'invalid username or password')
            return redirect('login')


@login_required(login_url=reverse_lazy('login'))
def logout_view(request):
    logout(request)
    return redirect('index')
