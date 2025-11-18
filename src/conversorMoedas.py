resposta = "s"  

while resposta == "s":
    moeda = input("Real ou Dólar? ").upper()  
    
    if moeda == "REAL":  
        valor = float(input("Digite o valor: R$"))
        conversao = valor / 5.33  
        print(f"Valor convertido em dólar = US$ {conversao:.2f}")
    elif moeda == "DOLAR": 
        valor = float(input("Digite o valor: US$"))
        conversao = valor * 5.33  
        print(f"Valor convertido em real = R$ {conversao:.2f}")
    else: 
        print("Opção inválida. Por favor, digite 'Real' ou 'Dólar'.")

    resposta = input("Você quer continuar? [S/N] ").upper()

print("Programa encerrado!")