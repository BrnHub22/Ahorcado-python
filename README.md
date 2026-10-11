# 🎮 Juego del Ahorcado en Python - Cultura Urbana

Clásico juego del ahorcado por consola **y ahora con interfaz gráfica Tkinter**. Adivina la palabra secreta letra por letra antes de quedarte sin vidas.

> Temática actual: **Cultura Urbana (Hip Hop)** - Palabras: `breakdance`, `graffiti`, `rap`, `dj`

### ✨ Características

- El jugador consta de 3 vidas por partida <3
- Incluye una pista: "La palabra secreta es parte de una cultura urbana"
- Sistema de validación: No permite números (`isdigit()`), caracteres especiales (`isalpha()`) ni más de una letra (`len()`)
- Dos versiones: consola y ventana

### 📂 Estructura del Proyecto

```
Ahorcado-python/
├── Ahorcado.py              # Versión consola original
├── AhorcadoTkinter.py       # Versión con interfaz gráfica (Tkinter)
├── Diagrama_Ahorcado.drawio # Diagrama de flujo editable (draw.io)
└── README.md
```

### 🖥️ Versión 1: Consola

```bash
python Ahorcado.py
```

### 🖌️ Versión 2: Tkinter 

```bash
python AhorcadoTkinter.py
```

**Mejoras de la versión Tkinter:**
- Ventana con colores neón personalizados (fondo #000000, horca #A14503, muñeco #EEFB00, palabra #00F2FF)
- Canvas que dibuja el ahorcado progresivamente
- Labels dinámicos para vidas, palabra oculta y letras usadas
- Validaciones con mensajes en pantalla en vez de print()
- Botón "Jugar de nuevo" que reinicia con `random.choice()`
- Soporte para Enter + Click
- MessageBox para victoria/derrota

### 🔄 Diagrama de Flujo

El diagrama muestra la lógica completa con validaciones `isdigit()`, `isalpha()`, `len() != 1` y las ramas Si/No.

[Diagrama](Diagrama_Ahorcado.png)

Puedes editarlo en [https://app.diagrams.net](https://app.diagrams.net/) abriendo `Diagrama_Ahorcado.drawio`

### 🧠 Concepto Clave: while vs def

En consola usamos `while intentos > 0` + `input()`. En Tkinter no se puede usar `while` porque `mainloop()` ya es un bucle infinito que escucha eventos. Por eso se usa `def verificar_letra()` conectado al botón con `command=`. Cada click equivale a una iteración del while.

### 👨‍💻 Autor
**BrnHub22 (Brayan Cope)** - 2026 - Lógica de Programación
