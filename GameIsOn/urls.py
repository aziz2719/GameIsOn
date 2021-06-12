"""GameIsOn URL Configuration
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from users.views import UserRegisterView, UserLoginView


schema_view = get_schema_view(
   openapi.Info(
      title="Club Api",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register/', UserRegisterView.as_view()),
    path('user/login/', UserLoginView.as_view()),
    path('club/', include('clubs.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += router.urls