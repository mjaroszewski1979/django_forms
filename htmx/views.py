from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.db.models import Q, Min, Avg, Count
from .models import Country,City
from .forms import CityFormSet, CityModelForm






def detail(request, slug=None): 
    city = get_object_or_404(City, slug=slug)
    return render(request, 'detail.html', {'city': city})

'''def create_city(request, pk):
    country = Country.objects.get(pk=pk)
    formset = CityFormSet(request.POST or None)

    if request.method == 'POST':
        if formset.is_valid():
            formset.instance = country
            formset.save()
            return redirect('cities:create-city', pk=country.id)

    context = {
        'formset' : formset,
        'country' : country
    }

    return render(request, 'create_city.html', context)'''
    
def create_city(request, pk):
    country = Country.objects.get(pk=pk)
    cities = City.objects.filter(country=country)
    form = CityModelForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            city = form.save(commit=False)
            city.country = country
            city.save()
            return redirect('htmx:detail-city', pk=city.id)
        else:
            return render(request, 'htmx/partials/city_form.html', {'form':form})

    context = {
        'form' : form,
        'country' : country,
        'cities' : cities
    }

    return render(request, 'htmx/create_city.html', context)

def create_city_form(request):
    context = {
        'form' : CityModelForm()
    }
    return render(request, 'htmx/partials/city_form.html', context)

def update_city(request, pk):
    city = City.objects.get(pk=pk)
    form = CityModelForm(request.POST or None, instance=city)

    if request.method == 'POST':
        if form.is_valid():
            city = form.save()
            return redirect('htmx:detail-city', pk=city.id)

    context = {
        'form' : form, 
        'city' : city
    }
    return render(request, 'htmx/partials/city_form.html', context)

def detail_city(request, pk):
    city = City.objects.get(pk=pk)
    context = {
        'city' : city
    }
    return render(request, 'htmx/city_detail.html', {'city': city})

def delete_city(request, pk):
    city = City.objects.get(pk=pk)
    city.delete()
    return HttpResponse('')

