from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crispy/', include('crispy.urls', namespace='crispy')),
    path('htmx/', include('htmx.urls', namespace='htmx')),
]
