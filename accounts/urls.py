from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
    # 包含默认的省份验证URL
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]
