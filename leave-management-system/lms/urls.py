from django.urls import path,include
from accounts import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name="login"),
    path('accounts/',include('accounts.urls'))
]
