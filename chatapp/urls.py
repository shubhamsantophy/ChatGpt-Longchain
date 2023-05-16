from django.urls import path, include
from chatapp.views import *

urlpatterns = [

    path('upload_pdf/', UploadPdfView.as_view(), name='upload_pdf'),

] 

