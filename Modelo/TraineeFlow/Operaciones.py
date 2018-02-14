'''
Created on 27 abr. 2017

@author: julian
'''
from Modelo.Conexion import Conexion
from Modelo.TraineeFlow.Listas import aplicantes_traineeflow
class Operaciones():
    '''
    classdocs
    '''

    
    def __init__(self):
        '''
        Constructor
        '''
    def Insertar(self,aplicantes_traineeflow):
        sql=" insert into aplicantes_traineeflow ( "
        sql=sql+"  ep_id, proyecto_id, aplicacion_id ,comite_id ) "
        sql=sql+" values( "        
        sql=sql+"  "+str(aplicantes_traineeflow.ep_id)
        sql=sql+" , "+str(aplicantes_traineeflow.proyecto_id)
        sql=sql+" , "+str(aplicantes_traineeflow.aplicacion_id)
        sql=sql+" , "+str(aplicantes_traineeflow.comite_id)
        sql=sql+" )"
        objConexion=Conexion()
        objConexion.Connect()
        objConexion.ExecuteQuery(sql)
        objConexion.Disconnect()
        
    def ConsultarEPIDOportunidadID(self,ep_id,proyecto_id):
        lst=[]
        sql=" select codigo ,ep_id ,proyecto_id ,aplicacion_id ,comite_id  "
        sql=sql+" from aplicantes_traineeflow "
        sql=sql+" where ep_id="+str(ep_id)+" "
        #sql=sql+" and proyecto_id="+proyecto_id+"  "
        objConexion=Conexion()
        objConexion.Connect()
        cursor=objConexion.Consult(sql)
        for row in cursor:
            objaplicantes_traineeflow=aplicantes_traineeflow(row['codigo']
                                                             , row['ep_id']
                                                             , row['comite_id']
                                                             , row['aplicacion_id']
                                                             , row['proyecto_id'])
            lst.append(objaplicantes_traineeflow)
        objConexion.Disconnect()
        return lst
        
        