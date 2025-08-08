import cx_Oracle

class OracleConnection:
    def __init__(self):
        self.host = "10.151.1.75"
        self.port = "1521"
        self.service = "bmatraffice"
        self.username = "SYS"
        self.password = "welcome1"
        # self.host = "db"
        # self.port = "1521"
        # self.service = "XE"
        # self.username = "sys"
        # self.password = "12345678"
    

    def get_connection(self):
        dns_tns = cx_Oracle.makedsn(
            self.host, 
            self.port, 
            service_name=self.service
        )

        connection = cx_Oracle.connect(
            self.username,
            self.password,
            dns_tns,
            mode=cx_Oracle.SYSDBA
        )

        return connection