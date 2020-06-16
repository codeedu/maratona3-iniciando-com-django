from django.urls import path

from app.views import category_list, category_create

urlpatterns = [
    path('category_list/', category_list),
    path('category_create/', category_create),
]