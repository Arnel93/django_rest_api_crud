from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateProductoAPIView.as_view(), name='get_productos'),
    path('<pk>/', views.RetrieveUpdateDestroyProductoAPIView.as_view(), name='get_producto'),

]
