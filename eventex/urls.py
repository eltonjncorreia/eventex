from django.conf.urls import url, include
from django.contrib import admin
from eventex.core.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
]
