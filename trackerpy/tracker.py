from .db_connector import get_db_connection
from datetime import datetime

class TrackerPy:
    def __init__(self, script_id: int, script_name: str, source_name: str, process_step: str):
        """
        Inicializa uma nova instância da classe TrackerPy

        Esta classe é responsável por rastrear e registrar informações sobre a execução de scripts,
        incluindo identificadores de script, nome de script e fonte de origem.

        #### Args:
            - script_id (int): Um identificador único para o script que está sendo monitorado.
            - script_name (str): O nome do script que está sendo monitorado.
            - source_name (str): O nome da fonte de origem onde os logs ou informações estão sendo gerados.
            - process_step (str): O nome da etapa em que o script se encontra (Ex: API, DATABASE, PROCESSING).
        
        #### Attributes:
            - script_id (int): Armazena o identificador único do script.
            - script_name (str): Armazena o nome do script.
            - source_name (str): Armazena o nome da fonte ou sistema.      
            - process_step (str): Armazena o nome da etapa do script.  
        """
        self.script_id = script_id
        self.script_name = script_name
        self.source_name = source_name
        self.process_step = process_step
 
    def log(self, status:str, message=None, output=None):
        """
        Registra um log no banco de dados com informações detalhadas sobre a execução de um processo.

        Este método insere um registro na tabela de logs do banco de dados, capturando o passo do processo,
        o status da execução, uma mensagem opcional e qualquer output relevante.

        Args:
            status (str): O status da execução, como 'INFO', 'SUCCESS', ou 'ERROR'.
            message (str, optional): Uma mensagem opcional que descreve detalhes adicionais do processo.
            output (str, optional): Dados ou resultados opcionais gerados durante o processo.

        Returns:
            None
        """
        timestamp = datetime.now()
        query = """
        INSERT INTO Log_Tracker_Py (script_id, script_name, source_name, process_step, timestamp, status, message, output)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        values = (self.script_id, self.script_name, self.source_name, self.process_step, timestamp, status, message, output)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def log_info(self, message=None, output=None):
        """
        Registra um log informativo no banco de dados.

        Este método é uma conveniência para registrar logs com o status 'INFO', 
        geralmente usado para indicar que um processo foi iniciado ou que informações adicionais estão disponíveis.

        Args:
            message (str, optional): Uma mensagem opcional que descreve detalhes adicionais do processo.
            output (str, optional): Dados ou resultados opcionais gerados durante o processo.

        Returns:
            None
        """
        self.log('INFO', message, output)

    def log_success(self, message=None, output=None):
        """
        Registra um log de sucesso no banco de dados.

        Este método é uma conveniência para registrar logs com o status 'SUCCESS', 
        geralmente usado para indicar que um processo foi concluído com êxito.

        Args:
            message (str, optional): Uma mensagem opcional que descreve detalhes adicionais do processo.
            output (str, optional): Dados ou resultados opcionais gerados durante o processo.

        Returns:
            None
        """
        self.log('SUCCESS', message, output)

    def log_error(self, message=None, output=None):
        """
        Registra um log de erro no banco de dados.

        Este método é uma conveniência para registrar logs com o status 'ERROR', 
        geralmente usado para indicar que um processo encontrou um problema ou falha.

        Args:
            message (str, optional): Uma mensagem opcional que descreve detalhes adicionais do erro.
            output (str, optional): Dados ou resultados opcionais gerados durante o processo.

        Returns:
            None
        """
        self.log('ERROR', message, output)