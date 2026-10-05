"""
Capa de Presentación (Interfaz gráfica de usuario).

Ventana desarrollada con tkinter que permite configurar los parámetros,
generar la contraseña, evaluar su nivel de seguridad y copiarla.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from controller import create_password
from evaluation import ALLOWED_LENGTHS, contains_type, evaluate_strength

TYPE_NAMES = {
    "lowercase": "Lowercase letters (a-z)",
    "uppercase": "Uppercase letters (A-Z)",
    "numbers": "Numbers (0-9)",
    "special": "Special characters (!@#$...)",
}

STRENGTH_COLORS = {
    "Weak": "#C0392B",
    "Medium": "#D68910",
    "Strong": "#1E8449",
}

# Controles y variables de la ventana; se llenan en create_window() para
# que las demás funciones puedan usarlos
widgets = {}


def selected_types():
    """Devuelve la lista de tipos de caracteres marcados por el usuario."""
    selected = []
    for char_type, variable in widgets["types"].items():
        if variable.get():
            selected.append(char_type)
    return selected


def generate():
    """Caso de uso: Generar contraseña."""
    try:
        password, strength, attempts = create_password(widgets["length"].get(),
                                                       selected_types())
    except ValueError as error:
        messagebox.showwarning("Invalid parameters", str(error))
        return

    widgets["password"].set(password)
    widgets["strength_label"].config(text="Strength: " + strength,
                                     fg=STRENGTH_COLORS[strength])
    widgets["detail_label"].config(text="Attempts to meet the criteria: " + str(attempts))


def evaluate():
    """Caso de uso: Evaluar nivel de seguridad."""
    password = widgets["password"].get()
    if password == "":
        messagebox.showinfo("Evaluate", "Generate a password first.")
        return

    detail = "Length: " + str(len(password)) + " characters\n"
    for char_type, name in TYPE_NAMES.items():
        if contains_type(password, char_type):
            mark = "Yes"
        else:
            mark = "No"
        detail += name + ": " + mark + "\n"
    detail += "Strength: " + evaluate_strength(password)
    widgets["detail_label"].config(text=detail)


def copy_password():
    """Caso de uso: Copiar contraseña al portapapeles."""
    password = widgets["password"].get()
    if password == "":
        messagebox.showinfo("Copy", "Generate a password first.")
        return

    widgets["window"].clipboard_clear()
    widgets["window"].clipboard_append(password)
    messagebox.showinfo("Copy", "Password copied to clipboard.")


def create_widgets(window):
    """Crea y ubica todos los controles dentro de la ventana."""
    frame = ttk.Frame(window, padding=20)
    frame.grid()

    title = ttk.Label(frame, text="Secure Password Generator",
                      font=("Helvetica", 16, "bold"))
    title.grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # Caso de uso: Configurar parámetros (longitud y tipos)
    length_frame = ttk.LabelFrame(frame, text="Length", padding=10)
    length_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 10))
    for length in ALLOWED_LENGTHS:
        option = ttk.Radiobutton(length_frame, text=str(length) + " characters",
                                 variable=widgets["length"], value=length)
        option.grid(sticky="w")

    types_frame = ttk.LabelFrame(frame, text="Character types", padding=10)
    types_frame.grid(row=1, column=1, sticky="nsew")
    for char_type, name in TYPE_NAMES.items():
        checkbox = ttk.Checkbutton(types_frame, text=name, variable=widgets["types"][char_type])
        checkbox.grid(sticky="w")

    # Caso de uso: Generar contraseña
    generate_button = ttk.Button(frame, text="Generate password", command=generate)
    generate_button.grid(row=2, column=0, columnspan=2, pady=15)

    field = ttk.Entry(frame, textvariable=widgets["password"], state="readonly",
                      font=("Courier", 16), width=24, justify="center")
    field.grid(row=3, column=0, columnspan=2)

    widgets["strength_label"] = tk.Label(frame, text="Strength: -",
                                         font=("Helvetica", 13, "bold"))
    widgets["strength_label"].grid(row=4, column=0, columnspan=2, pady=10)

    # Casos de uso: Evaluar nivel de seguridad y Copiar contraseña
    buttons_frame = ttk.Frame(frame)
    buttons_frame.grid(row=5, column=0, columnspan=2)
    evaluate_button = ttk.Button(buttons_frame, text="Evaluate strength", command=evaluate)
    evaluate_button.grid(row=0, column=0, padx=5)
    copy_button = ttk.Button(buttons_frame, text="Copy password", command=copy_password)
    copy_button.grid(row=0, column=1, padx=5)

    widgets["detail_label"] = ttk.Label(frame, text="", justify="left")
    widgets["detail_label"].grid(row=6, column=0, columnspan=2, pady=(10, 0))


def create_window():
    """Crea la ventana principal, sus variables y sus controles."""
    window = tk.Tk()
    window.title("Secure Password Generator")
    window.resizable(False, False)

    # Variables asociadas a los controles de la ventana
    widgets["window"] = window
    widgets["length"] = tk.IntVar(value=12)
    widgets["types"] = {}
    for char_type in TYPE_NAMES:
        widgets["types"][char_type] = tk.BooleanVar(value=True)
    widgets["password"] = tk.StringVar()

    create_widgets(window)
    return window


def start():
    """Abre la ventana y la mantiene activa hasta que el usuario la cierre."""
    window = create_window()
    window.mainloop()
