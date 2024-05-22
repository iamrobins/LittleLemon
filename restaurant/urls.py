from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('menu', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.OneMenuItemView.as_view()),
]