
# Generador Seguro de Contraseñas

**Autor:** Marlon Javier Ruiz Taruchaín

**Asignatura:** Lógica de Programación, Universidad Internacional del Ecuador (UIDE)

**Docente:** Reidel González Paz

**Fecha:** 10 de octubre de 2026

## Objetivo del sistema

Ayudar a los usuarios a crear contraseñas seguras de forma rápida. El programa genera contraseñas aleatorias a partir de los parámetros que elige el usuario, verifica que cumplan criterios de seguridad y muestra su nivel de fortaleza.

## Funcionalidades

| Funcionalidad | Descripción |
|---|---|
| Configurar parámetros | Elegir la longitud (8, 12 o 16 caracteres) y los tipos de caracteres: minúsculas, mayúsculas, números y caracteres especiales. |
| Generar contraseña | Crea una contraseña aleatoria y la regenera hasta que contenga todos los tipos seleccionados. |
| Evaluar nivel de seguridad | Muestra el nivel (Weak, Medium o Strong) y qué tipos de caracteres contiene la contraseña. |
| Copiar contraseña | Copia la contraseña al portapapeles. |

## Ejecución

Requiere Python 3 con tkinter (incluido en la instalación estándar de Python).

```bash
python main.py
```

## Estructura del proyecto

| Archivo | Componente de la arquitectura | Responsabilidad |
|---|---|---|
| `main.py` | Punto de entrada | Inicia el programa. |
| `interface.py` | Capa de presentación | Ventana con tkinter: recibe los parámetros y muestra los resultados. |
| `controller.py` | Capa de lógica | Coordina la validación, la generación y la verificación de la contraseña. |
| `randomness.py` | Utilidad de aleatoriedad | Define los conjuntos de caracteres y genera la contraseña al azar. |
| `evaluation.py` | Utilidad de evaluación | Valida los parámetros, comprueba los criterios y calcula el nivel de seguridad. |

## Diagramas

- [Diagrama de casos de uso](Casos%20de%20Uso-Casos%20de%20Uso.jpg)
- [Diagrama de flujo](Casos%20de%20Uso-Diagrama%20de%20Flujo.jpg)
- [Diagrama de arquitectura](Casos%20de%20Uso-Diagrama%20de%20Arquitectura.jpg)

## Tecnologías

Python, tkinter, Visual Studio Code, draw.io, Git y GitHub.
