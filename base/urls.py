from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('community/', views.community, name='community'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
]
