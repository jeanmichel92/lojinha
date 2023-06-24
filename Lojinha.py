print("Bem vindo a Loja do Jean Michel Bete") #Meu nome como identificador pessoal
valorProd = float (input("Entre com o valor do produto: ")) #inserção de dados em float, pois pode ser número quebrado
qntProd = int (input("Entre com o valor da quantidade: " )) #numero inteiro para quantidade
valorFinal = valorProd * qntProd

if qntProd <=9:
    valorFinal = valorProd #Como não tem desconto para essa quantidade, o valor final é o mesmo do inicial
elif 10 <= qntProd <= 99: #Entre 10 e 99 unidades, aplica-se 5% de desconto
    valorFinal = valorProd - valorProd * 0.05
elif 100 <= qntProd <= 999: #Entre 100 e 999 unidades, aplica-se 10% de desconto
    valorFinal = valorProd - valorProd * 0.1
else: #restou somente uma opção da tabela de desconto, posso utilizar o else, nesse caso ele da 15%
    valorFinal = valorProd - valorProd * 0.15

print("O valor unitário sem desconto foi: R${:.2f} ".format (valorProd))
print("O valor unitário com desconto foi: R${:.2f} ".format(valorFinal))
