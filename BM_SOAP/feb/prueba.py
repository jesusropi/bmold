'''
Created on 15/11/2013

@author: jesusropi
'''
from clientFEBPrueba2 import ServiciosFEBSoap12ServiceStub, CategoriasDisponiblesXTemporada, TemporadasDisponibles, TemporadasDisponiblesResponse
from soapbox import settings


# settings.VALIDATE_ON_PARSE = False

if __name__ == '__main__':
    from datetime import datetime
    stub = ServiciosFEBSoap12ServiceStub()
#     categoriasDisponiblesXTemporada = CategoriasDisponiblesXTemporada()
#     categoriasDisponiblesXTemporada.idTemporada = 2013
#     categoriasDisponiblesXTemporada.key = 'FEB_Generico'
#     categoriasDisponiblesXTemporadaResponse = stub.CategoriasDisponiblesXTemporada(categoriasDisponiblesXTemporada)
    temporadasDisponibles = TemporadasDisponibles();
    temporadasDisponibles.key = ['FEB_Generico']
    temporadasDisponiblesResponse = stub.TemporadasDisponibles(temporadasDisponibles)
    print temporadasDisponiblesResponse.xml('')
    
#     print status
#     stub = PutOpsPortServiceStub()
#     ops = Ops()
#     ops.aircraft = "LN-KKU"
#     ops.flight_number = "1234"
#     ops.type = "COMMERCIAL"
#     ops.takeoff_airport = Airport.create(code_type="IATA", code="WAW")
#     ops.takeoff_datetime = datetime.now()
#     ops.landing_airport = Airport.create(code_type="ICAO", code="EGLL")
#     ops.landing_datetime = datetime.now()
#     status = stub.PutOps(ops)
#     print status.action, status.id