
from django.contrib import admin
from django.urls import path
from scraper.views import scrape, clear


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scrape),
    path('delete/', clear),
]
