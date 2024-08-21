import pyodbc
from .config import DB_CONFIG

def get_db_connection():
    """
    Estabelece uma conexão com o banco de dados SQL Server.

    Esta função cria uma string de conexão utilizando as configurações fornecidas em `DB_CONFIG` e 
    estabelece uma conexão com o banco de dados SQL Server através do `pyodbc`.

    Returns:
        pyodbc.Connection: Um objeto de conexão do `pyodbc` que pode ser usado para executar consultas no banco de dados.

    Raises:
        pyodbc.Error: Se houver um problema ao tentar estabelecer a conexão, uma exceção do tipo `pyodbc.Error` será lançada.

    Example:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM my_table")
    """
    conn_str = (
        f"DRIVER={DB_CONFIG['driver']};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"UID={DB_CONFIG['uid']};"
        f"PWD={DB_CONFIG['pwd']}"
    )
    return pyodbc.connect(conn_str)