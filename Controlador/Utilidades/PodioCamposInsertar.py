'''
Created on 20 abr. 2017

@author: julian
'''

class PodioCamposInsertar(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    @staticmethod
    def CampoTexto(external_id,value):
        Campo={
            "external_id":external_id
            , "values":[
                            {"value":str(value)}
                        ]
        }
        return Campo
    
    @staticmethod
    def CampoTelefono(external_id,type,value):
        Campo={
            "external_id":external_id
            , "values":[
                             { "type": type, "value":str(value) }
                        ]
        }
        return Campo
    
    @staticmethod
    def CampoEmail(external_id,type,value):
        Campo={
            "external_id":external_id
            , "values":[
                             { "type": type, "value": str(value) }
                        ]
        }
        return Campo
    
    @staticmethod
    def CampoLink(external_id,url):
        Campo={
            "external_id":external_id
            , "values":[
                             { "embed": {"url":url},  }
                        ]
        }
        return Campo
    
    @staticmethod
    def CampoContacto(external_id,value):
        Campo={
            "external_id":external_id
            , "values":[
                            {"value":value}
                        ]
        }
        return Campo
    
    @staticmethod
    def CampoCategoria(external_id,value):
        Campo={
            "external_id":external_id
            , "values":[
                            {"value":value}
                        ]
        }
        return Campo
    
    @staticmethod
    def CampoAplicacion(external_id,value):
        Campo={
            "external_id":external_id
            , "values":[
                            {"value":value}
                        ]
        }
        return Campo