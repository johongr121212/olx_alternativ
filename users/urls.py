from django.urls import path
from .views import SignUpView,ProfileView,LogoutView,UpdateProfileView

app_name = 'users'


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/update/',UpdateProfileView.as_view(), name='update'),
    path('logout/', LogoutView, name='logout')
]