from django.urls import path
from .views import BoxView,OrderCreateView,ProductView,RecommendBoxView
urlpatterns = [
    path('boxes/', BoxView.as_view(), name='boxes'),
    path('orders/', OrderCreateView.as_view(), name='orders'),
    path('products/', ProductView.as_view(), name='products'),
    path('orders/<int:id>/recommend-box/', RecommendBoxView.as_view(), name='recommend-box'),
    
    
]
# /api/orders/1/recommend-box/
