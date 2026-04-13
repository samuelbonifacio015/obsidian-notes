---
tags: [upc, ciclo-6, estadistica-aplicada, apuntes, graficos, variables-cualitativas, diagrama-pareto]
fecha: 2026-04-13
tema: Representación Gráfica de Variables Cualitativas
curso: Estadística Aplicada I
---

# 📊 Representación Gráfica de Variables Cualitativas

Cuando trabajamos con variables **cualitativas** (nominales u ordinales), los gráficos nos permiten visualizar la distribución de frecuencias de las categorías de forma intuitiva.

---

## 1. Gráfico de Barras

> Las categorías se ubican en el **eje horizontal** y las **frecuencias** (absolutas `fi`, relativas `hi` o porcentuales `pi`) en el **eje vertical**.

- Cada barra tiene una altura proporcional a la frecuencia de la categoría
- Las barras deben tener el **mismo ancho** y estar **separadas** entre sí
- Sirve tanto para variables **nominales** como **ordinales**

**Ejemplo:** Si graficamos el número de alumnos por carrera (Ing. Software = 30, Medicina = 45, Derecho = 25):

```
  pi (%)
  50 |         ████
  40 |         ████
  30 |  ████   ████   ████
  20 |  ████   ████   ████
  10 |  ████   ████   ████
   0 +--------------------
        Ing.S   Med    Der
```

> **Tip examen:** Si te piden graficar una variable **ordinal**, usa SIEMPRE gráfico de barras (nunca circular), porque el orden se pierde en el círculo.

---

## 2. Gráfico Circular (Pie Chart / Pastel)

> Un círculo se divide en **sectores** cuyo ángulo (y área) es **proporcional** a la frecuencia que representa cada categoría.

- Cada sector = una categoría
- El ángulo de cada sector = `(fi / n) × 360°`
- Se recomienda usar cuando hay **pocas categorías** (máximo 5-6)
- Cada sector puede etiquetarse con el porcentaje

**Cuándo usarlo:**
- ✅ Variable **nominal** con pocas categorías
- ✅ Quieres mostrar proporciones de un todo

**Cuándo NO usarlo:**
- ❌ Variable **ordinal** (se pierde el orden)
- ❌ Muchas categorías (se vuelve ilegible)

> **Tip examen:** si la pregunta dice "ordinal" → gráfico de barras. Si dice "nominal con pocas categorías" → circular es aceptable.

---

## 3. Diagrama de Pareto ⭐

> El diagrama de Pareto es una representación gráfica que permite identificar y seleccionar los **aspectos prioritarios** de un problema. También se conoce como **diagrama ABC** o **Ley de las prioridades 80-20**.

### La Ley 80-20

> *"El 80% de los problemas que ocurren en cualquier actividad son ocasionados por el 20% de los elementos que intervienen en producirlos"*

Esto se resume como: **"pocos vitales, muchos triviales"**.

- De un problema con muchas causas → el **20% de las causas** resuelven el **80% del problema**
- Ejemplo clásico: en control de calidad, la mayoría de los defectos surgen de un **número pequeño de causas**

---

### Pasos para elaborar el Diagrama de Pareto

#### Paso 1: Construir tabla de distribución de frecuencias

Se ordenan las categorías en forma **descendente** respecto a la frecuencia.

> ⚠️ **Regla de "Otros":** La categoría *Otros* se coloca **al final**, sin importar su tamaño, pues agrupa categorías cuyas frecuencias son menores que la frecuencia más pequeña listada individualmente.

**Tabla modelo:**

Distribución de `<unidades elementales>` según `<variable>`

| Variable | Frecuencia absoluta `fi` | Frecuencia porcentual `pi` | Frec. acumulada porcentual `Pi` |
|----------|:------------------------:|:--------------------------:|:-------------------------------:|
| Categoría 1 | f1 | p1 | P1 |
| Categoría 2 | f2 | p2 | P2 |
| Categoría 3 | f3 | p3 | P3 |
| Otros | fk | pk | Pk |
| **Total** | **n** | **100%** | **100%** |

**Ejemplo práctico:** Defectos en una línea de producción (n = 200)

| Tipo de defecto | fi | pi | Pi |
|-----------------|:--:|:--:|:--:|
| Rayón | 80 | 40% | 40% |
| Abolladura | 50 | 25% | 65% |
| Color defectuoso | 30 | 15% | 80% |
| Otros | 40 | 20% | 100% |
| **Total** | **200** | **100%** | **100%** |

> 📌 Aquí el 20% de las causas (Rayón + Abolladura = 2 de 4 categorías) explican el 65% de los defectos → **pocos vitales**.

---

#### Paso 2: Dibujar los ejes

Se necesitan **tres ejes**:

| Eje | Posición | Qué muestra | Escala recomendada |
|-----|----------|-------------|-------------------|
| Vertical izquierdo | Izquierda | Frecuencias simples (`fi`, `hi` o `pi`) | Si usas `fi`: de 0 a `n`; si usas `hi`: de 0 a 1; si usas `pi`: de 0% a 100% |
| Vertical derecho | Derecha | Frecuencias acumuladas (`Fi`, `Hi` o `Pi`) | Se recomienda `Pi`: de 0% a 100% |
| Horizontal | Abajo | Categorías (barras) | Espacios para cada categoría, incluyendo *Otros* |

```
  fi (izq.)                        Pi (der.)
     |                                |
   n |                                | 100%
     |                                |
     |                                |
     |                                |
     |                                |
   0 +--------------------------------+ 0%
     [Cat.1] [Cat.2] [Cat.3] [Otros]
```

---

#### Paso 3: Graficar el diagrama de barras

- Las barras se ordenan de **mayor a menor** frecuencia
- La categoría *Otros* va **siempre al final**
- Las barras representan las frecuencias simples (`fi` o `pi`) del eje izquierdo

```
  fi                           Pi
 80 |████                        | 100%
    |████    80                  |
 60 |████    ████                |  80%
    |████    ████   50           |     ●65%
 40 |████    ████   ████         |  60%   ●
    |████    ████   ████   40    |        │●80%
 20 |████    ████   ████   ████  |  40%   │  ●
    |████ 0% ████   ████   ████  |        │    ●100%
  0 +----------------------------+  0%
     Rayón  Aboll. Color  Otros
```

---

#### Paso 4: Dibujar la curva de Pareto

- Se traza una **línea** que conecta los puntos de la **frecuencia acumulada porcentual** (`Pi`)
- Se recomienda agregar **etiquetas de datos** tanto en las barras como en la curva
- La curva usa el **eje vertical derecho**

**Elementos finales del gráfico:**

| Elemento | Descripción |
|----------|-------------|
| Título | "Distribución de `<unidades>` según `<variable>`" |
| Eje vertical izquierdo | Frecuencia simple (barras) |
| Eje vertical derecho | Frecuencia acumulada porcentual (curva) |
| Eje horizontal | Categorías ordenadas |
| Barras | Frecuencias simples |
| Curva (línea) | Frecuencias acumuladas (curva de Pareto) |
| Fuente | De dónde provienen los datos |

> **Tip examen:** Si te piden hacer un Pareto, recuerda el orden: **1)** tabla ordenada descendente, **2)** ejes con doble escala, **3)** barras de mayor a menor, **4)** curva acumulada. "Otros" siempre al final.

---

## 4. Cheatsheet rápido para examen

```
¿Qué gráfico usar para variable cualitativa?
├── ¿Variable ordinal?                → Gráfico de BARRAS (siempre)
├── ¿Variable nominal con pocas cat.? → Gráfico CIRCULAR o de BARRAS
├── ¿Identificar causas prioritarias? → Diagrama de PARETO
└── ¿Mostrar proporciones de un todo? → Gráfico CIRCULAR

Pareto: clave para examen
├── Ley 80-20: 20% causas → 80% problemas
├── Tabla: orden DESCENDENTE, "Otros" al FINAL
├── Ejes: izq. = frecuencia simple, der. = acumulada %
├── Barras: de mayor a menor
└── Curva: línea de frecuencia acumulada porcentual
```

---

*Fuente: Estadística Aplicada I — UPC 2026*
*Referencia: Cuaderno de trabajo MA642, 2026*
