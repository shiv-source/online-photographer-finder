from django.urls import path
from .views import user


urlpatterns=[
    path('',user,name="user")
]

# urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
