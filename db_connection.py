import pyodbc

def obtener_conexion():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=sv_name;'
        'DATABASE=db_name;'
        'Trusted_Connection=yes;'
        'TrustServerCertificate=yes;'
    )
