from django.shortcuts import render
from django.http import Http404
from .models import User, Car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import OwnerForm


def get_owner(request, owner_id):
    try:
        o = User.objects.get(pk=owner_id)
        print(o.last_name)
    except User.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'get_owner.html', {'owner': o})


def get_owners_list(request):
    context = {}
    context["dataset"] = User.objects.all()

    return render(request, "list_owners.html", context)


class CarListView(ListView):
    model = Car
    template_name = 'cars_list.html'


class CarRetrieveView(DetailView):
    model = Car
    template_name = "get_car.html"


class CarUpdateView(UpdateView):
    model = Car
    fields = ['brand', 'model', 'color']
    success_url = '/car/list/'


class CarCreate(CreateView):
    model = Car
    fields = ['license_plate_number', 'brand', 'model', 'color']
    template_name = 'car_creation.html'
    success_url = '/car/list/'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/car/list/'


def create_owner_view(request):
    context = {}

    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owner_creation.html", context)