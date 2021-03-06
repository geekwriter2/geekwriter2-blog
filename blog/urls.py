from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include # new
from blogging.feed import BlogFeed

urlpatterns = [
    path('polling/', include('polling.urls')),  # <-- Add this
    path('admin/', admin.site.urls),
    path('', include('blogging.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
    path('accounts/', include('allauth.urls')),
    path('latest/feed/', BlogFeed()),
]
