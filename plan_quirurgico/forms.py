# -*- coding: utf-8 -*-
from django import forms

from quirofanos_cmsb.helpers.custom_validators import MensajeError, CodigoError

from quirofanos_cmsb.forms import BaseForm

class DuracionIntervencionQuirurgicaForm(BaseForm):
    ''' Formulario de ingreso de la duracion de una intervencion quirurgica para buscar horarios disponibles '''
    horas = forms.IntegerField(min_value=1, max_value=12, initial=1)
    minutos = forms.IntegerField(min_value=0, max_value=59, initial=0)
    id_intervencion = forms.IntegerField(widget=forms.HiddenInput, required=False)

class CambiarEstadoIntervencionQuirurgicaForm(BaseForm):
    ''' Formulario de actualizacion de estado de una intervencion quirurgica '''
    id_intervencion = forms.IntegerField(min_value=1, widget=forms.HiddenInput, required=False)
    estado_intervencion = forms.CharField(widget=forms.HiddenInput, required=False)

