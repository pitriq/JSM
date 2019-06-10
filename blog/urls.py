from django.urls import path

from . import views

urlpatterns = [
    path('', views.main),
    path('post/<int:post_id>/', views.post_detail),
]
