# study_management/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.urls import get_resolver

def show_urls(request):
    # Get all patterns from URL resolver
    resolver = get_resolver()
    all_urls = [f"{pattern}" for pattern in resolver.reverse_dict.keys()]
    return HttpResponse("<br>".join(sorted(all_urls)), content_type="text/html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studies/', include('studies.urls')),
    path('debug/urls/', show_urls),  # Add this line to debug URLs
]
