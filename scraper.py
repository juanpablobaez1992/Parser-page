import requests
from bs4 import BeautifulSoup

class CatholicNewsScraper:
    """Simple scraper for Catholic news websites."""

    def __init__(self, url: str):
        self.url = url

    def get_articles(self):
        """Return a list of articles with title and link."""
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        articles = []
        for art in soup.select("article"):
            title_tag = art.find(["h1", "h2", "h3"])
            link_tag = art.find("a", href=True)
            if title_tag and link_tag:
                articles.append({
                    "title": title_tag.get_text(strip=True),
                    "link": link_tag["href"],
                })
        return articles

    def parse_article(self, article_url: str):
        """Fetch and parse a single article to extract text."""
        res = requests.get(article_url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
        return "\n".join(paragraphs)
