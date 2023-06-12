from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, RegistraterView

app_name = 'market'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('register/', RegistraterView.as_view(),name='market_register'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create')
]