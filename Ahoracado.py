# Sirve para elegir una palabra de forma aleatoria de la lista
import random 

# Sirve para crear una lista
palabras = ["breakdance", "graffiti", "rap", "dj"] 

# Sirve para elegir una palabra de forma aleatoria de la lista
palabra_secreta = random.choice(palabras)

# Sirve para guardar las letras adivinadas
letras_adivinadas = []

# En esta parte es los titulos que apareceran al momento de ejecutar el programa
print("----->BIENVENIDO AL JUEGO DEL AHORCADO<-----")

print("Pista:La palabra secreta es parte de una cultura urbana")

print("Recuerda tienes 3 vidas <3 , buena suerte")

# Sirve para mostrar la cantidad de letras por adivinar
for letra in palabra_secreta:
    letras_adivinadas.append("_")

# Aqui añadimos join para que se muestre mas limpio la palabra que se debe adivinar
print(" ".join(letras_adivinadas))

# Aqui creamos una variable para dar paso al bucle while
intentos = 3

# Aqui comienza el juego hasta que se acaben los intentos o adivine la palabra
while intentos > 0:
    letra = input("Ingrese una letra: ")

    if letra.isdigit(): # Sirve para que el usuario no pueda ingresar un numero 
        print("Este es un numero no una letra, intentalo de nuevo")
        continue # sirve para que continue con el bucle while

    if not letra.isalpha(): # Sirve para que el usuario no ingrese un caracter especial
        print("Este es un caracter no una letra, intentalo de nuevo")
        continue # sirve para que continue con el bucle while   

    if len(letra) != 1: # Sirve para que el usuario no ingrese dos o mas letras
        print("Solo es valido ingresar una letra, intentalo de nuevo")
        continue # sirve para que continue con el bucle while 

    if letra in palabra_secreta: # Sirve para decirle al usuario que la letra presionada es correcta y pone la letra donde corresponde
        print("Letra correcta bien hecho")

        for i in range(len(palabra_secreta)): # Sirve para saber cuantas letras tiene la palabra oculta y saber donde ponerla   
            if palabra_secreta[i] == letra: # Sirve para poner la letra donde corresponde 
                letras_adivinadas [i] = letra # Sirve para reemplazar el guion bajo por la letra adivinada
                
                print(" ".join(letras_adivinadas)) # # Aqui añadimos join para que se muestre mas limpio la palabra ya adivinada


        if "_" not in letras_adivinadas: # Sirve para decir al usuario que adivino la palabra
            print("Ganaste, la palabra correcta es: ", palabra_secreta)
            
            break # El break forza el cierre del bucle while por que se adivino la palabra secreta   
    
    else: # Sirve para decirle al usuario que la letra presionada es incorrecta y le resta una vida
        intentos = intentos - 1
        if intentos == 1:
            print(f"fallaste en la letra, tienes {intentos} vida")
        else:
            print(f"Fallaste en la letra, tienes {intentos} vidas")
          
        
if intentos == 0: # Sirve para decirle al usuario que perdio y cual era la palabra secreta
    print("Has perdido :( no te quedan vidas, la palabra correcta era: ", palabra_secreta)



    












