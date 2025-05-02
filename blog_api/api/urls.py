from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, register_user, login_user
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog-create'),
    path('blogs/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog-edit'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('api-token-auth/', authtoken_views.obtain_auth_token, name='api-token-auth'), #old login
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
