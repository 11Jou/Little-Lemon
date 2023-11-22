from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('menu', views.menu_view, name='menu'),
    path('booking', views.book, name='book'),
    path('bookings', views.getBook),
    path('login', views.signin, name='signin'),
    path('logout', views.logout_view , name='signout'),
    path('signup', views.signup_view , name='signup'),
]