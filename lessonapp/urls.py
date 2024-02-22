from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from lessonapp.views import user_orders, base_page, upload_photo, show_products, show_users


urlpatterns = [
    path('users/<int:pk_user>', user_orders, name='user_orders'),
    path('', base_page, name='base_page'),
    path('upload_photo/<int:pk_products>', upload_photo, name='upload_photo'),
    path('show_products', show_products, name='show_products'),
    path('show_users', show_users, name='show_users'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
