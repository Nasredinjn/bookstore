
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # new
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('accounts/',include('allauth.urls')),
    path('books/',include("books.urls")),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# auth.urls
"""
accounts/login/ [name="login"]
accounts/logout/ [name="logout"]
accounts/password_change/ [name="password_change"]
accounts/password_change/done/ [name="password_change_done"]
accounts/password_reset/ [name="password_reset"]
accounts/password_reset/done/ [name="password_reset_done"]
accounts/reset/<uidb64>/<token>/ [name="password_reset_confirm"]
accounts/reset/done/ [name="password_reset_complete"]

"""


