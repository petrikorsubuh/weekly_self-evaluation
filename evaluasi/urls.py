"""evaluasi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from apps.member import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.FromRegister.as_view()),
    path('register/add', views.Register.as_view()),
    path('login/', views.LoginView.as_view()),
    path('login/prosses', views.LoginProsses.as_view()),
    path('logout/', views.Logout.as_view()),
    path('member_landingPage/', views.MemberLandingPage.as_view()),

    #categori
    path('targets/', include(('apps.targets.urls', 'targets'), namespace='targets')),
    path('targets/achievement/', include(('apps.achievement.urls', 'achievement'), namespace='achievement')),

    #api
    # path('api/',include('rest_framework.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

