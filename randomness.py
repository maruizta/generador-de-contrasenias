"""
Utilidad de Aleatoriedad.

Construye el conjunto de caracteres a partir de los tipos elegidos por el
usuario y genera la contraseña de forma aleatoria.
"""

import random

# Conjuntos de caracteres definidos para el generador
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIAL = "!@#$%&*()-_=+[]{};:,.?/"

CHARACTER_TYPES = {
    "lowercase": LOWERCASE,
    "uppercase": UPPERCASE,
    "numbers": NUMBERS,
    "special": SPECIAL,
}


def build_character_set(selected_types):
    """Une los caracteres de todos los tipos seleccionados en un solo conjunto."""
    character_set = ""
    for char_type in selected_types:
        character_set += CHARACTER_TYPES[char_type]
    return character_set


def generate_password(length, character_set):
    """Genera una contraseña eligiendo caracteres al azar del conjunto."""
    password = ""
    for _ in range(length):
        password += random.choice(character_set)
    return password
