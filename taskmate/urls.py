from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', todolist_views.index, name='index'),
    path('todolist/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('contact-us', todolist_views.contact, name='contact'),
    path('about-us', todolist_views.about, name='about'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)