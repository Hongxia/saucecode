from django.conf.urls import url

from .views import RayTracingView

urlpatterns = [
    url(r'^raytracing/', RayTracingView.as_view(), name='raytracing'),
]