

salario_atual = float(input("Digite o salário atual: R$"))

def calc_reajuste(salario_atual):
    if salario_atual <= 280.00:
        aumento_salario = 20
    elif salario_atual <= 700.00:
        aumento_salario = 15
    elif salario_atual <= 1500.00:
        aumento_salario = 10
    else:
        aumento_salario = 5

    aumento = (aumento_salario / 100) * salario_atual
    salario_novo = aumento + salario_atual

    return salario_atual, aumento, salario_novo, aumento_salario

salario_antigo, valor_aumento ,salario_novo , percentual_aumento = calc_reajuste(salario_atual)

print("O salário antes do reajuste é ", salario_antigo)
print("O percentual de aumento aplicado foi de: ", percentual_aumento, "%")
print("O valor do aumento foi de: ", valor_aumento)
print("O novo salário é de: ", salario_novo)

#--------------------------------------------------------------------------------------
dia = int(input("Digite um número da semana: "))

def dias_sem(dia):
    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Segunda")
    elif dia == 3:
        print("Terça")
    elif dia == 4:
        print("Quarta")
    elif dia == 5:
        print("Quinta")
    elif dia == 6:
        print("Sexta")
    elif dia == 7:
        print("Sábado")
    else:
        print("Não existe")
 
dias_sem(dia)

#-----------------------------------------------------------------------------------------------

a = float(input(" valor de a: "))
b = float(input(" valor de b: "))
c = float(input(" valor de c: "))

delta = (b ** 2 - 4 * a * c)

def func_segGrau(a, delta):
    if a == 0:
        print("A equação não é de segundo grau, o programa está sendo encerrado.")
    elif delta == 0:
        print("A equação possuí apenas uma raiz.")
    elif delta > 0:
        print("A equação possuí duas raizes.")
    else:
        print("A equação não possuí raízes, o programa está sendo encerrado.")

func_segGrau(a, delta)