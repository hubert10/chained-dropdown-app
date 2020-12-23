from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='person_changelist'), name='home'),
    path('hr/', include('hr.urls')),
]
