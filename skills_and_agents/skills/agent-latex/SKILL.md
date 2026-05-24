---
name: agent-latex
description: >
  Elabora documentos académicos, tesis y artículos científicos en formato LaTeX
  con estilos IEEE y APA 7ma edición. Trigger: Cuando el usuario pide crear un
  documento científico, tesis, artículo, reporte con formato IEEE o APA, o
  necesita estructurar una tesis o documento académico en LaTeX.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: 1.0
---

## When to Use

- Crear artículos científicos en formato IEEE
- Redactar tesis con formato APA 7ma edición
- Generar reportes técnicos con estilo académico
- Estructurar documentos LaTeX con normas APA/IEEE
- Crear bibliografías y citas automáticas en LaTeX

## Critical Patterns

### Estructura IEEE

```
IEEEtran.cls - Clase oficial IEEE para LaTeX
- twocolumn, conference/article
- Keywords en mayúscula
- Ecuaciones centradas con número a la derecha
- Tablas con caption arriba, figuras con caption abajo
- Referencias numeradas correlativamente
```

### Estructura APA 7ma Edición

```
- Profundidad de autor única: Apellido, Inicial. (Año).
- Más de 3 autores: Apellido, A. A., & Apellido, B. B.
- DOI como hyperlink
- Tablas con caption arriba
- Figuras con caption abajo
- Sangría francesa en párrafos (0.5 pulgadas)
```

### Formato de Documento

| Elemento | IEEE | APA 7ma |
|----------|------|---------|
| Títulos | Uppercase, centered | Capitalize first letter |
| Autores | Abajo del título | Página título + cuerpo |
| Abstract | 150-250 palabras | 150-250 palabras, estructura |
| Keywords | After abstract | After abstract |
| Referencias | Numéricas [] | Alfabética, hanging indent |
| Citas | [1], [1]-[3] | (Apellido, Año) |

## Comandos Comunes

```bash
# Compilar documento LaTeX
pdflatex documento.tex
biber documento  # Para bibliografía
pdflatex documento.tex

# Visualizar
latex documento.tex && dvipdf documento.dvi
```

## Estructura de Tesis/Artículo

### Plantilla IEEE Article

```latex
%\title{Título del Artículo}
%\titleblock{
%  \thanks{Identificador de patrocinio}
%}
%\begin{document}
%\begin{frontmatter}
%\title{Título}
%\begin{authorblock}
%  \name Autor 1\thanks{Institución}
%  \name Autor 2
%\\end{authorblock}
%\begin{abstract}
% Resumen de 150-250 palabras.
%\begin{keywords}
% Palabra clave 1, Palabra clave 2, Palabra clave 3
%\begin{IEEEkeywords}
%\textbf{---} Sección \textbf{I.} Introducción
%\textbf{---} Sección II. Fondo Teórico
%\textbf{---} Sección III. Metodología
%\textbf{---} Sección IV. Resultados
%\textbf{---} Sección V. Discusión
%\textbf{---} Sección VI. Conclusión
%\textbf{---} Referencias
%\begin{thebibliography}{00}
%\bibitem{ref1} Autor, ``Título,'' Revista, vol. 1, pp. 1-10, 2024.
%\begin{thebibliography}
```

### Plantilla APA 7ma Edición

```latex
%\title{Título}
%\begin{document}
%\begin{center}
%  \textbf{Título de la Investigación}
%  \\[12pt]
%  \textit{Autor 1}^{1}, \textit{Autor 2}^{2}
%  \\[6pt]
%  $^{1}$Universidad, Departamento
%  $^{2}$Universidad, Departamento
%\newpage
%\textbf{Abstract}
% Resumen estructurado: contexto, objetivo, método, resultados, conclusión.
%\\[12pt]
% \textbf{Keywords:} palabra, palabra, palabra
%\newpage
%\textbf{Introducción} (Título centrado, negrita)
%
% Desarrollo con citas (Apellido, Año)
%
%\textbf{Referencia en hanging indent:}
% Apellido, A. A. (Año). Título del artículo. Revista, vol(issue), páginas. https://doi.org/xxxxx
```

## Assets Disponibles

- **IEEE Article Template**: [assets/ieee-article.tex](assets/ieee-article.tex)
- **APA 7th Edition Template**: [assets/apa7-thesis.tex](assets/apa7-thesis.tex)
- **IEEE Conference Template**: [assets/ieee-conference.tex](assets/ieee-conference.tex)

## Recursos

- Documentación IEEE LaTeX: references/ieee latex guide
- Guía APA 7ma: references/apa7-guide