from django.urls import path
from .views import new, create, main, show, update, delete

app_name = "posts"
urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('', main, name="main"),
    path('/show/<int:id>', show, name="show"),
    path('update/<int:id>/', update, name="update"),
    path('delte/<int:id>/', delete, name = "delete"),
]