# Guía de Ruff para Estudiantes

Esta guía te explica cómo usar **ruff** para escribir código Python profesional y limpio.

---

## 🎯 Qué es Ruff

**Ruff** es un linter (analizador de código) que revisa tu código Python y te da sugerencias para mejorarlo.

Piensa en Ruff como un **coach de código** que:
- Detecta errores que harían que tu código no funcione
- Sugiere mejores prácticas de programación
- Te enseña a escribir código más profesional y Pythonic

No es un enemigo ni un obstáculo, es una herramienta de aprendizaje.

---

## 📊 Los 3 Niveles de Errores de Ruff

### 🔴 CRÍTICO (E, F) - "Tu código no funcionará"

**Códigos:** `E4`, `E7`, `E9`, `F`

**Debes corregirlos obligatoriamente.** Si no lo haces, tu código no funcionará correctamente.

| Código | Categoría | Descripción | Ejemplo |
|--------|-----------|-------------|---------|
| **E4** | pycodestyle | Errores de importación | `import modulo_inexistente` |
| **E7** | pycodestyle | Errores de comparación | `if x = 1:` (en lugar de `==`) |
| **E9** | pycodestyle | Errores de sintaxis | `print("hola"` (falta paréntesis) |
| **F** | pyflakes | Errores semánticos | Variable no definida, import no usado |

---

### 🟠 IMPORTANTE (A, C4, BLE, I, W) - "Buena práctica que evita bugs"

**Códigos:** `A`, `C4`, `BLE`, `I`, `W`

**Debes intentar corregirlos.** Enseñan hábitos importantes que evitan bugs comunes.

| Código | Categoría | Descripción | Ejemplo |
|--------|-----------|-------------|---------|
| **A** | builtins | No shadowing de builtins | `list = [1,2,3]` ❌ |
| **C4** | comprehensions | Mejores prácticas | `set([x for x in l])` ❌ |
| **BLE** | blind-except | Evitar excepciones bare | `except:` ❌ |
| **I** | isort | Orden de imports | Imports desordenados ❌ |
| **W** | pycodestyle | Advertencias | Comparaciones innecesarias |

---

### 🟡 EDUCATIVO (B, SIM, UP, N) - "Mejora la calidad de tu código"

**Códigos:** `B` (seleccionados), `SIM`, `UP`, `N` (seleccionados)

**Aprende de estos consejos.** Hacen tu código más profesional, pero no son críticos.

#### Bugbear (seleccionadas)
| Código | Descripción | Ejemplo |
|--------|-------------|---------|
| **B006** | No usar mutables como default | `def f(x=[]):` ❌ |
| **B007** | Variable de loop no usada | `for i in range(10): pass` ❌ |
| **B008** | No hacer llamadas en defaults | `def f(x=time()):` ❌ |
| **B905** | zip() sin strict | `zip(a, b)` ❌ |

#### Python moderno
| Código | Descripción | Ejemplo |
|--------|-------------|---------|
| **SIM** | Simplificar código | Código verbose |
| **UP** | pyupgrade | Sintaxis moderna (f-strings) |

#### Naming (seleccionadas)
| Código | Descripción | Ejemplo |
|--------|-------------|---------|
| **N802** | Función en camelCase | `def miFuncion():` ❌ |
| **N803** | Argumento en camelCase | `def f(x):` ❌ |
| **N806** | Variable en camelCase | `miVariable = 1` ❌ |

---

## 🚀 Comandos Útiles

### Ver Errores en tu Código

```bash
ruff check calculadora/
```

Muestra todos los errores que encuentra ruff en tu código.

---

### Autocorregir lo Posible

```bash
ruff check calculadora/ --fix
```

Intenta corregir automáticamente muchos errores. **Siempre revisa** lo que autocorrigió.

---

### Ver Explicaciones Detalladas

```bash
ruff check calculadora/ --explain
```

Muestra explicaciones detalladas de cada error encontrado.

---

### Ver Explicación de una Regla Específica

```bash
ruff rule B006
```

Muestra la explicación completa de la regla `B006`.

---

### Formatear el Código (como Black)

```bash
ruff format calculadora/
```

Formatea tu código automáticamente (indentación, espacios, etc.).

---

## 📝 Errores Más Comunes y Cómo Corregirlos

### 1. E0602 - Variable No Definida

```python
# ❌ ERROR
x = y + 1  # 'y' no está definida

# ✅ CORRECTO
y = 5
x = y + 1
```

**Causa:** Usaste una variable que no existe.

**Solución:** Define la variable antes de usarla.

---

### 2. F401 - Import No Usado

```python
# ❌ ERROR
import math
x = 5 + 3

# ✅ CORRECTO
x = 5 + 3  # Eliminar el import
```

**Causa:** Importaste un módulo pero no lo usaste.

**Solución:** Elimina el import innecesario.

---

### 3. B006 - Mutable Como Default

```python
# ❌ ERROR
def agregar_elemento(lista=[]):
    lista.append(1)
    return lista

# ✅ CORRECTO
def agregar_elemento(lista=None):
    if lista is None:
        lista = []
    lista.append(1)
    return lista
```

**Causa:** Usar mutable (lista, dict, set) como argumento por defecto es peligroso porque se comparte entre todas las llamadas.

**Solución:** Usa `None` como default y crea el mutable dentro de la función.

---

### 4. BLE001 - Excepción Bare

```python
# ❌ ERROR
try:
    resultado = 10 / 0
except:
    pass  # ¡Oculta todos los errores!

# ✅ CORRECTO
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
```

**Causa:** Capturar todas las excepciones (`except:`) es peligroso porque oculta errores importantes.

**Solución:** Captura solo el tipo de excepción específico que esperas.

---

### 5. N802 - Nombre de Función en camelCase

```python
# ❌ ERROR
def calcularResultado():
    pass

# ✅ CORRECTO
def calcular_resultado():
    pass
```

**Causa:** En Python se usa `snake_case` para funciones y variables, no `camelCase`.

**Solución:** Usa guiones bajos en lugar de mayúsculas para separar palabras.

---

### 6. UP031 - Formato Viejo de String

```python
# ❌ ERROR
mensaje = "Hola %s, tienes %d años" % (nombre, 25)

# ✅ CORRECTO
mensaje = f"Hola {nombre}, tienes {25} años"
```

**Causa:** Formato viejo con `%` es menos legible que f-strings.

**Solución:** Usa f-strings (Python 3.6+) que son más modernos y legibles.

---

### 7. A001 - Shadowing de Builtin

```python
# ❌ ERROR
list = [1, 2, 3]  # 'list' es un builtin de Python

# ✅ CORRECTO
numeros = [1, 2, 3]
```

**Causa:** Usar nombres de builtins de Python como variables puede causar bugs confusos.

**Solución:** Usa nombres descriptivos que no coincidan con builtins.

---

### 8. C401 - Uso Innecesario de list()

```python
# ❌ ERROR
conjunto = set([x for x in lista])

# ✅ CORRECTO
conjunto = {x for x in lista}
```

**Causa:** `set([x for x in l])` crea una lista innecesaria antes de crear el set.

**Solución:** Usa `{x for x in l}` directamente para crear el set.

---

## 🔄 Flujo de Trabajo Recomendado

### Mientras Escribes Código

1. Escribe tu código normalmente
2. De vez en cuando ejecuta:
   ```bash
   ruff check calculadora/
   ```
3. Corrige los errores que puedas
4. Pregunta si no entiendes algún error

---

### Antes de Hacer Commit

1. **Autocorregir:**
   ```bash
   ruff check calculadora/ --fix
   ```

2. **Revisar lo que queda:**
   ```bash
   ruff check calculadora/
   ```

3. **Corregir manualmente** lo que no se autocorrigió

4. **Verificar que todo esté limpio:**
   ```bash
   ruff check calculadora/
   ```
   Deberías ver: `All checks passed!`

5. **Ejecutar pruebas:**
   ```bash
   pytest tests/ -v
   ```

6. **Commit:**
   ```bash
   git add .
   git commit -m "feat: descripción clara"
   ```

---

## ❓ Preguntas Frecuentes

### ¿Por qué tengo que usar ruff?

Porque te enseña a escribir código profesional. Las reglas de ruff se basan en años de experiencia de programadores expertos.

---

### ¿Qué pasa si un error no tiene sentido para mí?

¡Pregunta! Tu instructor puede explicarlo. A veces hay excepciones justificadas.

---

### ¿Puedo ignorar un error?

Generalmente no, a menos que tu instructor lo autorice explícitamente. Las reglas están por una razón importante.

---

### ¿Cuánto tiempo debo dedicar a corregir errores?

Al principio puede tomar tiempo, pero con la práctica escribirás código que cumple las reglas naturalmente.

---

### ¿Las reglas son solo para este proyecto?

No, son estándares de Python. Te servirán en cualquier proyecto Python que hagas en el futuro.

---

### ¿Qué pasa si no entiendo un error?

1. Lee el mensaje de error con cuidado
2. Ejecuta `ruff rule <codigo>` para ver explicación
3. Busca en internet el código de error
4. ¡Pregunta a tu instructor!

---

### ¿Es normal tener muchos errores al principio?

Sí, es completamente normal. Con la práctica, escribir código que cumple las reglas se volverá natural.

---

## ✅ Checklist Antes de Entregar

Antes de hacer commit y push a GitHub, verifica:

- [X] Ejecuté `ruff check calculadora/ --fix`
- [X] Corregí todos los errores rojos (CRÍTICOS: E, F)
- [X] Corregí los errores naranjas (IMPORTANTES: A, C4, BLE, I, W)
- [X] Corregí los errores amarillos (EDUCATIVOS: B, SIM, UP, N)
- [X] `ruff check calculadora/` muestra "All checks passed!"
- [X] Mi código se ejecuta sin errores de sintaxis
- [X] Mis pruebas pasan: `pytest tests/ -v`

---

## 📚 Reglas que Están Deshabilitadas

Algunas reglas están deshabilitadas en `ruff.toml` porque no son apropiadas para estudiantes:

- **E501** - Líneas muy largas (estudiantes pueden tener monitores pequeños)
- **E741** - Variables de una letra (muy pedante para principiantes)
- **ERA001** - Comentarios eliminados (útil para debugging)
- **SIM108** - Ternarios (pueden reducir legibilidad)
- **UP035** - Typing imports viejos (puede ser confuso al aprender typing)

---

## 🎯 Conclusión

**Ruff es tu amigo, no tu enemigo.** Te ayuda a escribir mejor código y te hace un programador más valioso en el mercado laboral.

No te frustres si tienes errores al principio. Es completamente normal. Con la práctica, escribir código que cumple las reglas de ruff será natural para ti.

¡Estás aprendiendo a escribir código profesional! 🚀

---

## 📖 Recursos Adicionales

- **Documentación oficial de Ruff:** https://docs.astral.sh/ruff/
- **Guía de estilo de Python (PEP 8):** https://peps.python.org/pep-0008/
- **Documentación del proyecto:**
  - `docs/PRACTICA.md` - Especificación de la práctica
  - `docs/PRUEBAS.md` - Guía de pruebas

---

**Versión:** 1.0
**Fecha:** Marzo 2026
**Proyecto:** Unidad 1 - Lenguajes y Autómatas I
