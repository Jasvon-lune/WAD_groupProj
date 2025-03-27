from django.urls import path
from rango import views
from tango_with_django_project import settings
from django.conf.urls.static import static


app_name = 'rango'

urlpatterns = [
    path('tNindex', views.tNindex, name='tNindex'),
    path('tNcourse', views.tNcourse, name='tNcourse'),
    path('tNlogin', views.tNlogin, name='tNlogin'),
    path('tNnote', views.tNnote, name='tNnote'),
    path('tNregister', views.tNregister, name='tNregister'),
    path('tNsearch', views.tNsearch, name='tNsearch'),
    path('tNupload/<int:NoteID>/', views.tNupload, name='tNupload'),
    path('tNupload/', views.tNupload, name='tNupload'),
    path('tNuser', views.tNuser, name='tNuser'),
    path('tNnote/<int:NoteID>/', views.tNnote, name = 'tNnote'),
    path('tNnotes/<str:CourseID>/', views.tNnotes, name = "tNnotes"),
    path('serve_docx/<int:NoteID>/', views.serve_docx, name='serve_docx'),
    path('logout/', views.user_logout, name='logout'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

