'''Simple example of connecting from Python to a Postgresql database'''

import sqlalchemy
#from sqlalchemy import Table, Column, Integer, String, ForeignKey
#Table, Column, Integer, String, ForeignKey - use these for more advanced SQL operations.

def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://asger:DontUseThisPassword@localhost:5432/oam-dk
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

def main():
    '''Example of establishing a connection and a simple SQL statement'''
    con, meta = connect('asger', 'DontUseThisPassword', 'oam-dk')

    stmt = 'SELECT doi, article_title FROM total_2015 where is_gold = true'
    result_proxy = con.execute(stmt)
    result = result_proxy.fetchall()
    print(result)

if __name__ == '__main__':
    main()
