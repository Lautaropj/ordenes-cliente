import pyodbc

def obtener_conexion():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=DESKTOP-8Q6TMUB\\ZOO2021;'
        'DATABASE=DRAGONFISH_ALCORTA;'
        'Trusted_Connection=yes;'
        'TrustServerCertificate=yes;'
    )
