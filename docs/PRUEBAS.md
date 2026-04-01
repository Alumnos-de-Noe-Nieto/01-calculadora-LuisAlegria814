# Guía de Pruebas Locales

Este documento te explica cómo ejecutar pruebas localmente antes de hacer commit y push a tu repositorio.

---

## 🎯 Por Qué Correr Pruebas Localmente

Ejecutar pruebas localmente te permite:

1. **Detectar errores temprano:** Saber si tu implementación es correcta antes de enviar
2. **Ahorrar tiempo:** No esperar a GitHub Actions para ver resultados
3. **Iterar rápidamente:** Probar, corregir, volver a probar sin commits intermedios
4. **Confianza:** Saber que tu código funciona antes de compartirlo

---

## 📋 Prerrequisitos

Antes de ejecutar pruebas, asegúrate de:

- Python 3.14+ instalado en Windows 11
- pytest instalado: `pip install pytest`
- Repositorio clonado en tu máquina
- Estás en la raíz del proyecto (donde está `README.md`)

> **Nota:** Esta guía asume que ya sabes cómo operar Python y Git desde la línea de comandos.

---

## 🚀 Ejecutar Todas las Pruebas

### Comando Básico

```bash
pytest tests/ -v
```

**Resultado esperado:**

```
============================ test session starts =============================
platform win32 -- Python 3.14.0, pytest-7.4.4
collected 82 items

tests/test_nivel_1_alfabeto.py::test_nivel_1_1_el_vacio_de_cartago PASSED
tests/test_nivel_1_alfabeto.py::test_nivel_1_2_la_invasion_barbara PASSED
...

========================= 82 passed in X.XXs =====================
```

**Significado:**
- **82 passed:** Todos los tests funcionales pasaron (Niveles 1-8)

---

## 📊 Ejecutar Pruebas por Nivel

### Nivel 1: Alfabeto

```bash
pytest tests/test_nivel_1_alfabeto.py -v
```

**Qué verificar:**
- Validación de símbolos válidos (I, V, X, L, C, D, M)
- Rechazo de caracteres inválidos
- Manejo de cadenas vacías
- Manejo de espacios en blanco

**Resultado esperado (completado):**
```
8 passed in X.XXs
```

---

### Nivel 2: Repeticiones I/X/C/M

```bash
pytest tests/test_nivel_2_repeticiones_icxm.py -v
```

**Qué verificar:**
- Repeticiones válidas (III, XXX, CCC, MMM)
- Repeticiones inválidas (IIII, XXXX, CCCC, MMMM)
- Mezcla de repeticiones válidas

**Resultado esperado (completado):**
```
9 passed in X.XXs
```

---

### Nivel 3: Repeticiones V/L/D

```bash
pytest tests/test_nivel_3_repeticiones_vld.py -v
```

**Qué verificar:**
- Repeticiones válidas (V, L, D únicos)
- Repeticiones inválidas (VV, LL, DD)
- Mezcla con otros símbolos

**Resultado esperado (completado):**
```
10 passed in X.XXs
```

---

### Nivel 4: Orden Descendente

```bash
pytest tests/test_nivel_4_orden_descendente.py -v
```

**Qué verificar:**
- Orden descendente válido (XVI, MDCLXVI)
- Sustracciones válidas (IV, IX, XL, etc.)
- Orden inválido (IVX, IIV, VIV)

**Resultado esperado (completado):**
```
10 passed in X.XXs
```

---

### Nivel 5: Restas Válidas

```bash
pytest tests/test_nivel_5_restas.py -v
```

**Qué verificar:**
- Las 6 restas válidas (IV, IX, XL, XC, CD, CM)
- Restas inválidas (IL, IC, XD, XM)
- Múltiples restas válidas

**Resultado esperado (completado):**
```
9 passed in X.XXs
```

---

### Nivel 6: Conversión

```bash
pytest tests/test_nivel_6_conversor.py -v
```

**Qué verificar:**
- Conversión de símbolos básicos (I→1, V→5, etc.)
- Conversión con sustracciones (IV→4, IX→9)
- Conversión de números complejos (MCMXCIV→1994)
- Validaciones previas (debe fallar si cadena no es válida)

**Resultado esperado (completado):**
```
6 passed in X.XXs
```

---

### Nivel 7: Parsing

```bash
pytest tests/test_nivel_7_parser.py -v
```

**Qué verificar:**
- Tokenización de expresiones básicas
- Tokenización de expresiones con espacios
- Tokenización de expresiones sin espacios
- Validación de estructura válida
- Detección de estructura inválida
- Manejo de expresiones vacías

**Resultado esperado (completado):**
```
12 passed in X.XXs
```

---

### Nivel 8: Orquestación

```bash
pytest tests/test_nivel_8_orquestacion.py -v
```

**Qué verificar:**
- Sumas básicas
- Sumas complejas
- Sumas con sustracciones
- Restas básicas
- Restas complejas
- Expresiones sin espacios
- Resultados negativos (deben lanzar excepción)

**Resultado esperado (completado):**
```
12 passed in X.XXs
```

---

## 🔍 Leer Resultados de Pruebas

### Éxito

```
tests/test_nivel_1_alfabeto.py::test_nivel_1_1_el_vacio_de_cartago PASSED
tests/test_nivel_1_alfabeto.py::test_nivel_1_2_la_invasion_barbara PASSED
...
========================= 8 passed in X.XXs =====================
```

✅ **Todo bien:** Tu implementación es correcta, puedes continuar al siguiente nivel.

---

### Falla

```
tests/test_nivel_1_alfabeto.py::test_nivel_1_1_el_vacio_de_cartago FAILED
tests/test_nivel_1_alfabeto.py::test_nivel_1_2_la_invasion_barbara PASSED
...
========================= 1 passed, 1 failed in X.XXs =====================

FAILED tests/test_nivel_1_alfabeto.py::test_nivel_1_1_el_vacio_de_cartago - AssertionError: assert False == True

tests/test_nivel_1_alfabeto.py:6: AssertionError
```

❌ **Hay errores:** Revisa tu implementación:
1. Lee el test específico que falló
2. Entiende qué se está probando
3. Corrige tu implementación
4. Vuelve a ejecutar el test

---

### Error

```
tests/test_nivel_1_alfabeto.py::test_nivel_1_1_el_vacio_de_cartago ERROR
tests/test_nivel_1_alfabeto.py::test_nivel_1_2_la_invasion_barbara SKIPPED
...
========================= 0 passed, 1 error in X.XXs =====================

ERROR tests/test_nivel_1_alfabeto.py::test_nivel_1_1_el_vacio_de_cartago - NotImplementedError
```

⚠️ **No has implementado la función:** La función lanza `NotImplementedError`. Implementa la función y vuelve a ejecutar el test.

---

## 💡 Debugging Avanzado

### Ver Mensajes Detallados con Prints

```bash
pytest tests/ -v -s
```

El flag `-s` permite ver los `print()` statements en tu código durante la ejecución de tests.

---

### Ejecutar Solo un Test Específico

```bash
pytest tests/test_nivel_1_alfabeto.py::test_nivel_1_1_el_vacio_de_cartago -v
```

Útil cuando quieres enfocarte en un solo test fallido.

---

### Ver Traceback Completo

```bash
pytest tests/ -v --tb=long
```

Muestra el traceback completo de errores, útil para debugging complejo.

---

### Ver Solo Tests Fallidos

```bash
pytest tests/ --tb=no -q
```

Muestra solo el resumen de tests fallidos y pasados, sin traceback.

---

### Ejecutar Tests en un Archivo Específico

```bash
pytest tests/test_nivel_1_alfabeto.py
```

Ejecuta todos los tests en ese archivo específico.

---

## 🔄 Flujo de Trabajo Recomendado

### Por Nivel (Desarrollo)

1. **Implementar función** en el archivo correspondiente
2. **Correr tests del nivel:**
   ```bash
   pytest tests/test_nivel_X*.py -v
   ```
3. **Si fallan:**
   - Revisar el test específico que falló
   - Leer el código del test para entender qué se espera
   - Corregir tu implementación
   - Volver al paso 2
4. **Cuando todos pasen:**
   - Verificar calidad de código: `ruff check calculadora/`
   - Corregir errores de ruff si hay
   - Commit: `git add . && git commit -m "feat: completar nivel X"`
5. **Continuar al siguiente nivel**

---

### Antes de Entregar (Final)

1. **Ejecutar todas las pruebas:**
   ```bash
   pytest tests/ -v
   ```
2. **Verificar que pasen los 82 tests**
3. **Verificar calidad de código:**
   ```bash
   ruff check calculadora/
   ```
4. **Probar el CLI para pruebas manuales:**
   ```bash
   python3 -m calculadora
   ```
5. **Probar expresiones de ejemplo:**
   ```
   🏛 > XIV + LX
   Resultado: 74
   ```
6. **Commit final:**
   ```bash
   git add .
   git commit -m "feat: práctica completa - todos los niveles implementados"
   ```
7. **Push a GitHub:**
   ```bash
   git push
   ```

---

## ❓ Errores Comunes y Soluciones

### ImportError

```
ModuleNotFoundError: No module named 'calculadora'
```

**Solución:**
- Ejecuta tests desde la raíz del proyecto (donde está `README.md`)
- No ejecutes tests desde dentro de la carpeta `tests/`

---

### AttributeError

```
AttributeError: 'NoneType' object has no attribute '...'
```

**Solución:**
- Verifica que tu función retorne algo (no termines sin return)
- Verifica que no estés retornando `None` explícitamente

---

### AssertionError

```
AssertionError: assert False == True
AssertionError: assert 5 == 10
```

**Solución:**
- Revisa la lógica de tu función
- Verifica qué valor está retornando vs qué valor se espera
- Imprime valores intermedios con `print()` para debugging

---

### NotImplementedError

```
NotImplementedError
```

**Solución:**
- Implementa la función (actualmente solo tiene `raise NotImplementedError()`)
- Revisa el docstring para entender qué debe hacer la función

---

### ExpresionInvalida (en Nivel 6)

```
ExpresionInvalida: La cadena 'IIII' viola las reglas de repetición
```

**Solución:**
- En Nivel 6, primero llamas a las validaciones anteriores
- Si alguna falla, lanza `ExpresionInvalida` con mensaje descriptivo
- Verifica que todas las validaciones estén implementadas correctamente

---

## 📊 Métricas de Progreso

### Inicio (sin implementar)

```
============================ test session starts =============================
collected 82 items

tests/test_nivel_1_alfabeto.py::test_nivel_1_1_el_vacio_de_cartago ERROR
tests/test_nivel_1_alfabeto.py::test_nivel_1_2_la_invasion_barbara ERROR
...

========================= 0 passed, 82 errors in X.XXs =====================
```

**Interpretación:**
- 0 passed: Ningún test pasa
- 82 errors: Todas las funciones lanzan `NotImplementedError`

---

### Medio (algunos niveles completados)

```
============================ test session starts =============================
collected 82 items

tests/test_nivel_1_alfabeto.py::test_nivel_1_1_el_vacio_de_cartago PASSED
...
tests/test_nivel_5_restas.py::test_nivel_5_1_seis_pares_validos PASSED
tests/test_nivel_6_conversor.py::test_nivel_6_1_basicos_romano_a_entero ERROR
...

========================= 46 passed, 30 errors in X.XXs =====================
```

**Interpretación:**
- 46 passed: Niveles 1-5 completados
- 30 errors: Niveles 6-8 no implementados
- Progreso: ~60%

---

### Final (práctica completa)

```
============================ test session starts =============================
collected 82 items

tests/test_nivel_1_alfabeto.py::test_nivel_1_1_el_vacio_de_cartago PASSED
...

========================= 82 passed in X.XXs =====================
```

**Interpretación:**
- 82 passed: Todos los tests funcionales pasan
- Progreso: 100% ✅

---

## 🚨 Verificación de Calidad de Código

Además de las pruebas funcionales, debes verificar la calidad de tu código:

```bash
ruff check calculadora/
```

**Resultado esperado (sin errores):**
```
All checks passed!
```

**Nota:** La verificación de calidad de código se ejecuta automáticamente en GitHub Actions como parte de la evaluación (30 puntos del total).

**Si hay errores:**
```
calculadora/conversor.py:25:5: B006 Do not use mutable data structures
calculadora/parser.py:10:23: N802 Function name should be lowercase
...
Found 3 errors.
```

**Solución:**
1. Ejecuta autocorrección: `ruff check calculadora/ --fix`
2. Revisa los errores restantes
3. Corrige manualmente según la guía en `docs/GUIA_RUFF.md`
4. Vuelve a verificar: `ruff check calculadora/`

---

## ✅ Checklist Antes de Commit y Push

Antes de hacer `git commit` y `git push`, verifica:

- [X] Todos los niveles implementados (1-8)
- [X] `pytest tests/ -v` muestra **82 passed**
- [X] `ruff check calculadora/` muestra **All checks passed!**
- [X] `python3 -m calculadora` funciona (REPL)
- [X] Probé expresiones de ejemplo en el REPL
- [X] Revisé el diff de git para confirmar cambios
- [X] Commit con mensaje claro: `git commit -m "feat: descripción"`
- [X] Push a GitHub: `git push`

---

## 📚 Recursos Adicionales

- **Especificación completa:** `docs/PRACTICA.md`
- **Guía de ruff:** `docs/GUIA_RUFF.md`
- **Teoría:** `docs/NOTAS_DE_CLASE.pdf`
- **Documentación de pytest:** https://docs.pytest.org/

---

**Versión:** 1.0
**Fecha:** Marzo 2026
**Proyecto:** Unidad 1 - Lenguajes y Autómatas I
