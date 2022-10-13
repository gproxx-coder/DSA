import psycopg2


class Connect:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password,
                                               host=self.host, port=self.port)
        except Exception as e:
            print(e)
        else:
            return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"rolling back due to ex {exc_val}")
        if self.connection:
            self.connection.close()


with Connect(dbname='OwnershipData', user='admin', password='pwd', host='127.0.0.1', port='5432') as cur:
    res = cur.execute("select * from dba.first_ownership limit 100")
    print(res.fetchall())
