def main():
    print("--- Verificador de Números Primos ---")

    entrada = input("Por favor, ingrese un número entero positivo: ")
    numero = int(entrada)

    if numero <= 1:
        print(f"El número {numero} NO es primo.")
    
    else:
        es_primo = True
        

        raiz = numero ** 0.5
        
        limite = int(raiz) + 1
        

        for i in range(2, limite):
            
            if numero % i == 0:
                es_primo = False
                break 
        
        print("-" * 30)
        if es_primo:
            print(f"El número {numero} ES primo.")
        else:
            print(f"El número {numero} NO es primo.")

if __name__ == "__main__":
    main()