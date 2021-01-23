*** Settings ***
Resource                            ../resource/Resource.robot


*** Test Cases ***
Caso de Teste: Acessar o site, logar e criar uma nova chave
    Abrir navegador
    Verificar se esta na pagina home do site
    Clicar no botao login da pagina home 
    # Inserir "efgraminho@gmail.com" no campo Email
    # Inserir "bazinga2020" no campo Password
    # Verificar se o acesso deu certo, aparecendo a frase "Enter the Arena with"
    Fechar navegador
