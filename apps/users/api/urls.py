from django.urls import path
from apps.users.api.api import user_api_view, user_datail_api_view

urlpatterns = [
    path('user/', user_api_view, name='user_api'),
    path('user/<int:id>', user_datail_api_view,name='user_detail_api'),
]