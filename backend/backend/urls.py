from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings          
from django.conf.urls.static import static   
from accounts.views import ToggleSuperuserStatus
from accounts.views import ProfileView

from accounts.views import SignupView, LoginView, LogoutView
# from bits.views import BitViewSet
# from comedians.views import ComedianViewSet
# from podcasts.views import PodcastViewSet
# from tourdates.views import TourdateViewSet

# Create a new router
router = routers.DefaultRouter()

# Register ViewSets with the router
# router.register(r"bits", BitViewSet)
# router.register(r"comedians", ComedianViewSet)
# router.register(r"podcasts", PodcastViewSet)
# router.register(r"tourdates", TourdateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('toggle_superuser/<int:user_id>/', ToggleSuperuserStatus.as_view(), name='toggle_superuser'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

# Serving media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
