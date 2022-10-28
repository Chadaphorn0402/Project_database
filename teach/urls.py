from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('course/', testing ,name="course"),
    path('enroll/', enrolla, name="enroll"),
    path('enroll/', enrolla1, name="enroll2"),
    # path('enroll/', enrolla2, name="enroll3"),
    # path('enroll/', enrolla3, name="enroll4"),
    # path('enroll/', enrolla4, name="enroll5"),
    path('enrollment/', enrollmentt, name="enrollment")


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)