from django.urls import path
from blog import views


urlpatterns = [
    path('post/', views.create_post),
    path('list/', views.list),
    path('delete/', views.remove_post),
]
