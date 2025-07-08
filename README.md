# Parser Page

Este proyecto contiene un ejemplo sencillo de un *scraper* de noticias de sitios
católicos y una pequeña interfaz web para seleccionarlas y procesarlas.

## Requisitos

- Python 3.8+
- Dependencias: `Flask`, `requests`, `beautifulsoup4`

Para instalarlas se puede ejecutar:

```bash
pip install flask requests beautifulsoup4
```

## Uso

1. Arrancar la aplicación web ejecutando:
   ```bash
   python webapp.py
   ```
2. Abrir un navegador en `http://localhost:5000`.
3. Se mostrarán las noticias extraídas de los sitios definidos en `SCRAPE_URLS`.
4. Seleccione las noticias que desee procesar y pulse "Parsear seleccionadas".

El código del *scraper* se encuentra en `scraper.py` y se puede adaptar para
soportar más páginas o cambiar la forma de obtener la información.
