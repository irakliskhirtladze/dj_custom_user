from django.urls import path
from users import views


urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
]
