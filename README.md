# Proyecto Final Python
#### Tipti
##### Nombre: Nathalia Estefanía Cóndor Flores
##### Correo: natis.nti@gmail.com

# Proyecto de Análisis de Datos

## Descripción

Este proyecto consiste en la carga, limpieza y análisis de datos de productos. Incluye la recopilación de datos de una página web, su procesamiento y visualización de estadísticas básicas.

## Estructura del Proyecto

├── data/
│   ├── processed/
│   │   └── cleaned_products.csv
│   └── raw/
│       └── products.csv
├── notebooks/
│   └── exploration.ipynb
├── src/
│   ├── analysis/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── analysis.py
│   ├── decorators/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── decorators.py
│   └── scraping/
│       ├── __init__.py
│       └── scraper.py
├── dep.txt
└── README.md


## Explicación del Código
-src/analysis/analysis.py
Este archivo contiene funciones para cargar, limpiar y analizar los datos.

-src/decorators/decorators.py
Este archivo contiene los decoradores timeit y logit para medir el tiempo de ejecución y registrar la ejecución de las funciones.

-src/scraping/scraper.py
Este archivo contiene funciones para recopilar datos de una página web utilizando requests y BeautifulSoup.

-notebooks/exploration.ipynb
Este notebook contiene análisis y visualizaciones adicionales de los datos limpios.
