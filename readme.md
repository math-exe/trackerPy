# TrackerPy

O **TrackerPy** é uma poderosa ferramenta de logging para scripts Python, projetada para facilitar o monitoramento e o rastreamento de processos em execução.

### Dependências
```bash
pip install -r requirements.txt
```

### Instalação

Para instalar o TrackerPy, siga os passos abaixo:

1. Navegue até o diretório principal onde você baixou os arquivos deste repositório. Seu caminho deve ser semelhante a:
    ```bash
    C:\Users\seu_usuario\trackerpy
    ```

2. Com o terminal aberto nesse diretório, execute o seguinte comando para instalar o TrackerPy: 
    ```bash
    pip install trackerpy
    ```
Após a instalação, você estará pronto para integrar o TrackerPy aos seus scripts Python, aproveitando suas funcionalidades para melhorar o controle e a rastreabilidade das suas operações.

### Como usar
**Passo 1:** Conexão com o banco de dados.

Primeiro, você precisa configurar o arquivo config.py, substitua o valor das variáveis com base nas suas credenciais e informações do banco de dados.
```bash
C:\Users\seu_usuario\trackerpy\config.py
```

**Passo 2:** Configuração da instância.

Após configurar config.py, você precisa inicializar uma instância da classe TrackerPy em seu script. A inicialização requer que você forneça alguns parâmetros, como o ID do script, o nome do script, a fonte do log e a etapa do processo.

```python
from trackerpy import TrackerPy

# Inicialize o TrackerPy
tracker = TrackerPy(script_id=1, script_name="Nome do Script", source_name="Fonte de Dados", process_step="PROCESSING")

```

**Passo 3:** Registro de Logs.
Com a instância do TrackerPy inicializada, você pode registrar diferentes tipos de logs ao longo do seu script. O TrackerPy fornece três métodos principais para registrar logs:

    1. log_info(): Para registrar informações gerais.
    2. log_success(): Para registrar o sucesso de um processo.
    3. log_error(): Para registrar erros que ocorreram durante a execução do script.

Aqui está um exemplo de como usar cada um desses métodos:
```python
# Registrar uma informação
tracker.log_info(message="O processo foi iniciado.")

# Registrar um sucesso
tracker.log_success(message="O processo foi concluído com sucesso.")

# Registrar um erro
try:
    # Código que pode gerar um erro
    result = 10 / 0
except Exception as e:
    tracker.log_error(message="Ocorreu um erro durante a execução do processo.", output=str(e))
```