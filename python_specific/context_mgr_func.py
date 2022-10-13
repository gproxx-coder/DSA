import psycopg2
from contextlib import contextmanager

@contextmanager
def connect(dbname, user, password, host, port):
    connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    try:
        yield connection
    except Exception as e:
        print(e)
    finally:
        # Close the connection
        connection.close()


with connect(dbname='OwnershipData', user='admin', password='pwd', host='127.0.0.1', port='5432') as cur:
    res = cur.execute("select * from dba.first_ownership limit 100")
    print(res.fetchall())


