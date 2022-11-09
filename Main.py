import json     # manipulate json
import requests # consume API
import psycopg2 # connect to database
from time import sleep # for sleep()


# uses API to get quotation of a coin
def api_quotation():  
    api_url,coin = "https://economia.awesomeapi.com.br/json/last/", "EUR-BRL"

    try:
        response = requests.get(api_url+coin)
    except Exception as e:
        print(e)
    
    if response.status_code != 200:
        ret = "Unknown"
    else:
        ret = response.content.decode()
    
    return json.loads(ret)

def generate_insert_query(quotation):
    key, value = '', ''
    
    for header in quotation:
        for x, iterator in enumerate(quotation[header]):
            if x != len(quotation[header]) - 1:
                key += iterator + ', '
                value += "'" + quotation[header][iterator] + "', "
            else:
                key += iterator
                value += "'" + quotation[header][iterator] + "'"

    return query_format(key, value)

    
def query_format(key, value):
    _key = 'INSERT INTO collection.euro(' + key + ')\n'
    _value = 'VALUES(' + value + ');'

    return _key + _value

def connection_cursor():
    connection_string = "host= 127.0.0.1" + " dbname= quotation" + " user= postgres" + " password= xxx" + " port = 5432"
    origin_connection = psycopg2.connect(connection_string)
    origin_connection.autocommit = True

    return origin_connection.cursor()

def execute_query(query_str, cursor:psycopg2.extensions.cursor):
    cursor.execute(query_str)

def main():

    time_performed = 0

    while 1 != 0:
        print('Execution time: {0}'.format(time_performed))

        print('#'*24+'\n-[Consumindo API]')
        quotation = api_quotation()
        
        print('-[Inserindo dados no BD]')
        execute_query(generate_insert_query(quotation), connection_cursor())

        print('-[Hibernando]\n'+'#'*24)
        time_performed += 1

        sleep(.9)

if __name__ == "__main__":
    main()
    exit()
