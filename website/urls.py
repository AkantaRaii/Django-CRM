from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('register',views.register_user,name='register'),
    path('record/<int:pk>',views.show_record,name='record'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('add/',views.add,name='add')
]