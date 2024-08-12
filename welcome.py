idade = 16
nome = "Eduardo"

print("Meu nome é " + nome, "e tenho " + str(idade) , "anos de idade")
name_user= input("Insira o nome do usuário:")
print("Nome do usuário é:" + name_user)
idade_user= input("Insira a idade do usuário:")
print("Idade do usuário:" + idade_user)


n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2 if n2 != 0 else "Infinito"
# Exibindo os resultados
print(f"A soma dos números é: {soma}, a subtração dos números é: {sub}, o produto dos números é: {mult}, a razão dos números é: {div}")

idade = int(input("Digite sua idade"))
if idade > 18 :
    print("Você é maior de idade")
else :
    print("Você é menor de idade")

lista_numeros = range(1000)
for num in lista_numeros:
    print(num)

