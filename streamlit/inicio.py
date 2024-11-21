import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Optimización No Lineal", layout="wide")

# Título principal
st.title("Optimización No Lineal")

# Introducción
st.markdown("""
### Universidad Nacional del Altiplano  
**Facultad de Ingeniería Estadística e Informática**  
**Trabajo Encargado N°009: Optimización No Lineal**  
**Docente:** Fred Torres Cruz  
**Autor:** Heydi Pamela Manasaya Quispe  
**GitHub:** [PamelaManasayaQ](https://github.com/PamelaManasayaQ/optimizacion-no-lineal)  
""")

# Ejercicio 1
st.header("Ejercicio 1: Convexidad de $f(x) = 3x + 2$")
st.markdown("""
Demostrar que la función $f(x) = 3x + 2$ es convexa en $\\mathbb{R}$.

**Demostración paso a paso:**

1. Tomamos $x_1 = 1$ y $x_2 = 3$.
2. Elegimos $\\lambda = 0.5$.
3. Calculamos la combinación convexa:  
   \[
   x = \\lambda x_1 + (1 - \\lambda)x_2 = 0.5 \\cdot 1 + 0.5 \\cdot 3 = 2.
   \]
4. Evaluamos $f(x)$ en el punto intermedio:  
   \[
   f(x) = f(2) = 3 \\cdot 2 + 2 = 8.
   \]
5. Calculamos la combinación convexa de $f(x_1)$ y $f(x_2)$:  
   \[
   \\lambda f(x_1) + (1 - \\lambda)f(x_2) = 0.5 \\cdot 5 + 0.5 \\cdot 11 = 8.
   \]
6. Comparando resultados, se cumple $f(\\lambda x_1 + (1 - \\lambda)x_2) = \\lambda f(x_1) + (1 - \\lambda)f(x_2)$.

**Conclusión:**  
La función $f(x) = 3x + 2$ es convexa en $\\mathbb{R}$.
""")

# Ejercicio 2
st.header("Ejercicio 2: Verificar convexidad de $f(x) = x^3$")
st.markdown("""
Verificamos si la función $f(x) = x^3$ es convexa, cóncava o ninguna de las dos en el intervalo $[0, \\infty)$.

**Paso 1: Derivadas**  
Primera derivada:
\[
f'(x) = 3x^2
\]
Segunda derivada:
\[
f''(x) = 6x
\]

**Paso 2: Análisis de la segunda derivada**  
- Para $x \\geq 0$, se cumple $f''(x) \\geq 0$.

**Conclusión:**  
La función $f(x) = x^3$ es convexa en el intervalo $[0, \\infty)$.
""")

# Ejercicio 3
st.header("Ejercicio 3: Convexidad de $f(x) = e^{2x}$")
st.markdown("""
Demostrar que la función $f(x) = e^{2x}$ es convexa en $\\mathbb{R}$.

**Paso 1: Derivadas**  
Primera derivada:
\[
f'(x) = 2e^{2x}
\]
Segunda derivada:
\[
f''(x) = 4e^{2x}
\]

**Paso 2: Análisis de la segunda derivada**  
La segunda derivada $f''(x) = 4e^{2x}$ es siempre positiva para todo $x \\in \\mathbb{R}$.

**Conclusión:**  
La función $f(x) = e^{2x}$ es convexa en $\\mathbb{R}$ porque $f''(x) > 0$.
""")

# Ejercicio 4
st.header("Ejercicio 4: Concavidad de $f(x) = \\ln(x)$")
st.markdown("""
Analizamos la concavidad de la función $f(x) = \\ln(x)$ en el intervalo $(0, \\infty)$.

**Paso 1: Derivadas**  
Primera derivada:
\[
f'(x) = \\frac{1}{x}
\]
Segunda derivada:
\[
f''(x) = -\\frac{1}{x^2}
\]

**Paso 2: Análisis de la segunda derivada**  
La segunda derivada $f''(x) = -\\frac{1}{x^2}$ es siempre negativa en $(0, \\infty)$.

**Conclusión:**  
La función $f(x) = \\ln(x)$ es cóncava en $(0, \\infty)$ porque $f''(x) \\leq 0$.
""")

# Ejercicio 5
st.header("Ejercicio 5: Análisis de $f(x) = x^4 - 2x^2 + 1$")
st.markdown("""
Determinar los intervalos de convexidad, concavidad y puntos de inflexión de $f(x) = x^4 - 2x^2 + 1$.

**Paso 1: Derivadas**  
Primera derivada:
\[
f'(x) = 4x^3 - 4x
\]
Segunda derivada:
\[
f''(x) = 12x^2 - 4
\]

**Paso 2: Soluciones de $f''(x) = 0$**  
Igualamos:
\[
12x^2 - 4 = 0 \\quad \\Rightarrow \\quad x^2 = \\frac{1}{3} \\quad \\Rightarrow \\quad x = \\pm \\frac{1}{\\sqrt{3}}
\]

**Paso 3: Análisis de la segunda derivada**  
- Convexa en $(-\\infty, -\\frac{1}{\\sqrt{3}}) \\cup (\\frac{1}{\\sqrt{3}}, \\infty)$.
- Cóncava en $(-\\frac{1}{\\sqrt{3}}, \\frac{1}{\\sqrt{3}})$.

**Paso 4: Puntos de inflexión**  
Los puntos de inflexión ocurren en:
\[
\\left(-\\frac{1}{\\sqrt{3}}, f\\left(-\\frac{1}{\\sqrt{3}}\\right)\\right) \\quad \\text{y} \\quad \\left(\\frac{1}{\\sqrt{3}}, f\\left(\\frac{1}{\\sqrt{3}}\\right)\\right)
\]
Donde $f(x) = \\frac{4}{9}$ en ambos puntos.

**Conclusión:**  
- **Convexa en:** $(-\\infty, -\\frac{1}{\\sqrt{3}}) \\cup (\\frac{1}{\\sqrt{3}}, \\infty)$.  
- **Cóncava en:** $(-\\frac{1}{\\sqrt{3}}, \\frac{1}{\\sqrt{3}})$.  
- **Puntos de inflexión:** $\\left(-\\frac{1}{\\sqrt{3}}, \\frac{4}{9}\\right)$ y $\\left(\\frac{1}{\\sqrt{3}}, \\frac{4}{9}\\right)$.
""")

st.success("¡Todos los ejercicios completados!")
