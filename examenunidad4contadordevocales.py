def main():
    print("--- contador de letritas ---")

    frase_usuario = input("dame una frase para contar: ")

    conteo_vocales = 0
    conteo_consonantes = 0

    for caracter in frase_usuario:
        
#toco usar ascii para no usar librerias o cadenas de texto
        valor_ascii = ord(caracter)

        if 65 <= valor_ascii <= 90:
            valor_ascii = valor_ascii + 32 


        if 97 <= valor_ascii <= 122:
            

            if (valor_ascii == 97 or valor_ascii == 101 or valor_ascii == 105 or 
                valor_ascii == 111 or valor_ascii == 117):
                conteo_vocales += 1
            else:

                conteo_consonantes += 1

    print("-" * 30)
    print(f"Frase analizada: \"{frase_usuario}\"")
    print(f"Vocales: {conteo_vocales}")
    print(f"Consonantes: {conteo_consonantes}")

if __name__ == "__main__":
    main()