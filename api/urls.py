from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('users/', include('app_users.api.urls'), name='users'),
    path('orders/', include('app_orders.api.urls'), name='orders'),
]
