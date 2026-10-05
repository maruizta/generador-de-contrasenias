"""
Utilidad de Evaluación.

Valida los parámetros ingresados, verifica que la contraseña cumpla los
criterios de seguridad y calcula su nivel de seguridad.
"""

from randomness import CHARACTER_TYPES

ALLOWED_LENGTHS = (8, 12, 16)


def validate_parameters(length, selected_types):
    """Devuelve (True, "") si los parámetros son válidos o (False, mensaje) si no."""
    if length not in ALLOWED_LENGTHS:
        return False, "Length must be 8, 12 or 16 characters."
    if len(selected_types) == 0:
        return False, "You must select at least one character type."
    return True, ""


def contains_type(password, char_type):
    """Indica si la contraseña tiene al menos un carácter del tipo indicado."""
    for character in password:
        if character in CHARACTER_TYPES[char_type]:
            return True
    return False


def meets_criteria(password, length, selected_types):
    """Criterios de seguridad: longitud correcta y al menos un carácter
    de cada tipo seleccionado por el usuario."""
    if len(password) != length:
        return False
    for char_type in selected_types:
        if not contains_type(password, char_type):
            return False
    return True


def evaluate_strength(password):
    """Calcula el nivel de seguridad (Weak, Medium o Strong).

    Suma un punto por cada tipo de carácter presente y puntos extra
    según la longitud de la contraseña.
    """
    points = 0
    for char_type in CHARACTER_TYPES:
        if contains_type(password, char_type):
            points += 1

    if len(password) >= 16:
        points += 2
    elif len(password) >= 12:
        points += 1

    if points <= 2:
        return "Weak"
    elif points <= 4:
        return "Medium"
    else:
        return "Strong"
