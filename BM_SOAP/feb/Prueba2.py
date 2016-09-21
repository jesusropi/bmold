from clientFEB import *
from soapbox import xsd

xsd.settings.VALIDATE_ON_PARSE = False

keygen = ['FEB_Generico']
stub = ServiciosFEBSoap12ServiceStub()

'''
    Resulatado de todos las categorias disponibles por temporada
'''

# if __name__ == '__main__':
#     categoriasDisponiblesXTemporada = CategoriasDisponiblesXTemporada()
#     categoriasDisponiblesXTemporada.idTemporada = [2013]
#     categoriasDisponiblesXTemporada.key = keygen
#     categoriasDisponiblesXTemporadaResponse = stub.CategoriasDisponiblesXTemporada(categoriasDisponiblesXTemporada)
#     print categoriasDisponiblesXTemporadaResponse.xml('categoriasdisponiblesportemporada')
#     for items in categoriasDisponiblesXTemporadaResponse.CategoriasDisponiblesXTemporadaResult[0].CategoriaItems:
#         items.CategoriaNombres[0] = str(items.CategoriaNombres[0])
#         items.CategoriaIDs[0] = str(items.CategoriaIDs[0])
#         print 'Nombre: ' + items.CategoriaNombres[0] + ' >  ID: ' + items.CategoriaIDs[0]
# 
# 
# '''
#     Resultado de todas las categorias por equipo inscrito
# '''
#   
# if __name__ == '__main__':
#     categoriaxequipoinscrito = CategoriaXEquipoInscrito()
#     categoriaxequipoinscrito.idInscripcion = [115]
#     categoriaxequipoinscrito.key = keygen
#     categoriaxequipoinscritoresponse = stub.CategoriaXEquipoInscrito(categoriaxequipoinscrito)
#     print categoriaxequipoinscritoresponse.xml('resultadoporcategoriadeequipo')
#     print 'Nombre de Categoria para id inscripcion 115: ' + str(categoriaxequipoinscritoresponse.CategoriaXEquipoInscritoResult[0].CategoriaNombres[0])
#  
# 
# '''
#     Resultado de todos las jordanas segun clasificacion
# '''
#  
# if __name__ == '__main__':
#     clasificacionxjornada = ClasificacionXJornada()
#     clasificacionxjornada.idJornada = [250]
#     clasificacionxjornada.key = keygen
#     clasificacionxjornadaresponse = stub.ClasificacionXJornada(clasificacionxjornada)
#     print clasificacionxjornadaresponse.xml('jornadasegunclaseficacion')
#     print 'Equipos que juagaron jornada 250 por clasificacion:'
#     for items in clasificacionxjornadaresponse.ClasificacionXJornadaResult[0].EquipoClasificacionItems:
#         print items.AliasEquipos[0]
# '''
#     Equipos inscritos por categoria
# '''
# 
# if __name__ == '__main__':
#     equiposinscritosxcategoria = EquiposInscritosXCategoria()
#     equiposinscritosxcategoria.codCategoria = [115]
#     equiposinscritosxcategoria.key = keygen
#     equiposinscritosxcategoriaresponse = stub.EquiposInscritosXCategoria(equiposinscritosxcategoria)
#     print equiposinscritosxcategoriaresponse.xml('inscritosporcategoria')
#     for items in equiposinscritosxcategoriaresponse.EquiposInscritosXCategoriaResult[0].EquipoItems:
#         print items.AliasEquipos[0]
# 
# '''
#     estadisticas de equipo
# '''
# 
# if __name__ == '__main__':
#     estadisticasacumuladasxequipo = EstadisticasAcumuladasXEquipo()
#     estadisticasacumuladasxequipo.idInscripcion = [115]
#     estadisticasacumuladasxequipo.key = keygen
#     estadisticasacumuladasxequiporesponse = stub.EstadisticasAcumuladasXEquipo(estadisticasacumuladasxequipo)
#     print estadisticasacumuladasxequiporesponse.xml('estadisticasequipo')
#     #for items in estadisticasacumuladasxequiporesponse.EstadisticasAcumuladasXEquipoResult[0].Jugadoress[0].EstadisticaJugadorItems:
#         #print items.Asistenciass[0], items.BalonesPers[0], items.BalonesRecs[0], items.ConvertidosDoss[0], items.ConvertidosTress[0], items.ConvertidosUnos[0],items.FaltasComs[0], items.FaltasRecs[0], items.IdJugadors[0], items.IntentosDoss[0], items.IntentosTress[0], items.IntentosUnos[0], items.Matess[0], items.NombreEquipos[0], items.NombreFases[0], items.Nombres[0], items.NumPartidoss[0], items.Puntoss[0], items.RebotesDefs[0], items.RebotesOfs[0], items.SegundosJugadoss[0], items.TaponesCons[0], items.TaponesFavs[0], items.Temporadas[0], items.TiempoJugados[0], items.Valoracions[0]
# 
# '''
#     Estadisticas acumulada por jugador 
# '''
# 
# if __name__ == '__main__':
#     estadisticasacumuladasxjugador = EstadisticasAcumuladasXJugador()
#     estadisticasacumuladasxjugador.idInscripcion = [115]
#     estadisticasacumuladasxjugador.idJugador = [33]
#     estadisticasacumuladasxjugador.key = keygen
#     estadisticasacumuladasxjugadorresponse = stub.EstadisticasAcumuladasXJugador(estadisticasacumuladasxjugador)
#     print estadisticasacumuladasxjugadorresponse.xml('estadisticasjugador')
#     
# '''
#     Fases
# '''
# if __name__ == '__main__':
#     fases = Fases()
#     fases.codCategoria = [115]
#     fases.idTemporada = [2012]
#     fases.key = keygen
#     fasesresponse = stub.Fases(fases)
#     print fasesresponse.xml('Fases')
# 
# '''
#     Grupos
# '''
# 
# if __name__ == '__main__':
#     grupos = Grupos()
#     grupos.idFase = [15296]
#     grupos.key = keygen
#     gruposresponse = stub.Grupos(grupos)
#     print gruposresponse.xml('Grupos')
# 
# 
# '''
#     Jornadas
# '''
#     
# if __name__ == '__main__':
#     jornadas = Jornadas()
#     jornadas.idGrupo = [29724]
#     jornadas.key = keygen
#     jornadasresponse = stub.Jornadas(jornadas)
#     print jornadasresponse.xml('Jornadas')
#     
# '''
#     Partido
# '''
#     
# if __name__ == '__main__':
#     partido = Partido()
#     partido.idPartido = [30158]
#     partido.key = keygen
#     partidoresponse = stub.Partido(partido)
#     print partidoresponse.xml('Patido')
# 
# '''
#     Partidos
# '''
#     
# if __name__ == '__main__':
#     partidos = Partidos()
#     partidos.idJornada = [20]
#     partidos.key = keygen
#     partidosresponse = stub.Partidos(partidos)
#     print partidosresponse.xml('Patidos')
# 
# '''
#     Ranking
# '''
# 
# if __name__ == '__main__':
#     ranking = Ranking()
#     ranking.idGrupo = [29724]
#     ranking.idJornada = [20]
#     ranking.idTipoRanking = [3]
#     ranking.key = keygen
#     rankingresponse = stub.Ranking(ranking)
#     print rankingresponse.xml('Ranking')
#     
# '''
#     Temporadas disponilbes
# '''
#     
# if __name__ == '__main__':
#     temporadasdisponibles = TemporadasDisponibles()
#     temporadasdisponibles.key = keygen
#     temporadasdisponiblesresponse = stub.TemporadasDisponibles(temporadasdisponibles)
#     print temporadasdisponiblesresponse.xml('temporadasdisponibles')
# 
# '''
#     Temporadas disponibles por categoria
# '''
# if __name__ == '__main__':
#     temporadasdisponiblesxcategoria = TemporadasDisponiblesXCategoria()
#     temporadasdisponiblesxcategoria.key = keygen
#     temporadasdisponiblesxcategoria.codCategoria = [110]
#     temporadasdisponiblesxcategoriaresponse = stub.TemporadasDisponiblesXCategoria(temporadasdisponiblesxcategoria)
#     print temporadasdisponiblesxcategoriaresponse.xml('temporadasdisponiblesporcategoria')

'''
    Tipos de ranking
'''

if __name__ == '__main__':
    tiposranking = TiposRanking()
    tiposranking.key = keygen
    tiposrankingresponse = stub.TiposRanking(tiposranking)
    print tiposrankingresponse.xml('tiposranking')
    #import StringIO
'''
    root = etree.XML(lista5)
    find_text = entree.XPath.SelectSingleNode('//currentSelectedNode/ancestor::childOfChild[0]')
    text = find_text(root)
    print(text)
    print(text.getparent().text)


    find_text = etree.XPath("//text()")
    text = find_text(root)[0]
    print(text)

    hasattr(text, 'getparent')
'''
    
    
    
import libxml2

listaxml = tiposrankingresponse.xml('tiposranking')
for tiporankingitem in tiposrankingresponse.TiposRankingResult[0].TipoRankingItems:
        print tiporankingitem.Ids, tiporankingitem.Nombres
doc = libxml2.parseDoc( listaxml )
root = doc.getRootElement()

print root.name
print root.content
child = root.children
# the children property returns the FIRST child of a node
while child is not None:
    if child.type == "element":
        # do something with the child node
        print child.name
    child = child.next

def walkTree(xmlnode):
        child = xmlnode.children
        while child is not None:
            if not child.isBlankNode():
                if child.type == "element":
                    childCount = int(child.xpathEval('count(*)'))

                    # a count of the ancestor nodes tells us how deep in the
                    # tree we are - lets just use it to indent our printed
                    # output
                    depth = int(child.xpathEval('count(ancestor::*)')) - 1
                    if childCount == 0:
                        # If the count of child elements is 0 then we
                        # have a node only containing text
                        print  depth * '\t' + child.name + ' : ' + child.content
                    else:
                        # If the node contains other child elements then
                        # we can recurse down the tree
                        print depth * '\t' + child.name
                        walkTree(child)

            child = child.next
#walkTree(root)
