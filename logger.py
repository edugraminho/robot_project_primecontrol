import logging
from custom_library.main import search_clan


logging.basicConfig(filename="logger_info.log", level=logging.INFO)

logging.info('''
    Caso de Teste: Acessar o site, logar e criar uma nova chave
    Abrir navegador
    Verificar se esta na pagina home do site
    Clicar no botao login da pagina home 
    Inserir "email" no campo Email
    Inserir "senha" no campo Password
    Clicar no botao de Login 
    Verificar se o acesso deu certo, aparecendo a frase "Enter the Arena with"
    Ir ate My Account dentro do menu bar 
    Clicar em Create New Key para abrir o formulario
    # Abrir um novo navegador para descobrir qual e o IP, Capturar e Fechar a Pagina
    Dentro do formulario: Create a Key adicionar "New Key" em Key Name; Em Description "Adding a key for testing the Prime Control"; E em IP "177.96.15.103"
    Verificar se a Key foi criada com sucesso
    Fechar navegador

''')


log_format = '%(asctime)s:%(levelname)s:%(filename)s:'


logging.basicConfig(filename="logger_info.log",
                    filemode='w',
                    level=logging.INFO, 
                    format=log_format)


logger = logging.getLogger('root')

logger.info(f'''
    A funcao search_clan retorna o Clan The resistance: {search_clan()}
    Com a Tag: {search_clan()[0]['tag']}
''')
