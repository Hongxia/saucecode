from django.views.generic import TemplateView

class RayTracingView(TemplateView):
    template_name = 'raytracing.html'

class ScanLineView(TemplateView):
    template_name = 'scanline.html'