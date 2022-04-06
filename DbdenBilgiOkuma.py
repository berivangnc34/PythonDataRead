# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
import os, sys

from openpyxl import Workbook,load_workbook
import psycopg2
#import xlsxwriter
import requests

db_host = '10.98.228.153'
db_name = 'atlas_db'
db_user = 'saatcms'
db_pass = 'cms123'
port = '5432'

try:
    connection=psycopg2.connect(dbname=db_name,user=db_user,password=db_pass,host=db_host,port=port)
    
    sql_query="select video_operation_folder_name from atlas_cms_vod.content where type='EPISODE' and parent_series_id='5771' order by id desc "
    cur=connection.cursor()
    cur.execute(sql_query)
    #tüm kayıtları al
    records =cur.fetchall() #getir
    print(cur.rowcount)
    
   
    

    for row in records:
        #print("parent_series_id",row[0],"\n")
        #print(type(row[1]))
        print(row[0])
        
        
        
        with open('DbdenGelenBilgiler.txt','a') as file :
            content=row[0]
            file.writelines(content) 
            file.writelines('\n')
            file.close()
            
        
        
except psycopg2.Error as e:
    print('tablodaki veriler okunmuyor.',e)
    
    
   

finally:
    if connection:
        connection.close()
        cur.close()
        print('sql bağlantısı kapandı')
        
        

