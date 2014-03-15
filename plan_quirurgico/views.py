from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def calendario(request):
	''' Controlador correspondiente al calendario de disponibilidad de quirofanos por mes

	Parametros:
	request -> Solicitud HTTP '''

	return render_to_response('plan_quirurgico/calendario.html')

def plan_dia(request):
	''' Controlador correspondiente al detalle del plan quirurgico por dia

	Parametros:
	request -> Solucitud HTTP '''

	return render_to_response('plan_quirurgico/plan_dia.html')