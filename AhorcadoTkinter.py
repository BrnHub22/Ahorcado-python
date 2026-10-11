import random
import tkinter as tk
from tkinter import messagebox

# Paso 1: Datos del juego (igual que tu codigo original)
palabras = ["breakdance", "graffiti", "rap", "dj"]
palabra_secreta = random.choice(palabras)
letras_adivinadas = ["_" for _ in palabra_secreta]
letras_usadas = []
intentos = 3

# Paso 2: Ventana principal
root = tk.Tk()
root.title("Juego del Ahorcado - Cultura Urbana")
root.geometry("550x650")
root.configure(bg="#000000")
root.resizable(False, False)

# Paso 3: Funciones de dibujo del ahorcado ---
def dibujar_ahorcado(canvas, intentos_restantes):
    canvas.delete("all")
    # Base
    canvas.create_line(20, 230, 180, 230, width=4, fill="#A14503")
    canvas.create_line(50, 230, 50, 20, width=4, fill="#A14503")
    canvas.create_line(50, 20, 130, 20, width=4, fill="#A14503")
    canvas.create_line(130, 20, 130, 50, width=4, fill="#A14503")
    
    vidas_perdidas = 3 - intentos_restantes

    if vidas_perdidas >= 1: # Se dibuja la cabeza en el primer intento fallido
        canvas.create_oval(110, 50, 150, 90, width=3, outline="#EEFB00")

    if vidas_perdidas >= 2: # Se dibuja el cuerpo y los brazos en el segundo intento fallido
        canvas.create_line(130, 90, 130, 150, width=3, fill="#EEFB00")
        canvas.create_line(130, 110, 110, 130, width=3, fill="#EEFB00")
        canvas.create_line(130, 110, 150, 130, width=3, fill="#EEFB00")

    if vidas_perdidas >= 3: # Se dibujan las piernas en el tercer intento fallido
        canvas.create_line(130, 150, 110, 180, width=3, fill="#EEFB00")
        canvas.create_line(130, 150, 150, 180, width=3, fill="#EEFB00")
        canvas.create_text(100, 100, text="-------------", fill="#FB0000", font=("Arial", 16, "bold"))

# Paso 4: Lógica del juego (igual que tu while) ---
def actualizar_pantalla():
    palabra_mostrar = " ".join(letras_adivinadas)
    label_palabra.config(text=palabra_mostrar)
    if intentos == 1:
        label_vidas.config(text=f"Te queda {intentos} vidas", fg="#FF5252")
    else:
        label_vidas.config(text=f"Te quedan {intentos} vidas", fg="#FFFFFF" if intentos>1 else "#FF5252")
    label_usadas.config(text=f"Letras usadas: {', '.join(letras_usadas) if letras_usadas else 'ninguna'}")
    dibujar_ahorcado(canvas_ahorcado, intentos)

def reiniciar_juego():
    global palabra_secreta, letras_adivinadas, letras_usadas, intentos
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = ["_" for _ in palabra_secreta]
    letras_usadas = []
    intentos = 3
    entry_letra.config(state="normal")
    btn_adivinar.config(state="normal")
    label_mensaje.config(text="¡Adivina la palabra!", fg="#FFFFFF")
    actualizar_pantalla()

def verificar_letra():
    global intentos
    letra = entry_letra.get().lower().strip()
    entry_letra.delete(0, tk.END)

    # Reglas del juego
    if letra.isdigit():
        label_mensaje.config(text="Este es un número no una letra, intenta de nuevo", fg="#EEFB00")
        return
    if not letra.isalpha():
        label_mensaje.config(text="Este es un carácter no una letra, intenta de nuevo", fg="#EEFB00")
        return
    if len(letra) != 1:
        label_mensaje.config(text="Solo es válido ingresar UNA letra", fg="#EEFB00")
        return
    if letra in letras_usadas:
        label_mensaje.config(text=f"Ya usaste la letra '{letra}'", fg="#EEFB00")
        return

    letras_usadas.append(letra)

    # Indica si la letra es correcta
    if letra in palabra_secreta:
        label_mensaje.config(text=f"¡BIEN! La letra '{letra}' es correcta", fg="#00FF08")
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                letras_adivinadas[i] = letra

        # Indica que el jugador ha ganado 
        if "_" not in letras_adivinadas:
            actualizar_pantalla()
            messagebox.showinfo("¡Ganaste!", f"¡Ganaste! La palabra correcta es: {palabra_secreta}")
            label_mensaje.config(text=f"¡Ganaste! Era: {palabra_secreta}", fg="#00FF08")
            entry_letra.config(state="disabled")
            btn_adivinar.config(state="disabled")
            return
    # Indica que la letra es incorrecta    
    else:
        intentos -= 1
        if intentos == 1:
            label_mensaje.config(text=f"Fallaste, te queda {intentos} vida", fg="#FF5252")
        else:
            label_mensaje.config(text=f"Fallaste, te quedan {intentos} vidas", fg="#FF5252")

        # Indica que el jugador ha perdido y nos muestra la palabra correcta
        if intentos == 0:
            actualizar_pantalla()
            messagebox.showerror("Perdiste", f"Has perdido :( La palabra correcta era: {palabra_secreta}")
            label_mensaje.config(text=f"Perdiste. Era: {palabra_secreta}", fg="#FF5252")
            entry_letra.config(state="disabled")
            btn_adivinar.config(state="disabled")
            return

    actualizar_pantalla()

# Paso 5: Aqui mostramos titulos y subtutulos de la ventana del juego, el canvas del ahorcado, las vidas y la palabra, la entrada de letra, los mensajes y el boton de reiniciar
# Titulo
tk.Label(root, text="-----> BIENVENIDO AL JUEGO DEL AHORCADO <-----", bg="#121212", fg="#FFFFFF", font=("Consolas", 12, "bold")).pack(pady=10)
tk.Label(root, text="Pista: La palabra secreta es parte de una cultura urbana", bg="#121212", fg="#B39DDB", font=("Arial", 10, "italic")).pack()

# Canvas ahorcado
canvas_ahorcado = tk.Canvas(root, width=200, height=250, bg="#000000", highlightthickness=0)
canvas_ahorcado.pack(pady=10)

# Vidas y palabra
label_vidas = tk.Label(root, text="", bg="#121212", fg="#00FF08", font=("Arial", 15, "bold"))
label_vidas.pack()

label_palabra = tk.Label(root, text="", bg="#000000", fg="#00F2FF", font=("Consolas", 28, "bold"))
label_palabra.pack(pady=15)

# Entrada de letra 
frame_entrada = tk.Frame(root, bg="#000000")
frame_entrada.pack(pady=5)

# Entrada de letra y boton adivinar
tk.Label(frame_entrada, text="Ingresa una letra:", bg="#121212", fg="#FFFFFF", font=("Arial", 11)).pack(side="left", padx=5)
entry_letra = tk.Entry(frame_entrada, width=5, font=("Arial", 16, "bold"), justify="center")
entry_letra.pack(side="left", padx=5)
entry_letra.bind("<Return>", lambda e: verificar_letra())

# Boton adivinar 
btn_adivinar = tk.Button(frame_entrada, text="Adivinar", command=verificar_letra, bg="#4400FF", fg="white", font=("Arial", 11, "bold"), padx=15, relief="flat", cursor="hand2")
btn_adivinar.pack(side="left", padx=10)

# Mensajes 
label_mensaje = tk.Label(root, text="¡Adivina la palabra!", bg="#121212", fg="#FFFFFF", font=("Arial", 11), wraplength=450)
label_mensaje.pack(pady=10)

# letras ya usadas
label_usadas = tk.Label(root, text="", bg="#121212", fg="#9E9E9E", font=("Arial", 9))
label_usadas.pack()

# Boton reiniciar
tk.Button(root, text="Jugar de nuevo", command=reiniciar_juego, bg="#2E2E2E", fg="#FFFFFF", font=("Arial", 12), relief="flat", padx=20, pady=5, cursor="hand2").pack(side="bottom", pady=15)

# Inicializar
actualizar_pantalla()
entry_letra.focus()

# Sirve para mantener la ventana abierta hasta que el usuario la cierre 
root.mainloop()

