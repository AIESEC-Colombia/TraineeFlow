'''
Created on 27 abr. 2017

@author: julian
'''

class aplicantes_traineeflow():
    '''
    classdocs
    '''

    codigo=None
    ep_id=None
    proyecto_id=None
    aplicacion_id=None
    comite_id=None
    
    def __init__(self,codigo
                    ,ep_id
                    ,proyecto_id
                    ,aplicacion_id
                    ,comite_id):
        '''
        Constructor
        '''
        self.codigo=codigo
        self.ep_id=ep_id
        self.proyecto_id=proyecto_id
        self.aplicacion_id=aplicacion_id
        self.comite_id=comite_id
        