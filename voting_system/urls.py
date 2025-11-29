from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from vote.views import home_view, sa_politics_news, chatbot_view  # <-- import home_view too

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),              # homepage
    path('news/', sa_politics_news, name='news'),  # news page
    path('chatbot/', chatbot_view, name='chatbot'),# chatbot page
    path('', include('vote.urls')),                # include app urls if you have more
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
