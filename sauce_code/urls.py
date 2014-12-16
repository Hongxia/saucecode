from django.conf.urls import include, url

urlpatterns = [
    # Graphics URLs
    url(r'^graphics/', include('graphics.urls', namespace='graphics')),

    # Root-level redirects for common browser requests
    # url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'img/compressed/favicon.ico'), name='favicon.ico'),
    # url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots.txt'),
]