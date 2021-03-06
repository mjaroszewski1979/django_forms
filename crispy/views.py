from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CityForm, NewStudsForm, CreditCardForm
from .models import Students
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

from . import forms

def index_1(request):
    context = {'form': forms.CollegeForm()}
    return render(request, 'crispy/index_1.html', context)

def index_2(request):
    context = {'form': forms.UniversityForm()}
    return render(request, 'crispy/index_2.html', context)

def index_3(request):
    context = {'form': forms.SchoolForm()}
    return render(request, 'crispy/index_3.html', context)

def index_4(request):
    context = {'form': forms.NewSchoolForm()}
    return render(request, 'crispy/index_4.html', context)

def index_5(request):
    context = {'form': forms.InlineForm()}
    return render(request, 'crispy/index_5.html', context)

def index_6(request):
    form = forms.AnotherForm()
    return render(request, 'crispy/index_6.html', {'form':form})

def index_7(request):
    context = {'form': forms.CreditCardForm()}
    return render(request, 'crispy/card.html', context)

class CreateView(SuccessMessageMixin, generic.CreateView):
    template_name = 'crispy/create.html'
    success_message = 'Success'
    form_class = CityForm


class NewCreateView(SuccessMessageMixin, generic.CreateView):
    template_name = 'crispy/newcreate.html'
    model = Students
    fields = ['name', 'address', 'age']

    def get_form(self, form_class=None):
       form = super().get_form(form_class)
       form.helper = FormHelper()
       form.helper.field_class = 'col-6 mb-2'
       form.helper.add_input(Submit('submit', 'Create', css_class='btn-primary mt-2'))
       return form

