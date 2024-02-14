import tkinter as tk
from tkinter import messagebox
import re

def lexical_analyzer(input_string):
    # Definimos los patrones para identificar tokens
    patterns = {
        'PALABRA R': r'base|altura|Area',
        'IDENTIFICADOR': r'[a-zA-Z_][a-zA-Z0-9_]*',
        'OPERADOR': r'[-+*/=]',
        'NUMERO': r'\d+',
        'SIMBOLO': r'[()]'
    }

    token_types = {key: set() for key in patterns.keys()}

    # Buscamos tokens en el input_string
    for key, pattern in patterns.items():
        matches = re.findall(pattern, input_string)
        for match in matches:
            token_types[key].add(match)

    # Extraemos tokens no clasificados como palabras reservadas
    palabras_reservadas_encontradas = token_types['PALABRA R']
    for key, pattern in patterns.items():
        if key != 'PALABRA R':
            token_types[key] = token_types[key].difference(palabras_reservadas_encontradas)

    return token_types

def display_table(token_types):
    result = ""
    result += '{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}'.format('TOKEN', 'PALABRA R', 'IDENTIFICADOR', 'OPERADOR', 'NUMERO', 'SIMBOLO') + "\n"
    for token in set.union(*(token_types.values())):
        result += '{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}'.format(
            token, 
            'X' if token in token_types['PALABRA R'] else '', 
            'X' if token in token_types['IDENTIFICADOR'] else '', 
            'X' if token in token_types['OPERADOR'] else '', 
            'X' if token in token_types['NUMERO'] else '', 
            'X' if token in token_types['SIMBOLO'] else ''
        ) + "\n"
    return result

def analyze_input():
    input_string = input_text.get("1.0", tk.END)  # Obtener el contenido desde la primera línea hasta el final
    if not input_string.strip():
        messagebox.showerror("Error", "Por favor, ingresa una cadena válida.")
        return
    token_types = lexical_analyzer(input_string)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, display_table(token_types))

# Crear ventana
root = tk.Tk()
root.title("Analizador Léxico")

root.configure(background='#FFFF00')  # Fondo amarillo

# Crear widgets
input_label = tk.Label(root, text="INGRESAR DATOS:", background='#FFFF00')  # Fondo amarillo
input_label.pack()

input_text = tk.Text(root, height=5, width=50)
input_text.pack()

analyze_button = tk.Button(root, text="ANALIZAR", command=analyze_input, background='#9370DB')  # Botón lila
analyze_button.pack()

result_label = tk.Label(root, text="RESULTADOS:", background='#FFFF00')  # Fondo amarillo
result_label.pack()

result_text = tk.Text(root, height=30, width=90)
result_text.pack()

# Ejecutar la interfaz
root.mainloop()

