*** Settings ***
Library                                 SeleniumLibrary


*** Variables ***
${URL}                                  https://developer.clashroyale.com/
${BROWSER}                              firefox

${ELEMENT}

${BTN_LOGIN}                            xpath=/html/body/div[2]/div/div[2]/div/div/div/div/div/div/form/div[4]/button/span[1]

${SPAN_ACESS}                           xpath=/html/body/div[2]/div/div[2]/div/div/div/div/div/h2/span[1]

${BTN_CREATE_KEY}                       xpath=html.sccc-lang-en.sccc-dir-ltr body div#content div.drawer-container div.drawer-main-container div.drawer-main div.new-api-key-page.page.theme--bicolor section div.container div.row div.col-xs-light.col-xs-12.col-sm-6.col-md-5.col-md-offset-2 form div.form-group.text-right button.ladda-button.btn.btn-primary.btn-lg.btn-block span.ladda-label

*** Keywords ***
Abrir navegador
    Open Browser                        ${URL}  ${BROWSER}

Fechar navegador
    Close Browser

Verificar se esta na pagina home do site
    Wait Until Element Is Visible       css=.footer__brand > a:nth-child(1) > img
    # Title Should Be                     Clash Royale API

    # Sleep                               1

Clicar no botao login da pagina home 
    Click Link                          css=.login-menu > a:nth-child(3)


Inserir "${EMAIL}" no campo Email
    Input Text                          id=email            ${EMAIL}

Inserir "${PASSWORD}" no campo Password
    Input Text                          id=password         ${PASSWORD}

Clicar no botao de Login 
    Click Element                       ${BTN_LOGIN}

Verificar se o acesso deu certo, aparecendo a frase "${ENTER_THE_ARENA}"
    Wait Until Element Is Visible       ${SPAN_ACESS}

Ir ate My Account dentro do menu bar 
    Click Element                       css=.dropdown-toggle__text

    Click Element                       css=.dropdown-menu > li:nth-child(1) > a:nth-child(1)

Clicar em Create New Key para abrir o formulario
    Click Element                       css=.create-key-btn > span:nth-child(2)


# Abrir um novo navegador para descobrir qual e o IP, Capturar e Fechar a Pagina
#     Open Browser                        https://www.expressvpn.com/pt/what-is-my-ip   ${BROWSER}

#     Wait Until Element Is Visible       css=.col-left > div:nth-child(1) > h6

#     Get Text                            css=.col-left > div:nth-child(1) > h4

#     Close Browser

Dentro do formulario: Create a Key adicionar "${KEY_NAME}" em Key Name; Em Description "${DESCRIPTION}"; E em IP "${IP}"
    Input Text                          id=name           ${KEY_NAME}
    Input Text                          id=description    ${DESCRIPTION}
    Input Text                          id=range-0        ${IP}

    Double Click Element                css=.ladda-button


Verificar se a Key foi criada com sucesso
    Wait Until Element Is Visible       css=.col-xs-dark > h2

