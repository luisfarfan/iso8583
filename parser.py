from .constants import *


class FullCargaParser(object):
    def __init__(self, tipo_operacion):
        # if tipo_operacion:
        self.OPERACION_REQUEST = {
            FullCargaOperationsRequest.ECHO_TEST.value: FullCargaOperationsRequest.ECHO_TEST,
            FullCargaOperationsRequest.OPERACION_VENTA.value: FullCargaOperationsRequest.OPERACION_VENTA,
            FullCargaOperationsRequest.OPERACION_DEVOLUCION.value: FullCargaOperationsRequest.OPERACION_DEVOLUCION,
            FullCargaOperationsRequest.OPERACION_CONSULTA.value: FullCargaOperationsRequest.OPERACION_CONSULTA,
            FullCargaOperationsRequest.OPERACION_CONSULTA_SALDO.value: FullCargaOperationsRequest.OPERACION_CONSULTA_SALDO,
        }.get(tipo_operacion)

        self.OPERACION_RESPONSE = {
            FullCargaOperationsResponse.ECHO_TEST.value: FullCargaOperationsResponse.ECHO_TEST,
            FullCargaOperationsResponse.OPERACION_VENTA.value: FullCargaOperationsResponse.OPERACION_VENTA,
            FullCargaOperationsResponse.OPERACION_DEVOLUCION.value: FullCargaOperationsResponse.OPERACION_DEVOLUCION,
            FullCargaOperationsResponse.OPERACION_CONSULTA.value: FullCargaOperationsResponse.OPERACION_CONSULTA,
            FullCargaOperationsResponse.OPERACION_CONSULTA_SALDO.value: FullCargaOperationsResponse.OPERACION_CONSULTA_SALDO,
        }.get(tipo_operacion)
