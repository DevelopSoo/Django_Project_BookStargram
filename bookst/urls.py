from django.urls import path, include
from .views import new, create, detail, edit, update, delete


app_name = "bookst"

urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('<int:post_id>/', detail, name="detail"),
    path('edit/<int:post_id>/', edit, name="edit"),
    path('update/<int:post_id>/', update, name="update"),
    path('delete/<int:post_id>/', delete, name="delete"),
]

