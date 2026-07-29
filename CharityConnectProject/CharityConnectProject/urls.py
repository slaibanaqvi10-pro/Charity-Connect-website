from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    # Front pages (Home, About, Services, Gallery, Campaigns, Donate)
    path('', include("portal.url")),
    path('admin/', admin.site.urls),

    # Donation App
    path('donation/', include("donation.url")),

    # User Auth App
    path('user/', include("user.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
