
from os import name
import time

header='PREV_EXTRACT_TS;CURR_EXTRACT_TS;CRUD_ACTION;DOMAIN;PAYLOAD\n'
com = '2021-07-01-11.00.00.123456;2021-07-01-12.00.00.123999;?;BS_GENERAL          ;'
dp1 = '{"TABLE":"POSTDISTRIKT ","DATA": {"POSTD_NR":"'
dp3 = '","LANDE_KODE_CHA_2":"TT","POSTD_ADR":"TORSHAVN","POSTD_SAEK_NR":100,"OPDAT_TID":"1996-09-11-15.54.05.142262","USERID":"    U082"}}'
cs  = '{"TOTAL_ROWS":       ?}'

number = 65000

def timer_dec (base_fn):
    def enhanced_fn(* args , **kwargs): 
        start_time=time.time() 
        base_fn(*args,**kwargs)
        end_time=time.time()
        print (f"Task time : {end_time-start_time}  seconds")
    return enhanced_fn


@timer_dec
def createDataFile(name, size, line=''):
    deleteData(name)
    createFile(name, header)
  
    for x in range(size):
        parts = [com.replace('?', 'U'), dp1, str(x), dp3, '\n']
        line = line + ''.join(parts)
        if x % 10000 == 0:
            createFile(name,line)
            line=''
    createFile(name, line)

def createDataFileComprehension(name, size, line=''):
    deleteData(name)
    createFile(name, header)
    line = [ ' '.join([com.replace('?', 'U'), dp1, str(x), dp3, '\n']) for x in range(size) ]
  
    createFile(name, line)    
   
def saveSomeLines(line, name): 
    createFile(name,line)
    return ''

def deleteData(name):
     open(name, 'w').close()

def createFile(name, data):
    with open(name, 'a') as f:
        f.write(data)

def createCSFile(name,size):
    deleteData(name)
    createFile(name, header)
    line = com.replace('?','S') + cs.replace('?',f'{size}')
    createFile(name, line)

if __name__ == "__main__":
    createDataFileComprehension("./Create_csv_from_json/post_data.csv",number)
    # createCSFile ("./Create_csv_from_json/post_cs.csv",number)
