from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('requirements/<int:requirement_id>/bid/', views.place_bid, name='place_bid'),
    path('bids/<int:bid_id>/<str:action>/', views.manage_bid, name='manage_bid'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
