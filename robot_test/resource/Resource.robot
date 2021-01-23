*** Settings ***
Library                                 SeleniumLibrary


*** Variables ***
${URL}                                  https://developer.clashroyale.com/
${BROWSER}                              gc

${BTN_LOGIN_HOME}                       css=#content > div > div.drawer-main-container > div > header > div > div > div:nth-child(3) > div > a:nth-child(3)

# ${BTN_LOGIN}                            css=#content > div > div.drawer-main-container > div > div > div > div > div > div > form > div.form-group.text-right > button

# ${SPAN_ACESS}                           css=#content > div > div.drawer-main-container > div > div > div > div > div > h2 > span:nth-child(1)

*** Keywords ***
Abrir navegador
    Open Browser                        ${URL}  ${BROWSER}

Fechar navegador
    Close Browser

Verificar se esta na pagina home do site
    Title Should Be                     Clash Royale API


Clicar no botao login da pagina home 
    Click Element                       xpath=//*[@id="content"]/div/div[2]/div/header/div/div/div[3]/div/a[2]


#    Click Element                       ${BTN_LOGIN_HOME}
# Inserir "${EMAIL}" no campo Email

#     Input Text                          id=email

# Inserir "${PASSWORD}" no campo Password
#     Input Text                          id=password

# Clicar no botao de Login 
#     Click Element                       ${BTN_LOGIN}

# Verificar se o acesso deu certo, aparecendo a frase "${ENTER_THE_ARENA}"
#     Wait Until Element Is Visible       ${SPAN_ACESS}



#1.Acessar o website https://developer.clashroyale.com/
# 2.Clicar no botão login 
# 3.Inserir usuário e senha (O cadastro não precisa ser feito pela automação, pode realizá-lo manualmente) 
# 4.Clicar em login 

# 5 -Ir até o menu minha conta 
# 6.Criar uma nova chave