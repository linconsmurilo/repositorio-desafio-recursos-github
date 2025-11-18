def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print("--- Conversor de Temperatura ---")
    
    while True:
        print("\nEscolha uma opção (ou digite 'Sair' para fechar):")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")

        escolha = input("Digite 1, 2 ou 'Sair': ").lower()

        if escolha == 'sair':
            print("Fechando o programa. Até mais!")
            break 

        try:
            opcao = int(escolha)

            if opcao == 1:
                temp_celsius = float(input("Digite a temperatura em Celsius: "))
                temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)
                print(f"Resultado: {temp_celsius:.2f}°C é igual a {temp_fahrenheit:.2f}°F")
            elif opcao == 2:
                temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
                temp_celsius = fahrenheit_para_celsius(temp_fahrenheit)
                print(f"Resultado: {temp_fahrenheit:.2f}°F é igual a {temp_celsius:.2f}°C")
            else:
                print("Opção inválida. Por favor, digite 1, 2 ou 'Sair'.")
        
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar um número válido para a opção e temperatura.")

if __name__ == "__main__":
    main()