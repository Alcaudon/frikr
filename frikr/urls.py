from django.conf.urls import url
from django.contrib import admin
from photos import views as photos_views
from users import views as user_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Photo URLs
    url(r'^$', photos_views.home, name='photos_home'),
    url(r'^photos/(?P<pk>[0-9]+)$', photos_views.detail, name='photo_detail'),

    # Users Urls
    url(r'^login$', user_views.login, name='users_login'),
    url(r'^logout$', user_views.logout, name='users_logout')
]
