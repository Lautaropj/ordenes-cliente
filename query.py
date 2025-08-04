import pandas as pd



def ordenes_cliente(conn, nombre):
    query = """
        SELECT
            EMAIL,
            FCLIENTE, 
            CASE 
                WHEN FCUIT IS NULL OR FCUIT = '' THEN '' 
                ELSE STUFF(STUFF(FCUIT, 3, 0, '-'), 12, 0, '-') 
            END AS Cuit,
            FFCH AS Fecha,
            CONCAT(FLETRA, ' ', FNUMCOMP) AS Factura,
            FTOTAL AS Total
        FROM [DRAGONFISH_ALCORTA].[ZooLogic].[COMPROBANTEV]
        WHERE 
            FCLIENTE LIKE ?
            AND UPPER(FCLIENTE) NOT IN ('CF','CONSUMIDOR FINAL','')
        ORDER BY
            FCLIENTE ASC,
            FFCH ASC
    """
    return pd.read_sql(query, conn, params=[f"%{nombre}%"])
