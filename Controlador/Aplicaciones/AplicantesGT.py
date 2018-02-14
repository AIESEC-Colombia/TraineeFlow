'''
Created on 24 abr. 2017

@author: julian
'''
from Controlador.Utilidades.PodioCamposInsertar import PodioCamposInsertar
class AplicantesGT():
    '''
    classdocs
    '''

    IdAPlicacion=18428685
    CodigoAPlicacion="5cd9915ae91e4585b71ef2861fcbbe86"
    Client=None
    def __init__(self, Client):
        '''
        Constructor
        '''
        self.Client=Client
    
    def GuardarAplicante(self
                         ,EPId
                         ,Nombre
                         ,Email                         
                         ,ComiteHost
                         ,HomeLC
                         ,HomeMC
                         ,IdProyecto
                         ,CiudadProyecto
                         ,LinkOPEXPA
                         ,TipoAplicacion):
        
        attributes=  {
            "fields":[ ]
        }
        attributes["fields"].append(PodioCamposInsertar.CampoCategoria("programa", TipoAplicacion)) 
        if(EPId!=""):
            attributes["fields"].append(PodioCamposInsertar.CampoTexto("title", EPId))
        
        if(Nombre!=""):
            attributes["fields"].append(PodioCamposInsertar.CampoTexto("nombre", Nombre))
        
        if(Email!=""):
            attributes["fields"].append(PodioCamposInsertar.CampoTexto("email", Email))       
        
        
        if(ComiteHost!=""):
            attributes["fields"].append(PodioCamposInsertar.CampoCategoria("comite-host", ComiteHost))
        
        if(HomeLC!=""):
            attributes["fields"].append(PodioCamposInsertar.CampoTexto("home-lc", HomeLC))
            
        if(HomeMC!=""):
            attributes["fields"].append(PodioCamposInsertar.CampoTexto("host-lc", HomeMC))
        
        if(IdProyecto!=""):
            attributes["fields"].append(PodioCamposInsertar.CampoAplicacion("relationship-2", IdProyecto))
        
        if(CiudadProyecto!=""):
            attributes["fields"].append(PodioCamposInsertar.CampoAplicacion("ciudad-donde-desarrolla-el-proyecto", CiudadProyecto))
        
        if(LinkOPEXPA!=""):
            attributes["fields"].append(PodioCamposInsertar.CampoAplicacion("link-de-la-op-en-expa", LinkOPEXPA))
        
        self.Client.Item.create(self.IdAPlicacion, attributes)
    
    def Consulta(self,Filters):
        data=self.Client.Item.filter(
                int(self.IdAPlicacion), {
                    'limit': 500,
                    'filters':Filters,
                },
            )["items"]
        return data
    
    def getIdComitePodio(self,Id):
        lstComites={
                2018 : {'Comite' : "Bogota", 'ValorPodio': 1},
                1395 : {'Comite': "ANDES", 'ValorPodio': 2},
                1868 : {'Comite' : "Armenia", 'ValorPodio': 3},                                               
                759 : {'Comite' : "BUCARAMANGA", 'ValorPodio': 4},
                915 : {'Comite' : "CALI", 'ValorPodio': 5},                                
                858 : {'Comite' : "CARTAGENA", 'ValorPodio': 6},
                1737 : {'Comite' : "CENTRAL", 'ValorPodio': 7},
                1738 : {'Comite' : "CUCUTA", 'ValorPodio': 8},                
                1198 : {'Comite' : "EAFIT", 'ValorPodio': 9},
                509 : {'Comite' : "EAN", 'ValorPodio': 10},
                1505 : {'Comite' : "ECI", 'ValorPodio': 11},
                1858 : {'Comite' : "EXTERNADO", 'ValorPodio': 12},                
                1165 : {'Comite' : "JAVERIANA", 'ValorPodio': 13},
                1739 : {'Comite' : "JAVERIANA CALI", 'ValorPodio': 14},                
                661 : {'Comite' : "MANIZALES", 'ValorPodio': 15},
                510 : {'Comite' : "MONTERIA", 'ValorPodio': 16},
                1745 : {'Comite' : "NEIVA", 'ValorPodio': 17},                
                1756 : {'Comite' : "PASTO", 'ValorPodio': 18},
                825 : {'Comite' : "PEREIRA", 'ValorPodio': 19},
                1740 : {'Comite' : "Popayan", 'ValorPodio': 20},
                1919 : {'Comite' : "Riohacha", 'ValorPodio': 21},
                428 : {'Comite' : "ROSARIO", 'ValorPodio': 22},
                1921 : {'Comite' : "SAN GIL", 'ValorPodio': 23},
                1812 : {'Comite' : "Santa Marta", 'ValorPodio': 24},
                1747 : {'Comite' : "SINCELEJO", 'ValorPodio': 25},
                294 : {'Comite' : "TOLIMA", 'ValorPodio': 26},
                1754 : {'Comite' : "TULUA", 'ValorPodio': 27},
                1877 : {'Comite' : "TUNJA", 'ValorPodio': 28},
                1746 : {'Comite' : "UdeA", 'ValorPodio': 29},
                173 : {'Comite' : "UNIATLANTICO", 'ValorPodio': 30},
                1469 : {'Comite' : "UNINORTE", 'ValorPodio': 31},
                1479 : {'Comite' : "UPB", 'ValorPodio': 32},
                172 : {'Comite' : "VALLEDUPAR", 'ValorPodio': 33},
                1920 : {'Comite' : "Villavicencio", 'ValorPodio': 34},
                1832 : {'Comite' : "MC CO", 'ValorPodio': 35},
                1923 : {'Comite' : "FLORENCIA", 'ValorPodio': 36}, 
                2052 : {'Comite' : "APC", 'ValorPodio': 37}, 
                }
        return lstComites[Id]['ValorPodio']
        