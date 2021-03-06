from django.conf.urls import patterns, include, url

urlpatterns = patterns('medico.views',
    url(r'^solicitud_quirofano/(?P<ano>\d{4})/(?P<mes>\d{1,2})/(?P<dia>\d{1,2})/(?P<id_quirofano>\d+)/(?P<hora_inicio>\d{1,2}[.]([5]|[0]))/(?P<duracion_en_medias_horas>\d+)$', 'solicitud_quirofano', name='solicitud_quirofano'),
    url(r'^mis_solicitudes/(?P<estado>[a-z]+)/$', 'mis_solicitudes', name='mis_solicitudes'),
	url(r'^mis_solicitudes/(?P<estado>[a-z]+)/(?P<periodo>\d+)$', 'mis_solicitudes', name='mis_solicitudes'),
	url(r'^mis_solicitudes/cancelar_solicitud/(?P<pk>\d+)$', 'cancelar_solicitud', name='cancelar_solicitud'),
    url(r'^proximas_intervenciones/cancelar_intervencion/(?P<pk>\d+)$', 'cancelar_intervencion', name='cancelar_intervencion'),
    url(r'^proximas_intervenciones$', 'proximas_intervenciones', name='proximas_intervenciones'),
    url(r'^proximas_intervenciones/(?P<periodo>[a-z_]+)$', 'proximas_intervenciones', name='proximas_intervenciones'),
)
