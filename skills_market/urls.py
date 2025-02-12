"""skills_market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from sm_projects.api.viewset import ProjectViewSet
from sm_employees.api.viewset import EmployeeViewSet
from sm_skills.api.viewset import SkillsViewSet
from sm_search.api.view import SearchProxy

api_router = DefaultRouter()
api_router.register('projects', ProjectViewSet)
api_router.register('employees', EmployeeViewSet)
api_router.register('skills', SkillsViewSet)

api_urls = api_router.urls
api_urls.append(
    url(r'^search/', SearchProxy.as_view())
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_router.urls, namespace='API'))
]


