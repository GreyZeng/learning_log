from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    # 包含默认的省份验证URL
    path('', include('django.contrib.auth.urls'))
]
