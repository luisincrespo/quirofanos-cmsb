# -*- coding: utf-8 -*-
import re
from django.utils.translation import ugettext as _

class ExpresionRegular():
    ''' Constantes que contienen expresiones regulares a ser utilizadas en validaciones de modelos y formularios '''
    CODIGO_TELEFONO = re.compile(r'^\d{4}$', re.UNICODE)
    NUMERO_TELEFONO = re.compile(r'^\d{7}$', re.UNICODE)
    NOMBRE_GENERAL = re.compile(r'^(\s|[^\W0-9_])*$', re.UNICODE)
    CEDULA_BD = re.compile(r'^(V-|E-)\d+$', re.UNICODE)
    TELEFONO_BD = re.compile(r'^\d{4}-\d{7}$', re.UNICODE)
    CEDULA = re.compile(r'^\d+$', re.UNICODE)
    NUMERO_EXPEDIENTE = re.compile(r'^\d{6}$', re.UNICODE)
    NUMERO_HABITACION = re.compile(r'^\d{3}$', re.UNICODE)

class MensajeError():
    ''' Constantes que contienen mensajes de error a ser utilizados en validaciones de modelos y formularios '''
    CODIGO_TELEFONO_INVALIDO = _(u'Código de teléfono inválido, debe contener exactamente 4 dígitos.')
    NUMERO_TELEFONO_INVALIDO = _(u'Número de teléfono inválido, debe contener exactamente 7 dígitos.')
    NOMBRE_GENERAL_INVALIDO = _(u'Nombre inválido, puede contener sólo letras y espacios.')
    CONTRASENAS_NO_COINCIDEN = _(u'Las contraseñas ingresadas no coinciden.')
    CEDULA_BD_INVALIDA = _(u'Cédula inválida, debe ser de la forma: V-XXX... ó E-XXX...')
    CEDULA_BD_NO_EXISTE = _(u'El número de cédula ingresado no corresponde a un médico.')
    TELEFONO_BD_INVALIDO = _(u'Teléfono inválido, debe ser de la forma: XXXX-XXXXXXX.')
    RIESGO_MALO_SIN_RAZON_BD = _(u'La razón del riesgo no puede ser nula si el riesgo es malo.')
    RIESGO_NO_MALO_CON_RAZON_BD = _(u'La razón del riesgo debe ser nula si el riesgo es distinto de malo.')
    RIESGO_MALO_SIN_RAZON = _(u'Se indicó que el riesgo es malo. Debe indicarse la razón del riesgo.')
    HORA_FIN_MENOR_HORA_INICIO = _(u'La hora de fin debe ser mayor que la hora de inicio.')
    CEDULA_INVALIDA = _(u'Cédula inválida, debe contener sólo números.')
    APELLIDO_INVALIDO = _(u'Apellido inválido, puede contener sólo letras y espacios.')
    EXISTE_USUARIO = _(u'El nombre de usuario ingresado ya existe.')
    NUMERO_EXPEDIENTE_INVALIDO = _(u'Número de expediente inválido, debe contener exactamente 6 dígitos.')
    NUMERO_HABITACION_INVALIDO = _(u'Número de habitación inválido, debe contener exactamente tres dígitos.')
    AREA_INGRESO_SIN_NUMERO_EXPEDIENTE = _(u'El área de ingreso de un paciente no puede existir sin un número de expediente asociado.')
    NUMERO_EXPEDIENTE_SIN_AREA_INGRESO = _(u'El número de expediente de un paciente no puede existir sin un área de ingreso asociada.')
    EXISTE_CUENTA = _(u'El médico asociado a la cédula ingresada ya ha solicitado su cuenta.')
    DURACION_MENOR_QUE_UNA_HORA = _(u'La duración de una intervención quirúrgica debe ser mínimo una hora.')
    PACIENTE_CON_EXPEDIENTE_SIN_ESPECIFICACION = _(u'Se indicó que el paciente posee expediente. Debe especificarse area de ingreso y número de expediente.')
    PACIENTE_HOSPITALIZADO_SIN_HABITACION = (u'Se indicó que el paciente está hospitalizado. Debe indicarse el número de habitación.')
    INTERVALO_INVALIDO = (u'El intervalo para el filtrado es invalido. La fecha Hasta debe ser mayor.')

class CodigoError():
    ''' Constantes que contienen codigos de error a ser utilizados en validaciones de modelos y formularios '''
    CODIGO_TELEFONO_INVALIDO = "codigo_telefono_invalido"
    NUMERO_TELEFONO_INVALIDO = "numero_telefono_invalido"
    NOMBRE_GENERAL_INVALIDO = "nombre_general_invalido"
    CONTRASENAS_NO_COINCIDEN = "contrasenas_no_coinciden"
    CEDULA_BD_INVALIDA = "cedula_bd_invalida"
    CEDULA_BD_NO_EXISTE = "cedula_bd_no_existe"
    TELEFONO_BD_INVALIDO = "telefono_bd_invalido"
    RIESGO_MALO_SIN_RAZON_BD = "riesgo_bd_malo_sin_razon"
    RIESGO_NO_MALO_CON_RAZON_BD = "riesgo_bd_no_malo_con_razon"
    RIESGO_MALO_SIN_RAZON = "riesgo_malo_sin_razon"
    HORA_FIN_MENOR_HORA_INICIO = "hora_fin_menor_hora_inicio"
    CEDULA_INVALIDA = "cedula_invalida"
    EXISTE_USUARIO = "existe_usuario"
    NUMERO_EXPEDIENTE_INVALIDO = "numero_expediente_invalido"
    NUMERO_HABITACION_INVALIDO = "numero_habitacion_invalido"
    AREA_INGRESO_SIN_NUMERO_EXPEDIENTE = "area_ingreso_sin_numero_expediente"
    NUMERO_EXPEDIENTE_SIN_AREA_INGRESO = "numero_expediente_sin_area_ingreso"
    EXISTE_CUENTA = "existe_cuenta"
    DURACION_MENOR_QUE_UNA_HORA = "duracion_menor_que_una_hora"
    PACIENTE_CON_EXPEDIENTE_SIN_ESPECIFICACION = "paciente_con_expediente_sin_especificacion"
    PACIENTE_HOSPITALIZADO_SIN_HABITACION = "paciente_hospitalizado_sin_habitacion"
    INTERVALO_INVALIDO = "intervalo_invalido"
