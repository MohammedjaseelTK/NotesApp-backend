from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # AUTH
    path('register/', Register.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),

    # NOTES
    path('notes/', NoteList.as_view(), name='notes'),                 # GET + POST
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note-detail'), # GET + PUT + DELETE
]