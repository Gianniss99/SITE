from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import AboutUsView


urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('about_us', AboutUsView.as_view(), name='about_us'),  # Προσθήκη του URL για τη σελίδα "About Us"
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
