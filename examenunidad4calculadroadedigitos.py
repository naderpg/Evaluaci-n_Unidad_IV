def main():
    print("calculadora division")


    entrada_usuario = input("ingrese un numero entero: ")
    numero_ingresado = int(entrada_usuario)

    if numero_ingresado < 0:
        print("por favor ingrese un numero mayor a cero")
    else:
        suma_total = 0
        numero_temporal = numero_ingresado

        while numero_temporal > 0:
            ultimo_digito = numero_temporal % 10
            suma_total = suma_total + ultimo_digito
            numero_temporal = numero_temporal // 10

        print("-"*30)
        print(f"numero dividido: {numero_ingresado}")
        print(f"la division queda en: {suma_total}")


if __name__ == "__main__":
    main()
