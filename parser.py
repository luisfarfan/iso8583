from constants import *


class FullCargaProccess:
    pass


class FullCargaParser(FullCargaProccess):
    # tamaño del ISO que se debe de calcular
    LENGTH_ISO = 0
    # bytearray de envio o respuesta, el socket de igual manera va responder con un bytearray
    BYTE_ARRAY = bytearray(0)
    OPERACION_RESPONSE_DICT = {}
    OPERACION_RESPONSE_LIST = []

    def __init__(self, tipo_operacion):
        # mapeando en un diccionario los diferentes tipos de operaciones de ENVIO para FULLCARGA
        self.OPERACION_REQUEST = {
            FullCargaTipoOperacion.ECHO_TEST.value: FullCargaOperationsRequest.ECHO_TEST.value,
            FullCargaTipoOperacion.OPERACION_VENTA.value: FullCargaOperationsRequest.OPERACION_VENTA.value,
            FullCargaTipoOperacion.OPERACION_DEVOLUCION.value: FullCargaOperationsRequest.OPERACION_DEVOLUCION.value,
            FullCargaTipoOperacion.OPERACION_CONSULTA.value: FullCargaOperationsRequest.OPERACION_CONSULTA.value,
            FullCargaTipoOperacion.OPERACION_CONSULTA_SALDO.value: FullCargaOperationsRequest.OPERACION_CONSULTA_SALDO.value,
        }.get(tipo_operacion)

        # mapeando en un diccionario los diferentes tipos de operaciones de RESPUESTA para FULLCARGA
        self.OPERACION_RESPONSE = {
            FullCargaTipoOperacion.ECHO_TEST.value: FullCargaOperationsResponse.ECHO_TEST.value,
            FullCargaTipoOperacion.OPERACION_VENTA.value: FullCargaOperationsResponse.OPERACION_VENTA.value,
            FullCargaTipoOperacion.OPERACION_DEVOLUCION.value: FullCargaOperationsResponse.OPERACION_DEVOLUCION.value,
            FullCargaTipoOperacion.OPERACION_CONSULTA.value: FullCargaOperationsResponse.OPERACION_CONSULTA.value,
            FullCargaTipoOperacion.OPERACION_CONSULTA_SALDO.value: FullCargaOperationsResponse.OPERACION_CONSULTA_SALDO.value,
        }.get(tipo_operacion)

        # almacenando el valor de respuesta en formato dict
        self.OPERACION_RESPONSE_DICT = self.OPERACION_RESPONSE.__dict__
        # calculando el length del ISO de envio o respuesta
        self.__calculateLength()
        # creando una lista segun el tipo de operacion, y se ordena segun su campo "order"
        self.__operationResponseToList()

    def __calculateLength(self):
        for attr in self.OPERACION_RESPONSE.__dict__:
            if isinstance(attr, str):
                self.LENGTH_ISO = self.LENGTH_ISO + self.OPERACION_RESPONSE.__getattribute__(attr).tamanio

    def setByteArrayISO(self, bytearray):
        self.BYTE_ARRAY = bytearray
        self.__setValues()

    def getRawIso(self):
        rawResponse = []
        for key in self.OPERACION_RESPONSE_LIST:
            rawResponse.append(key.__dict__)
        return rawResponse

    def getValueFromISO(self, iso, parse=True):
        for key in self.OPERACION_RESPONSE_DICT:
            if self.OPERACION_RESPONSE_DICT[key].iso == iso:
                isoreturn = self.__getValueFromIso(self.OPERACION_RESPONSE_DICT[key])
                if isoreturn:
                    if parse:
                        return self.__convertToRealValue(self.BYTE_ARRAY[isoreturn[0]:isoreturn[0] + isoreturn[1]],
                                                         self.OPERACION_RESPONSE_DICT[key].tipo.value)
                    return self.BYTE_ARRAY[isoreturn[0]:isoreturn[0] + isoreturn[1]]
        return None

    def __setValues(self):
        for i, key in enumerate(self.OPERACION_RESPONSE_LIST):
            self.OPERACION_RESPONSE_LIST[i].real_value = self.getValueFromISO(key.iso)

    def __getValueFromIso(self, iso_body):
        initial = 0
        for key in self.OPERACION_RESPONSE_LIST:
            if key.iso != iso_body.iso:
                initial = initial + key.tamanio
            else:
                break
        return initial, iso_body.tamanio

    # @ToDo faltaria poner las demas validaciones segun tipo de parametro
    def __convertToRealValue(self, bytes, type):
        if type == FullCargaTypeField.HEXA.value:
            return int(bytes.hex(), 16)
        elif type == FullCargaTypeField.ASCII.value:
            return bytes.decode('ascii')
        else:
            return bytes.hex()

    def __operationResponseToList(self):
        for attr in self.OPERACION_RESPONSE_DICT:
            self.OPERACION_RESPONSE_LIST.append(self.OPERACION_RESPONSE.__getattribute__(attr))
        self.OPERACION_RESPONSE_LIST.sort(key=lambda x: x.order)
