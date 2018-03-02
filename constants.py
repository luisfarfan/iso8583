from enum import Enum


class FullCargaTipoOperacion(Enum):
    ECHO_TEST = 1
    OPERACION_VENTA = 2
    OPERACION_DEVOLUCION = 3
    OPERACION_CONSULTA = 4
    OPERACION_CONSULTA_SALDO = 5


class FullCargaTramaProperties(object):
    bytesValue = None

    def __init__(self, order, iso, campo, tipo, tamanio):
        self.order = order
        self.iso = iso
        self.campo = campo
        self.tipo = tipo
        self.tamanio = tamanio
        self.real_value = None

    def setBytes(self, bytes):
        self.bytesValue = bytes

    def getBytes(self):
        return self.bytesValue


class FullCargaTypeField(Enum):
    # Son los tipos de campos que permite la documetacion de FULLCARGA
    HEXA = 'HEXA'
    BCD = 'BCD'
    ASCII = 'ASCII'
    V = 'V'
    LLV = 'LLV'


class FullCargaResponseCode(Enum):
    OK = b'00'
    DELAYED = b'01'


class FullCargaCommonFields(object):
    # ToDo falta ajustar los campos, con las propiedades exactas que dicen en la documentación
    def __init__(self):
        self.MESSAGE_LENGTH = FullCargaTramaProperties(0, 131, 'MESSAGE_LENGTH', FullCargaTypeField.HEXA, 2)
        self.TPDU = FullCargaTramaProperties(1, 132, 'TPDU', FullCargaTypeField.HEXA, 5)
        self.TYPE = FullCargaTramaProperties(2, 133, 'TYPE', FullCargaTypeField.HEXA, 2)
        self.BITMAP = FullCargaTramaProperties(3, 1, 'BITMAP', FullCargaTypeField.HEXA, 8)


class EchoTestRequest(FullCargaCommonFields):
    def __init__(self):
        super(EchoTestRequest, self).__init__()
        self.PROCCES_CODE = FullCargaTramaProperties(4, 3, 'PROCCES CODE', FullCargaTypeField.BCD, 3)
        self.STAN = FullCargaTramaProperties(5, 11, 'STAN', FullCargaTypeField.BCD, 3)
        self.TIME = FullCargaTramaProperties(6, 12, 'TIME', FullCargaTypeField.BCD, 3)
        self.DATE = FullCargaTramaProperties(7, 13, 'DATE', FullCargaTypeField.BCD, 2)


class EchoTestResponse(FullCargaCommonFields):
    def __init__(self):
        super(EchoTestResponse, self).__init__()
        self.PROCCES_CODE = FullCargaTramaProperties(4, 3, 'PROCCES CODE', FullCargaTypeField.BCD, 3)
        self.STAN = FullCargaTramaProperties(5, 11, 'STAN', FullCargaTypeField.BCD, 3)
        self.TIME = FullCargaTramaProperties(6, 12, 'TIME', FullCargaTypeField.BCD, 3)
        self.DATE = FullCargaTramaProperties(7, 13, 'DATE', FullCargaTypeField.BCD, 2)
        self.RESPONSE_CODE = FullCargaTramaProperties(8, 39, 'RESPONSE CODE', FullCargaTypeField.ASCII, 2)


class OperacionVentaRequest(FullCargaCommonFields):
    def __init__(self):
        super(OperacionVentaRequest, self).__init__()
        self.TERMINAL_ID = FullCargaTramaProperties(9, 41, 'TERMINAL ID', FullCargaTypeField.ASCII, 8)


class OperacionVentaResponse(FullCargaCommonFields):
    def __init__(self):
        super(OperacionVentaResponse, self).__init__()


class OperacionDevolucionRequest(FullCargaCommonFields):
    def __init__(self):
        super(OperacionDevolucionRequest, self).__init__()


class OperacionDevolucionResponse(FullCargaCommonFields):
    def __init__(self):
        super(OperacionDevolucionResponse, self).__init__()


class OperacionConsultaRequest(FullCargaCommonFields):
    def __init__(self):
        super(OperacionConsultaRequest, self).__init__()


class OperacionConsultaResponse(FullCargaCommonFields):
    def __init__(self):
        super(OperacionConsultaResponse, self).__init__()


class OperacionConsultaSaldoRequest(FullCargaCommonFields):
    def __init__(self):
        super(OperacionConsultaSaldoRequest, self).__init__()


class OperacionConsultaSaldoResponse(FullCargaCommonFields):
    def __init__(self):
        super(OperacionConsultaSaldoResponse, self).__init__()


class FullCargaOperationsRequest(Enum):
    ECHO_TEST = EchoTestRequest()
    OPERACION_VENTA = OperacionVentaRequest()
    OPERACION_DEVOLUCION = OperacionDevolucionRequest()
    OPERACION_CONSULTA = OperacionConsultaRequest()
    OPERACION_CONSULTA_SALDO = OperacionConsultaSaldoRequest()


class FullCargaOperationsResponse(Enum):
    ECHO_TEST = EchoTestResponse()
    OPERACION_VENTA = OperacionVentaResponse()
    OPERACION_DEVOLUCION = OperacionDevolucionResponse()
    OPERACION_CONSULTA = OperacionConsultaResponse()
    OPERACION_CONSULTA_SALDO = OperacionConsultaSaldoResponse()
