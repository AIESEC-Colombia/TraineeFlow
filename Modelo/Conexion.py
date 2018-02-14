#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql.cursors
class Conexion(object):
    user="root"
    password="valarmorghulis"
    host="127.0.0.1"
    db="podio_expa"
    charset='utf8mb4'
    connection=None
    cursor=None
    """docstring for Conexion."""
    def __init__(self):
        """"""
    def Connect(self):
        self.connection=pymysql.Connect(host=self.host,
                                     user=self.user,
                                     password=self.password,
                                     db=self.db,
                                     charset=self.charset,
                                     cursorclass=pymysql.cursors.DictCursor)
    def Disconnect(self):
        if(self.cursor!=None):
            self.cursor.close()
            self.cursor=None
        self.connection.close()
        
       

    def Consult(self,sql):
        self.cursor=self.connection.cursor()
        self.cursor.execute(sql)
        return self.cursor
    
    def ExecuteQuery(self,sql):
        self.cursor=self.connection.cursor()
        self.cursor.execute(sql)
        self.connection.commit()
       
