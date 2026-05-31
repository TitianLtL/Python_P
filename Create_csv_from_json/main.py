
import time

header='PREV_EXTRACT_TS;CURR_EXTRACT_TS;CRUD_ACTION;DOMAIN;PAYLOAD\n'
com = '2021-07-01-11.00.00.123456;2021-07-01-12.00.00.123999;?;BS_GENERAL          ;'
dp1 = '{"TABLE":"POSTDISTRIKT ","DATA": {"POSTD_NR":"'
dp3 = '","LANDE_KODE_CHA_2":"TT","POSTD_ADR":"TORSHAVN","POSTD_SAEK_NR":100,"OPDAT_TID":"1996-09-11-15.54.05.142262","USERID":"    U082"}}'
cs  = '{"TOTAL_ROWS":       ?}'

number = 65000

def gen_lines(from_size, to_size):
    line = ''
    for x in range(from_size, to_size):
        parts = [com.replace('?', 'U'), dp1, str(x), dp3, '\n']
        line = line + ''.join(parts)
    yield line

def createDataFile2(name, size):
    deleteData(name)
    createFile(name, header)
  
    for x in range(0, 2):
        line = ''
        gen_lines_obj = gen_lines(x, x+1000)
        line = next(gen_lines_obj)
        createFile(name, line)

    
def deleteData(name):
     open(name, 'w').close()

def createFile(name, data):
    with open(name, 'a') as f:
        f.write(data)



if __name__ == "__main__":
    createDataFile2("./Create_csv_from_json/data_v2.csv",number)

