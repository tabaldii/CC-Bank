def fazbarra():
    print("=" * 50)


def pausa():
    from time import sleep
    sleep(1)


class  infocliente:          #Guardar informações do cliente
    primeiro_nome = ""
    ultimo_nome = ""
    CPF = 0
    senha = 0
    cartao = 0
    credito = 0
    compras = ""
    renda = 0


class comprascliente:       #Guardar as compras do cliente
    cartaocompra = 0
    data = ""
    categoria = ""
    loja = ""
    valor = 0


def cpf_validate(numbers):      #validar CPF
    cpf = [int(char) for char in numbers if char.isdigit()]
    if len(cpf) != 11:
        return False
    if cpf == cpf[::-1]:
        return False
    for i in range(9, 11):
        valor = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digito = ((valor * 10) % 11) % 10
        if digito != cpf[i]:
            return False
    return True


infoadmin = ["anderson", 309309] #informações para login do administrador

fazbarra()
print("             BEM-VIND0(A) AO CCBANK!")
fazbarra()
pausa()
print()
print("INSIRA O CÓDIGO DA AÇÃO QUE DESEJA REALIZAR:")
pausa()
listaclientes = []
listacompras = []
identificar = 0
while identificar != 6:
    print(f"{'CÓDIGO':^10}{'      FUNÇÃO'}")
    print(f"{'1 -':>7}{'         ABRIR NOVA CONTA'}")
    print(f"{'2 -':>7}{'         REALIZAR COMPRA'}")
    print(f"{'3 -':>7}{'         EXTRATO CLIENTE'}")
    print(f"{'4 -':>7}{'         PAGAMENTO/FATURA'}")
    print(f"{'5 -':>7}{'         VIZUALIZAR LISTA DE CLIENTES'}")
    print(f"{'6 -':>7}{'         SAIR'}")
    identificar = int(input("DIGITE O CÓDIGO: "))
    if identificar == 1:
        fazbarra()
        print("PARA ADICIONAR UMA NOVA CONTA PRECISAMOS QUE\nVOCÊ FORNEÇA SUAS INFORMAÇÕES DE ADMINISTRADOR: ")
        while True:
            username = str(input("     USERNAME: "))        #informações para logar como admin
            senhaadmin = int(input("     SENHA: "))
            if username != infoadmin[0] or senhaadmin != infoadmin[1]:
                print("AS INFORMAÇÕES ESTÃO INCORRETAS! TENTE NOVAMENTE! ")
            else:
                break
        print("     FAZENDO LOGIN...")
        pausa()
        pausa()
        print("     LOGADO COM SUCESSO!")
        fazbarra()
        print("VAMOS PRECISAR DAS SEGUINTES INFORMAÇÕES SUAS: ")

        dados = infocliente()
        dados.primeiro_nome = str(input("   PRIMEIRO NOME: "))
        dados.ultimo_nome = str(input("   ÚLTIMO NOME: "))
        while True:
            dados.CPF = str(input("   DIGITE SEU CPF: "))
            if cpf_validate(dados.CPF):
                print("   CPF VÁLIDO!")
                break
            else:
                print("   CPF INVÁLIDO! POR FAVOR DIGITE UM CPF VÁLIDO.")
        fazbarra()
        print("ESTAMOS GERANDO O NÚMERO DO SEU CARTÃO...")
        pausa()
        while True:
            import random
            numerocar = random.randint(1000000000000, 10000000000000)
            if numerocar not in listaclientes:
                dados.cartao = numerocar
                break
        print(f"O NÚMERO DO SEU CARTÃO É:{numerocar} ")
        fazbarra()
        while True:
            senhacliente = input("CRIE UMA SENHA DE 6 DÍGITOS: ")
            novasenha = str(senhacliente)
            if len(novasenha) > 6 or len(novasenha) < 6:
                print("ESSA SENHA NÃO É ACEITA! TENTE NOVAMENTE!")
            else:
                break
        while True:
            confirmasenha = input("REPITA A SENHA PARA CONFIRMAR: ")
            if confirmasenha != senhacliente:
                print("A SENHA DIGITADA É DIFERENTE! TENTE NOVAMENTE!")
            else:
                break
        dados.senha = senhacliente
        fazbarra()
        print("PARA DISPONIBILIZAR UM CRÉDITO JUSTO QUEREMOS SABER QUAL É SUA RENDA MENSAL:")
        while True:
            print(f"{'CÓDIGO':^10}{'      RENDA'}")     #escolher uma renda
            print(f"{'1 -':>7}{'         INFERIOR À 1 (UM) SALÁRIO MÍNIMO'}")
            print(f"{'2 -':>7}{'         ENTRE 1(UM) E 2(DOIS) SALÁRIOS MÍNIMOS'}")
            print(f"{'3 -':>7}{'         ACIMA DE 2 SALÁRIOS MÍNIMOS'}")
            irenda = int(input("INSIRA O CÓDIGO: "))
            if 0 < irenda < 4:
                break
            else:
                print("NÚMERO INVÁLIDO")
        if irenda == 1:
            dados.credito = 500
            dados.renda = 1
        elif irenda == 2:
            dados.credito = 1000
            dados.renda = 2
        elif irenda == 3:
            dados.credito = 1500
            dados.renda = 3
        fazbarra()
        print(f"O SEU LIMITE DE CRÉDITO É DE R$ {dados.credito},00")
        fazbarra()
        print("CONTA FINALIZADA! AGRADECEMOS A PREFERÊNCIA!!!")
        fazbarra()
        listaclientes.append(dados)
        print()
    fazbarra()
    if identificar == 2:
        print("PARA FAZER COMPRAS LOGUE COM O NÚMERO DO SEU CARTÃO E SENHA: ")
        fazbarra()
        logar = int(input("NÚMERO DO CARTÃO: "))
        logarsenha = input("DIGITE SUA SENHA: ")
        print("SE O PROGRAMA FECHAR = DADOS NÃO RECONHECIDOS!")
        fazbarra()
        while True:
            for c in listaclientes:
                if logarsenha == c.senha and logar == c.cartao:
                    compra = comprascliente()
                    compra.cartaocompra = logar
                    compra.valor = float(input("QUAL É O VALOR DA COMPRA? "))
                    if compra.valor <= c.credito:
                        c.credito = c.credito - compra.valor
                        compra.data = input("QUAL É A DATA DA COMPRA (USE '/')? ")
                        print("AS CATEGORIAS SÃO:")
                        print("VIAGEM / FARMÁCIA / SUPERMERCADO / VESTIMENTAS / CARRO / OUTROS")
                        compra.categoria = str(input("ESCREVA A CATEGORIA: "))
                        compra.loja = str(input("NOME DA LOJA: "))
                        print("COMPRA FINALIZADA!!!")
                        print(f"SEU LIMITE AGORA É DE R${c.credito}!")
                        listacompras.append(compra)
                        fazbarra()
                        print()
                        break
                    else:
                        print("NÃO É POSSÍVEL REALIZAR A COMPRA!")
                        fazbarra()
            break
    if identificar == 3:
        print("PARA VER O EXTRATO LOGUE COM O NÚMERO DO SEU CARTÃO E SENHA: ")
        fazbarra()
        logarcompra = int(input("NÚMERO DO CARTÃO: "))
        print("SE O PROGRAMA FECHAR = NÚMERO NÃO RECONHECIDO!")
        fazbarra()
        for c in listacompras:
            if logarcompra == c.cartaocompra:
                print(f"VALOR DA COMPRA: R${c.valor}")
                print(f"DATA DA COMPRA: {c.data}")
                print(f"CATEGORIA DA COMPRA: {c.categoria}")
                print(f"NOME DA LOJA: {c.loja}")
                fazbarra()
    if identificar == 4:
        print("PARA FAZER PAGAMENTOS LOGUE COM O NÚMERO DO SEU CARTÃO E SENHA: ")
        fazbarra()
        logarpaga = int(input("NÚMERO DO CARTÃO: "))
        print("SE O PROGRAMA FECHAR = NÚMERO NÃO RECONHECIDO!")
        fazbarra()
        for c in listaclientes:
            if logarpaga == c.cartao:
                if c.renda == 1:
                    valorpagar = 500 - c.credito
                    print(f"O VALOR A SER PAGO É DE R$ {valorpagar}.")
                    pagamento = str(input("REALIZAR PAGAMENTO (SIM/NÃO)? ")).upper().strip()[0]
                    if pagamento == "S":
                        c.credito = 500
                        print("PAGAMENTO EFETUADO!")
                        print(f"SEU LIMITE AGORA É DE {c.credito},00")
                    else:
                        break
                elif c.renda == 2:
                    valorpagar = 1000 - c.credito
                    print(f"O VALOR A SER PAGO É DE R$ {valorpagar}.")
                    pagamento = str(input("REALIZAR PAGAMENTO (SIM/NÃO)? ")).upper().strip()[0]
                    if pagamento == "S":
                        c.credito = 1000
                        print("PAGAMENTO EFETUADO!")
                        print(f"SEU LIMITE AGORA É DE {c.credito},00")
                    else:
                        break
                elif c.renda == 3:
                    valorpagar = 1500 - c.credito
                    print(f"O VALOR A SER PAGO É DE R$ {valorpagar}.")
                    pagamento = str(input("REALIZAR PAGAMENTO (SIM/NÃO)? ")).upper().strip()[0]
                    if pagamento == "S":
                        c.credito = 1500
                        print("PAGAMENTO EFETUADO!")
                        print(f"SEU LIMITE AGORA É DE {c.credito},00")
                    else:
                        break
    if identificar == 5:
        if len(listaclientes) == 0:
            print("AINDA NÃO TEMOS CLIENTES!")
        else:
            print("LISTA DE NOMES DOS NOSSOS CLIENTES: ")
            fazbarra()
            for c in listaclientes:
                print(f"=> {c.primeiro_nome} {c.ultimo_nome}")
        fazbarra()
print("AGRADECEMOS A VISITA, VOLTE SEMPRE!!!")
