# ==============================
# Sistema de Folha de Pagamento
# ==============================

# Função para autenticação do funcionário
def autenticar():
    matricula_cadastrada = "12345"
    senha_cadastrada = "senha123"

    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")

    if matricula == matricula_cadastrada and senha == senha_cadastrada:
        print("\nAcesso permitido!\n")
        return True
    else:
        print("\nMatrícula ou senha incorretas. Acesso negado.\n")
        return False

# Função para calcular o desconto do INSS
def calcular_inss(salario):
    if salario <= 1518.00:
        desconto = salario * 0.075
    elif salario <= 2793.88:
        desconto = salario * 0.09
    elif salario <= 4190.83:
        desconto = salario * 0.12
    elif salario <= 8157.41:
        desconto = salario * 0.14
    else:
        desconto = 951.62  # teto máximo
    return desconto

# Função para calcular o desconto do IRRF
def calcular_irrf(salario):
    if salario <= 2428.80:
        desconto = 0
    elif salario <= 2826.65:
        desconto = salario * 0.075
    elif salario <= 3751.05:
        desconto = salario * 0.15
    elif salario <= 4664.68:
        desconto = salario * 0.225
    else:
        desconto = salario * 0.275
    return desconto

# Função para calcular vale transporte
def calcular_vale_transporte(salario, deseja_vale):
    if deseja_vale.lower() == "s":
        return salario * 0.06
    else:
        return 0

# Função para calcular vale refeição
def calcular_vale_refeicao(valor_vr):
    return valor_vr * 0.20

# Função para calcular plano de saúde (R$150 por dependente)
def calcular_plano_saude(qtd_dependentes):
    return qtd_dependentes * 150.00

# Função principal
def folha_pagamento():
    if not autenticar():
        return

    salario_base = float(input("Informe o salário base (R$): "))
    deseja_vale = input("Deseja receber vale transporte (s/n)? ")
    valor_vr = float(input("Informe o valor do vale refeição fornecido pela empresa (R$): "))
    dependentes = int(input("Informe a quantidade de dependentes: "))

    # Cálculos
    desconto_inss = calcular_inss(salario_base)
    desconto_irrf = calcular_irrf(salario_base)
    desconto_vale_transporte = calcular_vale_transporte(salario_base, deseja_vale)
    desconto_vale_refeicao = calcular_vale_refeicao(valor_vr)
    desconto_plano_saude = calcular_plano_saude(dependentes)

    total_descontos = (desconto_inss + desconto_irrf +
                       desconto_vale_transporte + desconto_vale_refeicao +
                       desconto_plano_saude)

    salario_liquido = salario_base - total_descontos

    # Resultado
    print("\n===== RESUMO DA FOLHA DE PAGAMENTO =====")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"INSS: -R$ {desconto_inss:.2f}")
    print(f"IRRF: -R$ {desconto_irrf:.2f}")
    print(f"Vale Transporte: -R$ {desconto_vale_transporte:.2f}")
    print(f"Vale Refeição (20%): -R$ {desconto_vale_refeicao:.2f}")
    print(f"Plano de Saúde ({dependentes} dependente(s)): -R$ {desconto_plano_saude:.2f}")
    print("-----------------------------------------")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")
    print("=========================================")

# Executar o programa
folha_pagamento()