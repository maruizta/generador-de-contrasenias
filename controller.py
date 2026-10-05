"""
Capa de Lógica (Controlador).

Coordina la generación y la validación de la contraseña siguiendo el
diagrama de flujo: construir el conjunto de caracteres, generar la
contraseña y regenerarla mientras no cumpla los criterios de seguridad.
"""

from randomness import build_character_set, generate_password
from evaluation import validate_parameters, meets_criteria, evaluate_strength


def create_password(length, selected_types):
    """Devuelve la contraseña generada, su nivel de seguridad y el número
    de intentos que fueron necesarios."""
    valid, message = validate_parameters(length, selected_types)
    if not valid:
        raise ValueError(message)

    character_set = build_character_set(selected_types)

    # Generar contraseña -> ¿Cumple con los criterios? -> NO: volver a generar
    attempts = 0
    while True:
        attempts += 1
        password = generate_password(length, character_set)
        if meets_criteria(password, length, selected_types):
            break

    strength = evaluate_strength(password)
    return password, strength, attempts
