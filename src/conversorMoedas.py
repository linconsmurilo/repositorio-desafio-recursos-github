TAXA_CAMBIO_DOLAR_REAL = 5.32

def dolar_para_real(valor_dolar):
    valor_real = valor_dolar * TAXA_CAMBIO_DOLAR_REAL
    return valor_real

def real_para_dolar(valor_real):
    valor_dolar = valor_real / TAXA_CAMBIO_DOLAR_REAL
    return valor_dolar

def main():
    print("--- Conversor de Moedas (Real/Dólar) ---")
    print(f"Cotação utilizada: 1 USD = R$ {TAXA_CAMBIO_DOLAR_REAL:.2f}")
    
    while True:
        print("\nEscolha uma opção (ou digite 'Sair' para fechar):")
        print("1. Dólar (USD) para Real (BRL)")
        print("2. Real (BRL) para Dólar (USD)")

        escolha = input("Digite 1, 2 ou 'Sair': ").lower()

        if escolha == 'sair':
            print("Fechando o programa. Até mais!")
            break

        try:
            opcao = int(escolha)

            if opcao == 1:
                valor_input = float(input("Digite o valor em Dólares (USD): "))
                valor_convertido = dolar_para_real(valor_input)
                print(f"Resultado: U$ {valor_input:.2f} é igual a R$ {valor_convertido:.2f}")
            elif opcao == 2:
                valor_input = float(input("Digite o valor em Reais (BRL): "))
                valor_convertido = real_para_dolar(valor_input)
                print(f"Resultado: R$ {valor_input:.2f} é igual a U$ {valor_convertido:.2f}")
            else:
                print("Opção inválida. Por favor, digite 1, 2 ou 'Sair'.")
        
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar um número válido para a opção e o valor.")

if __name__ == "__main__":
    main()