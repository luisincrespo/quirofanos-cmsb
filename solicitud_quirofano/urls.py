from django.conf.urls import patterns, include, url

urlpatterns = patterns('solicitud_quirofano.views',
    url(r'^solicitud$', 'solicitud', name='solicitud'),
    url(r'^mis_solicitudes$', 'mis_solicitudes', name='mis_solicitudes'),
)