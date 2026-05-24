# Guía de Referencia IEEE LaTeX

## Clase IEEEtran

La clase `IEEEtran.cls` es la clase oficial IEEE para LaTeX. Proporciona
formatos para artículos de revista y conferencias.

### Opciones de documento

```latex
\documentclass[conference, a4paper]{IEEEtran}  % Conferencia
\documentclass[journal, a4paper]{IEEEtran}      % Revista
\documentclass[technote, a4paper]{IEEEtran}    % Nota técnica
```

## Estructura del Artículo IEEE

### Título

```latex
\title{Título en Mayúsculas}
```

### Bloque de Autores

```latex
\author{
   ~\IEEEauthorblockN{Autor 1\IEEEauthorrefmark{1}}
    \IEEEauthorblockA{\IEEEauthorrefmark{1}Afiliación}
    \and
    ~\IEEEauthorblockN{Autor 2\IEEEauthorrefmark{2}}
    \IEEEauthorblockA{\IEEEauthorrefmark{2}Afiliación}
}
```

## Secciones

Las secciones se numeran correlativamente con números romanos:

```latex
\section{I. Introducción}
\section{II. Marco Teórico}
\section{III. Metodología}
\section{IV. Resultados}
\section{V. Discusión}
\section{VI. Conclusión}
```

### Subsecciones

Las subsecciones usan letras mayúsculas:

```latex
\subsection{A. Contexto}
\subsection{B. Problemática}
```

## Tablas

- Caption **arriba** de la tabla
- Borde horizontal superior con `toprule`
- Borde horizontal inferior con `bottomrule`
- Líneas internas con `midrule`

```latex
\begin{table}[htbp]
\centering
\caption{Resultados del Análisis}
\label{tab:resultados}
\begin{tabular}{lcc}
\toprule
Variable & Valor & Error \\
\midrule
X & 10.5 & 0.3 \\
Y & 20.2 & 0.5 \\
\bottomrule
\end{tabular}
\end{table}
```

## Figuras

- Caption **abajo** de la figura
- Centradas horizontalmente
- Etiqueta de referencia después del caption

```latex
\begin{figure}[htbp]
\centering
%\includegraphics[width=3in]{figura}
\caption{Descripción de la figura}
\label{fig:resultado}
\end{figure}
```

## Ecuaciones

Ecuaciones centradas con número a la derecha:

```latex
\begin{equation}
    E = mc^2
    \label{eq:einstein}
\end{equation}
```

Ecuaciones sin número:
```latex
\begin{equation*}
    E = mc^2
\end{equation*}
```

## Citas y Referencias

### Citas en texto

- Una referencia: `[1]`
- Múltiples referencias: `[1]-[3]` o `[1], [2], [3]`

```latex
Según el estudio~\cite{referencia1}
Los resultados demuestran que...~\cite[Cap. 2]{referencia2}
```

### Lista de referencias

```latex
\begin{thebibliography}{00}
 bibitem{referencia1}
 A.~Autor, ``Título del artículo,'' \emph{Revista}, vol. 1, núm. 1, pp. 1-10, 2024.
\end{thebibliography}
```

## Formato de Referencias

### Artículo de revista

```latex
A.~Autor, ``Título del artículo,'' \emph{Revista}, vol. 1, núm. 1, pp. 1-10, 2024.
```

### Libro

```latex
A.~Autor, \emph{Título del libro}, 2.$^a$ ed. Ciudad: Editorial, 2023.
```

### Ponencia en conferencia

```latex
A.~Autor, ``Título de la ponenci,'' en \emph{Proc. Nombre Conferencia}, 2023, pp. 1-5.
```

### Tesis

```latex
A.~Autor, ``Título de la tesis,'' Ph.D. dissertation, Universidad, Ciudad, 2023.
```

### Página web

```latex
A.~Autor. (2024). Título de la página. [En línea]. Disponible: https://ejemplo.com
```

## Keywords

Se colocan después del abstract, en mayúsculas, precedidas de "Abstract---":

```latex
\begin{IEEEkeywords}
Palabra clave 1, Palabra clave 2, keyword3
\end{IEEEkeywords}
```

## Agradecimientos

```latex
\section*{Agradecimientos}
Los agradecimientos a instituciones o personas.
```