from django.urls import path
from first_app import views

# Template Tagging
app_name = "first_app"

urlpatterns = [
    path('index/',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('welcome/',views.welcome,name="welcome"),
    path('users/',views.users,name="users"),
    path('form/',views.form_name_view,name="form_name_view"),
    path('other/',views.other,name="other"),
    path('relative/',views.relative,name="relative"),
    path('logout/',views.user_logout,name="logout"),
    path('special/',views.special,name="special"),
    path('user_login/',views.user_login,name="user_login"),
]

