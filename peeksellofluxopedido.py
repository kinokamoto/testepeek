
import random
import time
from splinter.browser import Browser

#Definir variáveis
URL = "https://peeksello.review/" #Define o site que deve acessar
EMAIL = 'testedigitaldesk@outlook.com' #Define o email que deve digitar
SENHA = 'Teste1234' #Define a senha que deve digitar
OBSERVACAO = 'Teste automatizado Peeksello.'
SLEEP = 4 #Tempo determinado para aguardar antes de executar a próxima linha
COLECAO = 2 #Seleciona coleção específica
CATEGORIA = 'Camiseta' #Seleciona categoria específica
QTD = 5 #Incrementar quantidade - definir valor
#PESQUISACLIENTE = 'Lucy' #Digita nome de cliente específico (no mínimo 3 caracteres)
#EMAIL = 'cliente2t@outlook.com'
#SENHA = 'Peeksello1234'

#Realizar login com conta login e senha
B = Browser('firefox', capabilities={'acceptSslCerts': True})
B.visit(URL) #Visita a url
time.sleep(SLEEP)
B.find_by_css('a.btn-sign-in').last.click() #Clicar em Outra Conta
time.sleep(SLEEP)
B.find_by_css('.form-group .form-control').click() #Clicar no campo Login
B.find_by_css('.form-group .form-control').type(EMAIL) #Digita o email definido
#na variável
time.sleep(SLEEP)
B.find_by_css('.form-group .form-control').last.click() #Clicar no campo Senha
time.sleep(SLEEP)
B.find_by_css('.form-group .form-control').last.type(SENHA) #Digita a senha definida
#na variável
time.sleep(SLEEP)
B.find_by_css('input.btn.btn-primary').click() #Clica em login

"""#Realizar login com conta Google
B = Browser('firefox', capabilities={'acceptSslCerts': True})
B.visit(URL) #Visita a url
time.sleep(SLEEP)
B.find_link_by_href('/Login/LogarComGoogle').click() #Clica no botão "Fazer login com Chrome"
time.sleep(SLEEP)
B.find_by_name('identifier') #Encontra o campo do email
time.sleep(SLEEP)
B.fill('identifier', EMAIL)  #Preence o campo de email
time.sleep(SLEEP)
B.find_by_css('span.RveJvd.snByac').first.click() #Clica em próximo
time.sleep(SLEEP)
B.find_by_name('password') #Encontra o campo da senha
time.sleep(SLEEP)
B.fill('password', SENHA) #Preenche o campo senha
time.sleep(SLEEP)
B.find_by_css('span.RveJvd.snByac').first.click() #Clica em login"""

"""#Selecionar uma empresa específica de uma lista, através do URL
time.sleep(SLEEP)
B.find_link_by_href('https://peeksello.peeksello.review').click()"""

"""Caso haja somente uma empresa vinculada ao usuário,
já é logado automaticamente nela."""

#Selecionar a empresa de forma aleatória
time.sleep(SLEEP)
EMPRESA = B.find_by_css('div.container a') #Procura a tag A das empresas
ALEATORIO_EMPRESA = EMPRESA[random.randint(1, len(EMPRESA)-1)].click() #Seleciona uma dessas tags
#que encaminhará para a empresa escolhida
#SELETOR_EMPRESA = B.find_by_css('div.wrapper-selecao-empresa a')

"""#Selecionar coleção pré-determinada
time.sleep(SLEEP)
B.find_by_css('a.btn-box.btn-access')[COLECAO].click()"""

#Selecionar uma coleção aleatória
time.sleep(SLEEP)
SELETOR_COLECAO = B.find_by_css('a.btn-box.btn-access') #Procura pelos ícones
ALEATORIO_COLECOES = SELETOR_COLECAO[random.randint(0, len(SELETOR_COLECAO)-1)].click() #Seleciona um dos ícones
time.sleep(SLEEP)

#Adicionar mais de um produto ao carrinho
VARPEDIDOS = 0
while VARPEDIDOS < 3:
    #Abrir menu
    time.sleep(SLEEP)
    B.find_by_css('span.display-menu').first.click()

    #Selecionar uma categoria aleatória
    time.sleep(SLEEP)
    SELETOR_CATEGORIAS = B.find_by_css('ul.categorias-list>li')
    CATEGORIAS = SELETOR_CATEGORIAS[random.randint(2, len(SELETOR_CATEGORIAS)-3)]
    #Ignora as 2 primeiras e 2 ultimas coisas das categorias
    SELETOR_CATEGORIA = CATEGORIAS.find_by_css('ul')
    CATEGORIA = SELETOR_CATEGORIA[random.randint(0, len(SELETOR_CATEGORIA)-1)]
    #print 'Categoria: ' + CATEGORIA.text
    CATEGORIA.find_by_css('a').first.click()

    """#Selecionar categoria determinada
    time.sleep(SLEEP)
    B.find_by_text(CATEGORIA).click()"""

    #Selecionar um produto aleatório - acessá-lo
    time.sleep(SLEEP)
    SELETOR_PRODUTOS = B.find_by_css('a.detail-area') #Seleciona a área da imagem para
    #que acesse (entre) no produto
    PRODUTOS = SELETOR_PRODUTOS[random.randint(0, len(SELETOR_PRODUTOS)-1)].click()

    """#Selecionar um produto aleatório - marcar o botão
    time.sleep(SLEEP)
    SELETOR_PRODUTOS = B.find_by_css('div.galeria-celula i') #Seleciona o produto pelo botão
    PRODUTOS = SELETOR_PRODUTOS[random.randint(0,len(SELETOR_PRODUTOS)-1)].click()"""

    #Abrir modal da quantidade
    time.sleep(SLEEP)
    B.find_by_css('div.info a').click()
    time.sleep(SLEEP)

    #Acrescentar quantidade de produtos, enquanto i for menor que QTD
    i = 0
    while i < QTD:
        SELETOR_TAMANHOS = B.find_by_css('.modal-body .item.active .input-group')
        QUANTIDADE_TAMANHOS = len(SELETOR_TAMANHOS)
        if QUANTIDADE_TAMANHOS == 1:
            TAMANHO = B.find_by_css('.modal-body .item.active .input-group a')[1].click()
        else:
            TAMANHO = SELETOR_TAMANHOS[random.randint(0, QUANTIDADE_TAMANHOS-1)] #Seleciona tamanho
            TAMANHO.find_by_css('a')[1].click() #Clica na tag A que adiciona itens
        time.sleep(SLEEP)
        i = i + 1
    B.find_by_css('div.modal-footer').click()
    B.find_by_css('button.btn.btn-primary').click()
    VARPEDIDOS = VARPEDIDOS + 1

#Selecionar o carrinho
time.sleep(SLEEP)
B.find_by_tag('span.badge.badge-primary').click()
#B.find_by_css('i.glyphicon.glyphicon-shopping-cart').click()

"""Caso queira acrescentar as quantidades depois de selecionar todos os produtos...
#Selecionar modal dos tamanhos
time.sleep(SLEEP)
B.find_by_css('i.glyphicon.glyphicon-edit').click()

#Selecionar quantidade
i = 0
while i < QTD:
    SELETOR_TAMANHOS = B.find_by_css('.modal-body .item.active .input-group')
    QUANTIDADE_TAMANHOS = len(SELETOR_TAMANHOS)
    if QUANTIDADE_TAMANHOS == 1:
        TAMANHO = SELETOR_TAMANHOS.first
    else:
        TAMANHO = SELETOR_TAMANHOS[random.randint(0, QUANTIDADE_TAMANHOS-1)] #seleciona tamanho
        TAMANHO.find_by_css('a')[1].click() #clica na tag A que adiciona itens
    time.sleep(SLEEP)
    i = i + 1

#Fechar a modal de quantidade
time.sleep(SLEEP)
B.find_by_css('button.btn.btn-primary').click()"""

#Abrir modal de seleção de cliente
time.sleep(SLEEP)
B.find_by_id('input-lojista').click()

"""#Buscar por um cliente específico
time.sleep(SLEEP)
B.find_by_id('inputModalLojistas').type(PESQUISACLIENTE)"""

#Buscar por um cliente aleatório
time.sleep(SLEEP)
CLIENTE1 = 'Cliente1T'
CLIENTE2 = 'Cliente2T'
CLIENTE3 = 'Cliente3T'
CLIENTES = [CLIENTE1, CLIENTE2, CLIENTE3]
CLIENTE = random.choice(CLIENTES)
B.find_by_id('inputModalLojistas').type(CLIENTE)
#print CLIENTE

#Selecionar o cliente que foi buscado
time.sleep(SLEEP)
B.find_by_css('div.list-group a').click()

#Observação do pedido
time.sleep(SLEEP)
B.find_by_css('textarea.form-control.scrollPage').type(OBSERVACAO)
#Digita a observação definida na variável incial.
#B.find_by_css('textarea.form-control.scrollPage').click() #Clica na observação.

#Solicitar o pedido
time.sleep(SLEEP)
B.find_by_css('a.btn.btn-primary.btn-lg.btn-validar-pedido').click()
#Clica no botão Solicitar Pedido

#Selecionar condição de pagamento
time.sleep(SLEEP)
SELETOR_PAGAMENTO = B.find_by_css('div.modal-body div.panel-heading')
FORMA_PAGAMENTO = SELETOR_PAGAMENTO[random.randint(0, len(SELETOR_PAGAMENTO)-1)]
FORMA_PAGAMENTO.find_by_css('h4 a').first.click()
time.sleep(SLEEP)
SELETOR_CONDICAO = B.find_by_css('label.item-pay input')
CONDICAO = SELETOR_CONDICAO[random.randint(0, len(SELETOR_CONDICAO)-1)].click()

"""DIV_PARCELAS = B.find_by_id('collapse' + FORMA_PAGAMENTO["id"]).first
PARCELAS = DIV_PARCELAS.find_by_css('a').click()
PARCELAS[random.randint(0, len(PARCELAS)-1)].click()
FORMA_PAGAMENTO.find_by_css('input').first.click()"""

#Solicitar o pedido
time.sleep(SLEEP)
B.find_by_id('modal-condicoes-pagamento').first.find_by_css('div.modal-footer button').first.click()
#Clica em Solicitar Pedido

#Fechar o navegador
time.sleep(15)
B.quit()