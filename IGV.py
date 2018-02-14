'''
Created on 24 abr. 2017

@author: julian
'''
from Controlador.pypodio2 import api
from urllib.parse import  urlencode
from Controlador.Utilidades.ExtraerInformacionPodio import ExtraerInformacionPodio
from Controlador.Aplicaciones.UsuarioPodio import UsuarioPodio
from Controlador.Aplicaciones.Oportunidades import Oportunidades
from Controlador.Expa.Informacion import Informacion
from Controlador.Aplicaciones.Aplicantes import Aplicantes
#from Modelo.TraineeFlow.Operaciones import Operaciones
#from Modelo.TraineeFlow.Listas import *
import requests
import json
from datetime import datetime, timedelta

objUsuarioPodio=UsuarioPodio()
objOportunidades=Oportunidades()
objExtraerInformacionPodio=ExtraerInformacionPodio()
#objOperaciones=Operaciones()

#Declaracion de Variables
api_key=objUsuarioPodio.api_key
login=objUsuarioPodio.login
password=objUsuarioPodio.password
CodigoSecretoUsuario=objUsuarioPodio.CodigoSecretoUsuario
c = api.OAuthClient(api_key, CodigoSecretoUsuario, login, password)
objAplicantes=Aplicantes(c)
NumeroAPlicantesFaltante=0
data=c.Item.filter(
                int(objOportunidades.IdAplicacion), {
                    'limit': 500,
                    'filters':[
                                {
                                    "key":"programa",
                                    "values":1
                                }
                               ],
                },
            )["items"]
fields = [objExtraerInformacionPodio.makeDict(item,nested=c) for item in data]
objInformacion=Informacion('dev.colombia@ai.aiesec.org', 'ITcolombia1718')
token=objInformacion.getToken()
CuentaAplicantes=0
NumeroOportunidades=len(fields)
for field in fields:
    NumeroOportunidades=NumeroOportunidades-1
    print (str(NumeroOportunidades))
    Campos=field["values"].keys()
    idinternopodio=field["item"]    
    if("op-id" in Campos):
        if(str(field["values"]["op-id"]).isdigit()):
            IdOportunidad=int(field["values"]["op-id"])
            print(IdOportunidad)
            params = {"access_token":token
                      ,"filters[opportunity_id]": IdOportunidad
                      ,"filters[created_at][from]": (datetime.now()-timedelta(days=1)).strftime("%y-%m-%d")
                      ,"filters[created_at][to]":  ((datetime.now()).strftime("%y-%m-%d"))
                      }
            baseUrl = "https://gis-api.aiesec.org/{version}/{routes}?{params}"
            
            url=baseUrl.format(version='v2', routes="applications.json", params=urlencode(params, True))
            r = requests.get(url)
            if int(r.status_code)==200:
                Aplicaciones=json.loads(r.text)
                for Aplicacione in Aplicaciones["data"]:
                    Person=Aplicacione["person"]
                    Opportunity=Aplicacione["opportunity"]
                
                    ParametrosConsulta=[
                        {
                            "key":"title",
                            "values":str(Person["id"])
                                
                        },
                        {
                            "key":"relationship-2",
                            "values":idinternopodio
                        }                          
                       ]
                    PodioAPlicacion=objAplicantes.Consulta(ParametrosConsulta)
                    if(len(PodioAPlicacion)==0):   
                        NumeroAPlicantesFaltante=NumeroAPlicantesFaltante+1
                        CuentaAplicantes=CuentaAplicantes+1  
                        EPId=str(Person["id"])
                        Nombre=Person["full_name"]
                        Email=Person["email"]                    
                        ComiteHost=objAplicantes.getIdComitePodio(int(Opportunity["office"]["id"]))
                        HomeLC=Person["home_lc"]["name"]
                        HomeMC=Person["home_lc"]["country"]
                        IdProyecto=int(idinternopodio)
                        CiudadProyecto=Opportunity["location"]
                        LinkOPEXPA=Opportunity["url"]
                        objAplicantes.GuardarAplicante(EPId
                                                       , Nombre
                                                       , Email                                                   
                                                       , ComiteHost
                                                       , HomeLC
                                                       , HomeMC
                                                       , IdProyecto
                                                       , CiudadProyecto
                                                       , LinkOPEXPA)
