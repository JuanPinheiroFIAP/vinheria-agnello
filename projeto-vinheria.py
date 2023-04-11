print("Sejá Bem vindo so nosso site!")
print("Olá vamos efetuar seu cadastro no nosso site")
nome = input("Me informe seu nome completo: ")
idade = int(input("Me informe sua idade: "))
endereço_cliente = input("Me informe seu endereço: ")
endereço_entrega = input("Me informe seu endereço entrega: ")

if idade >= 18:
    catalogo_vinhos = print("Vinho Tinto:80.00,/n Vinho Branco: 70.00,Vinho Rosé: 60.00,Vinho Verde: 50.00, Espumante: 90.00")
else:
    print("Sinto muito mas o comprador tem que ser maior de idade.")
    print("Até mais!")