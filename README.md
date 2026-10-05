# Relación entre los diagramas y el software

## Correr la Aplicacion

```bash
python main.py
```

## Diagrama de casos de uso → Botones de la ventana

| Caso de uso | Control | Función |
|---|---|---|
| Configurar parámetros | Opciones *Length* y casillas *Character types* | `selected_types()` |
| Generar contraseña | Botón *Generate password* | `generate()` → `create_password()` |
| Evaluar nivel de seguridad | Botón *Evaluate strength* | `evaluate()` → `evaluate_strength()` |
| Copiar contraseña | Botón *Copy password* | `copy_password()` |

## Diagrama de flujo → `create_password()` (controller.py)

| Paso | Código |
|---|---|
| Inicio | `main.py` → `start()` |
| Escoger longitud y tipos | `Radiobutton` y `Checkbutton` |
| Almacenar parámetros | `IntVar` / `BooleanVar` en `widgets` |
| Construir conjuntos | `build_character_set()` |
| Generar contraseña | `generate_password()` |
| ¿Cumple criterios? NO → regenerar | ciclo `while` + `meets_criteria()` |
| Mostrar contraseña | `Entry` y etiqueta de nivel |
| Fin | cerrar la ventana (`mainloop()` termina) |

## Diagrama de arquitectura → Archivos

| Componente | Archivo |
|---|---|
| Capa de presentación | `interface.py` |
| Capa de lógica (controlador) | `controller.py` |
| Utilidad de aleatoriedad | `randomness.py` |
| Utilidad de evaluación | `evaluation.py` |


