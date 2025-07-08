from flask import Flask, render_template_string, request
from scraper import CatholicNewsScraper

app = Flask(__name__)

# Example Catholic news sites. Feel free to adjust or add your own.
SCRAPE_URLS = [
    "https://www.vaticannews.va/es.html",
]

HTML_TEMPLATE = """
<!doctype html>
<title>Noticias Católicas</title>
<h1>Noticias Católicas</h1>
<form method="post">
    {% for art in articles %}
    <div>
        <input type="checkbox" name="article" value="{{ art.link }}">
        <a href="{{ art.link }}" target="_blank">{{ art.title }}</a>
    </div>
    {% endfor %}
    <button type="submit">Parsear seleccionadas</button>
</form>

{% if selected %}
<h2>Artículos seleccionados</h2>
<ul>
{% for url, text in selected %}
    <li><strong>{{ url }}</strong><pre>{{ text[:200] }}...</pre></li>
{% endfor %}
</ul>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    articles = []
    selected = []
    if request.method == 'POST':
        for url in request.form.getlist('article'):
            scraper = CatholicNewsScraper(url)
            text = scraper.parse_article(url)
            selected.append((url, text))
    else:
        for url in SCRAPE_URLS:
            scraper = CatholicNewsScraper(url)
            articles.extend(scraper.get_articles())
    return render_template_string(HTML_TEMPLATE, articles=articles, selected=selected)
if __name__ == '__main__':
    app.run(debug=True)
