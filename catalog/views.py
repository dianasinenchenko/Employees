from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import generic

from .models import Employees


def index(request):
    num_employees = Employees.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_employees': num_employees,
                 'num_visits': num_visits},
    )


class EmployeesListView(generic.ListView):
    model = Employees
    paginate_by = 10


class EmployeesDetailView(generic.DetailView):
    model = Employees


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employees


class EmployeesCreate(PermissionRequiredMixin, CreateView):
    model = Employees
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class EmployeesUpdate(PermissionRequiredMixin, UpdateView):
    model = Employees
    fields = ['first_name', 'last_name', 'email']
    permission_required = 'catalog.can_mark_returned'


class EmployeesDelete(PermissionRequiredMixin, DeleteView):
    model = Employees
    success_url = reverse_lazy('employees')
    permission_required = 'catalog.can_mark_returned'

