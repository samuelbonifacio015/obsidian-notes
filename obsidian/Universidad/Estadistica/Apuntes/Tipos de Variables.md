---
tags:
  - upc
  - ciclo-6
  - estadistica-aplicada
  - apuntes
  - variables
  - escalas-de-medicion
fecha: 2026-04-13
tema: Tipos de Variables y Escalas de Medición
curso: Estadística Aplicada I
---

# 📊 Variables y Escalas de Medición

## 1. Tipos de Variables

Una **variable** es cualquier característica o atributo que se mide en una unidad estadística.

```
Variable
├── Cualitativa (categórica)
└── Cuantitativa
    ├── Discreta
    └── Continua
```

---

### 🏷️ Variable Cualitativa

> Resultado de la medición = **etiqueta / nombre**

- No tiene sentido matemático operar con ella
- Ejemplos: lugar de nacimiento, carrera estudiada, grado de instrucción

**Analogía Braymar:** el campo `categoria_producto` ("cuadernos", "lapiceros", "mochilas") → es cualitativa, no puedes promediar categorías.

---

### 🔢 Variable Cuantitativa

> Resultado de la medición = **número** con significado matemático

#### Discreta
- Valores **finitos o infinitos numerables** dentro de un intervalo
- Solo toma ciertos valores concretos (enteros, generalmente)
- Ejemplos: n° de capacitaciones, n° de trabajos anteriores

#### Continua
- Valores **infinitos no numerables** — puede tomar **cualquier valor** en un intervalo
- Ejemplos: tiempo de traslado (min), salario (S/), peso (kg)

**Analogía real:**
| Tipo | Ejemplo tech |
|------|-------------|
| Discreta | Número de requests fallidas en un deploy |
| Continua | Latencia promedio de la API de Braymar (ms) |

---

### Tabla resumen — Tipos de Variables

| Variable | Tipo | Ejemplo |
|----------|------|---------|
| Lugar de nacimiento | Cualitativa | Lima, Cusco |
| N° de capacitaciones | Cuantitativa discreta | 0, 1, 2, 3... |
| Salario actual (S/) | Cuantitativa continua | 2500.50, 3800.00 |
| Carrera estudiada | Cualitativa | Ing. Software, Medicina |
| Tiempo de traslado (min) | Cuantitativa continua | 14.7, 32.0 |

---

## 2. Escalas de Medición

Otra forma de clasificar variables — importa porque **determina qué operaciones estadísticas son válidas**.

```
Escalas
├── Nominal   → solo clasificar
├── Ordinal   → clasificar + ordenar
├── Intervalo → clasificar + ordenar + diferencias iguales (cero relativo)
└── Razón     → todo lo anterior + cero absoluto (ausencia real)
```

---

### 🔵 Nominal

- Solo **clasifica en categorías**, sin orden entre ellas
- Si se usa número, es pura etiqueta (no matemático)
- Operaciones válidas: contar, moda

> Ejemplos: número de celular, marca de equipo, nombre de carrera

**Tip examen:** si puedes reordenar las categorías sin perder sentido → es nominal.

---

### 🟡 Ordinal

- Clasifica **y** permite ordenar (jerarquía: mayor/menor que)
- Las **diferencias entre categorías no son iguales ni medibles**
- Operaciones válidas: moda, mediana, percentiles

> Ejemplos: grado militar (general > coronel > comandante), talla de bebida (grande > mediana > pequeña), nivel de satisfacción (alto/medio/bajo)

**Tip examen:** hay orden claro pero no sabes cuánto más es uno que otro → ordinal.

---

### 🟠 Intervalo

- Mide cuantitativamente, diferencias **iguales = cantidades iguales**
- **Cero es relativo** — no indica ausencia de la característica
- Operaciones válidas: suma, resta, media, desviación estándar

> Ejemplos: temperatura en °C (0°C no es ausencia de temperatura), año de fabricación (año 0 no es "sin año")

**Tip examen:** ¿tiene cero pero ese cero no significa "nada"? → intervalo.

---

### 🟢 Razón

- Todo lo de intervalo **+** cero absoluto (ausencia real del atributo)
- Operaciones válidas: todas, incluidos cocientes (el doble de X tiene sentido)

> Ejemplos: peso (kg), longitud (m), salario (S/), tiempo de vida útil (años), kilometraje

**Tip examen:** ¿0 significa literalmente que no hay nada? → razón.

---

### Tabla resumen — Escalas

| Escala | Clasificar | Ordenar | Dif. iguales | Cero absoluto |
|--------|:----------:|:-------:|:------------:|:-------------:|
| Nominal | ✅ | ❌ | ❌ | ❌ |
| Ordinal | ✅ | ✅ | ❌ | ❌ |
| Intervalo | ✅ | ✅ | ✅ | ❌ |
| Razón | ✅ | ✅ | ✅ | ✅ |

---

## 3. Parámetros y Estadísticos

> Para entender estos conceptos, primero hay que distinguir entre **población** y **muestra**:
> - **Población:** Conjunto total de todas las unidades (personas, objetos, eventos) que comparten una característica y sobre las cuales se quiere estudiar algo.
> - **Muestra:** Subconjunto representativo extraído de la población, usado cuando no es posible o práctico estudiar a toda la población.

---

### 📐 Parámetro

> Medida que describe una característica resumen de las unidades que componen una **población**.

- Es un valor **fijo** (no cambia), pero generalmente **desconocido** (no se puede calcular porque no se tiene acceso a toda la población)
- Se representa con letras **griegas**: μ, σ², σ, P, N
- Ejemplo: El salario promedio de TODOS los egresados de la UPC → **μ** (media poblacional)

---

### 📐 Estadístico

> Medida que describe una característica resumen de las unidades que componen una **muestra**.

- Es un valor que **varía** según la muestra seleccionada (distinta muestra → distinto estadístico)
- Se usa para **estimar** el parámetro correspondiente
- Se representa con letras **latinas**: x̄, s², s, p̂, n
- Ejemplo: El salario promedio de 200 egresados seleccionados → **x̄** (media muestral)

---

### Tabla comparativa — Notación

| Medida | Parámetro (población) | Estadístico (muestra) |
|--------|----------------------|----------------------|
| Media | μ (mu) | x̄ (x barra) |
| Varianza | σ² (sigma cuadrado) | s² |
| Desviación estándar | σ (sigma) | s |
| Proporción | P | p̂ (p sombrero) |
| Tamaño | N | n |

---

### Ejemplo práctico

> **Situación:** Queremos conocer la edad promedio de todos los estudiantes de la UPC (población = 30,000 alumnos).

| Escenario | Qué calculamos | Tipo | Notación |
|-----------|---------------|------|----------|
| Encuestamos a los 30,000 alumnos | Edad promedio de TODOS | Parámetro | μ = 22.4 años |
| Encuestamos a 500 alumnos | Edad promedio de la muestra | Estadístico | x̄ = 21.8 años |

> ⚠️ **Clave:** El estadístico (x̄ = 21.8) es nuestra **estimación** del parámetro (μ = 22.4). Si tomáramos otra muestra de 500, probablemente daría un x̄ distinto.

---

**Tip examen:** Si te preguntan si un valor es parámetro o estadístico, identifica primero: **¿se midió a TODA la población?** → Sí = parámetro. ¿Se midió solo una parte? → Estadístico.

---

## 4. Ejercicio Resuelto (Ejemplo 3)

| Variable | Tipo | Escala |
|----------|------|--------|
| Número de celular | Cualitativa | Nominal |
| Longitud de cable de fibra óptica (m) | Cuantitativa continua | Razón |
| Marca de medidor láser (Bosch, Hilti…) | Cualitativa | Nominal |
| Tiempo de vida útil de laptop (años) | Cuantitativa continua | Razón |
| Peso de celular (kg) | Cuantitativa continua | Razón |
| Grado en el ejército | Cualitativa | Ordinal |
| Kilometraje de auto (km/año) | Cuantitativa continua | Razón |
| Tamaño de bebida (pequeña/mediana/grande) | Cualitativa | Ordinal |
| Año de fabricación de celular | Cuantitativa discreta | Intervalo |

> ⚠️ **Año de fabricación = Intervalo**, no Razón. El año 0 no significa "sin fabricación" — el cero es relativo.

---

## 5. Cheatsheet rápido para examen

```
¿Es número con sentido matemático?
├── NO  → Cualitativa
│         └── ¿Tiene orden? → Ordinal / Nominal
└── SÍ  → Cuantitativa
          ├── ¿Solo valores enteros/contables? → Discreta
          └── ¿Cualquier valor en un rango?   → Continua

¿Qué escala es?
├── Sin orden entre categorías         → Nominal
├── Con orden pero sin diferencia fija → Ordinal
├── Diferencias iguales, cero relativo → Intervalo
└── Diferencias iguales, cero absoluto → Razón
```

---

*Fuente: Estadística Aplicada I — UPC 2026, Semanas 1-2*
