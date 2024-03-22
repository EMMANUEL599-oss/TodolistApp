from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='todo/')),  # Redirect root path to 'todo/' URL
    path('todo/', include('todo.urls')),
    path('admin/', admin.site.urls),
]
