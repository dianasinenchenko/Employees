from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('employees/', views.EmployeesListView.as_view(), name='employees'),
    path('employees/<int:pk>', views.EmployeesDetailView.as_view(), name='employees-detail'),
]


urlpatterns += [
    path('employees/create/', views.EmployeesCreate.as_view(), name='employees_create'),
    path('employees/<int:pk>/update/', views.EmployeesUpdate.as_view(), name='employees_update'),
    path('employees/<int:pk>/delete/', views.EmployeesDelete.as_view(), name='employees_delete'),
]

