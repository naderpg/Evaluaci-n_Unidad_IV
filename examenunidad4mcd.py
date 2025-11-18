def main():
    print("--- Calculadora de MCD ---")

    a = int(input("Ingrese el primer número (a): "))
    b = int(input("Ingrese el segundo número (b): "))

    num1_original = a
    num2_original = b


    while b != 0:
        residuo = a % b
        
        a = b         
        b = residuo   


    print("-" * 30)
    print(f"El MCD de {num1_original} y {num2_original} es: {a}")

if __name__ == "__main__":
    main()