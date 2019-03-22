from django.urls import path
from . import views

urlpatterns = [
  path('', views.wishitems_index, name='wishitems_index'),
  path('add/', views.WishitemAdd.as_view(), name='wishitem_add'),
  path('delete/<int:wishitem_id>/', views.wishitem_delete, name='wishitem_delete'),
]