'''
Created on 02/12/2013

@author: jesusropi
'''
from clientFEB import *

stub = ServiciosFEBSoap12ServiceStub()
xsd.settings.VALIDATE_ON_PARSE = False

def getTemporadasDisponiblesXCategoria(codCategoria, key):
    """
         Get the seasons for a category.
    """
    temporadasdisponiblesxcategoria = TemporadasDisponiblesXCategoria()
    temporadasdisponiblesxcategoria.key = key
    temporadasdisponiblesxcategoria.codCategoria = codCategoria
    temporadasdisponiblesxcategoriaresponse = stub.TemporadasDisponiblesXCategoria(temporadasdisponiblesxcategoria)
    return temporadasdisponiblesxcategoriaresponse

def getCategoriasDisponiblesXTemporada(idTemporada, key):
    """
         Get the category for a season.
    """
    categoriasDisponiblesXTemporada = CategoriasDisponiblesXTemporada()
    categoriasDisponiblesXTemporada.idTemporada = idTemporada
    categoriasDisponiblesXTemporada.key = key
    categoriasDisponiblesXTemporadaResponse = stub.CategoriasDisponiblesXTemporada(categoriasDisponiblesXTemporada)
    return categoriasDisponiblesXTemporadaResponse
    '''for items in categoriasDisponiblesXTemporadaResponse.CategoriasDisponiblesXTemporadaResult[0].CategoriaItems:
        items.CategoriaNombres[0] = str(items.CategoriaNombres[0])
        items.CategoriaIDs[0] = str(items.CategoriaIDs[0])
        print 'Nombre: ' + items.CategoriaNombres[0] + ' >  ID: ' + items.CategoriaIDs[0]'''

def getCategoriaXEquipoInscrito(idInscripcion, key):
    """
         Get the category for a team.
    """
    categoriaxequipoinscrito = CategoriaXEquipoInscrito()
    categoriaxequipoinscrito.idInscripcion = idInscripcion
    categoriaxequipoinscrito.key = key
    categoriaxequipoinscritoresponse = stub.CategoriaXEquipoInscrito(categoriaxequipoinscrito)
    return categoriaxequipoinscritoresponse.xml('resultadoporcategoriadeequipo')
    '''print 'Nombre de Categoria para id inscripcion 115: ' + str(categoriaxequipoinscritoresponse.CategoriaXEquipoInscritoResult[0].CategoriaNombres[0])'''

def getClasificacionXJornada(idJornada, key):
    """
         Get the clasification for a day.
    """
    clasificacionxjornada = ClasificacionXJornada()
    clasificacionxjornada.idJornada = idJornada
    clasificacionxjornada.key = key
    clasificacionxjornadaresponse = stub.ClasificacionXJornada(clasificacionxjornada)
    return clasificacionxjornadaresponse.xml('jornadasegunclaseficacion')
    '''print 'Equipos que juagaron jornada 250 por clasificacion:'
    for items in clasificacionxjornadaresponse.ClasificacionXJornadaResult[0].EquipoClasificacionItems:
        print items.AliasEquipos[0]'''

def getEquiposInscritosXCategoria(codCategoria, key):
    """
         Get the teams for a category.
    """
    equiposinscritosxcategoria = EquiposInscritosXCategoria()
    equiposinscritosxcategoria.codCategoria = codCategoria
    equiposinscritosxcategoria.key = key
    equiposinscritosxcategoriaresponse = stub.EquiposInscritosXCategoria(equiposinscritosxcategoria)
    return equiposinscritosxcategoriaresponse
    '''for items in equiposinscritosxcategoriaresponse.EquiposInscritosXCategoriaResult[0].EquipoItems:
        print items.AliasEquipos[0]'''

def getEstadisticasAcumuladasXEquipo(idInscripcion, key):
    """
         Get the stadistics for a team.
    """
    estadisticasacumuladasxequipo = EstadisticasAcumuladasXEquipo()
    estadisticasacumuladasxequipo.idInscripcion = idInscripcion
    estadisticasacumuladasxequipo.key = key
    estadisticasacumuladasxequiporesponse = stub.EstadisticasAcumuladasXEquipo(estadisticasacumuladasxequipo)
    return estadisticasacumuladasxequiporesponse
    #for items in estadisticasacumuladasxequiporesponse.EstadisticasAcumuladasXEquipoResult[0].Jugadoress[0].EstadisticaJugadorItems:
        #print items.Asistenciass[0], items.BalonesPers[0], items.BalonesRecs[0], items.ConvertidosDoss[0], items.ConvertidosTress[0], items.ConvertidosUnos[0],items.FaltasComs[0], items.FaltasRecs[0], items.IdJugadors[0], items.IntentosDoss[0], items.IntentosTress[0], items.IntentosUnos[0], items.Matess[0], items.NombreEquipos[0], items.NombreFases[0], items.Nombres[0], items.NumPartidoss[0], items.Puntoss[0], items.RebotesDefs[0], items.RebotesOfs[0], items.SegundosJugadoss[0], items.TaponesCons[0], items.TaponesFavs[0], items.Temporadas[0], items.TiempoJugados[0], items.Valoracions[0]
 
def getEstadisticasAcumuladasXJugador(idInscripcion,idJugador, key):
    """
         Get the stadistics for a player.
    """
    estadisticasacumuladasxjugador = EstadisticasAcumuladasXJugador()
    estadisticasacumuladasxjugador.idInscripcion = idInscripcion
    estadisticasacumuladasxjugador.idJugador = idJugador
    estadisticasacumuladasxjugador.key = key
    estadisticasacumuladasxjugadorresponse = stub.EstadisticasAcumuladasXJugador(estadisticasacumuladasxjugador)
    return estadisticasacumuladasxjugadorresponse
   
def getFasescodCategoria(idTemporada, codCategoria,key):
    """
         Get the phases for a category.
    """
    fases = Fases()
    fases.codCategoria = codCategoria
    fases.idTemporada = idTemporada
    fases.key = key
    fasesresponse = stub.Fases(fases)
    return fasesresponse
    
def getGrupos(idFase, key):
    """
         Get the groups.
    """
    grupos = Grupos()
    grupos.idFase = idFase
    grupos.key = key
    gruposresponse = stub.Grupos(grupos)
    return gruposresponse

def getJornadas(idGrupo, key):
    """
         Get the days.
    """
    jornadas = Jornadas()
    jornadas.idGrupo = idGrupo
    jornadas.key = key
    jornadasresponse = stub.Jornadas(jornadas)
    return jornadasresponse

def getPartido(idPartido, key):
    """
         Get the match.
    """
    partido = Partido()
    partido.idPartido = idPartido
    partido.key = key
    partidoresponse = stub.Partido(partido)
    return partidoresponse

def getPartidos(idJornada, key):
    """
         Get the matches for a day.
    """
    partidos = Partidos()
    partidos.idJornada = idJornada
    partidos.key = key
    partidosresponse = stub.Partidos(partidos)
    return partidosresponse


def getRanking(idGrupo, idJornada, idTipoRanking, key):
    """
         Get the ranking for a team and day.
    """
    ranking = Ranking()
    ranking.idGrupo = idGrupo
    ranking.idJornada = idJornada
    ranking.idTipoRanking = idTipoRanking
    ranking.key = key
    rankingresponse = stub.Ranking(ranking)
    return rankingresponse.xml('Ranking')

def getTemporadasDisponibles(key):
    """
         Get the seasons.
    """
    temporadasdisponibles = TemporadasDisponibles()
    temporadasdisponibles.key = key
    temporadasdisponiblesresponse = stub.TemporadasDisponibles(temporadasdisponibles)
    return temporadasdisponiblesresponse

def getTiposRanking(key):
    """
         Get the rankings.
    """
    tiposranking = TiposRanking()
    tiposranking.key = key
    tiposrankingresponse = stub.TiposRanking(tiposranking)
    return tiposrankingresponse.xml('tiposranking')
    


