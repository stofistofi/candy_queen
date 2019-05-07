from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="candy-index"),
    path('<int:id>', views.get_candy_by_id, name="candy_details"),
    path('create_candy', views.create_candy, name="create_candy")
]
