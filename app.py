import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from urllib.parse import urljoin
import time

app = Flask(__name__)


# --- TOOL 1: Text & Table Scraper ---
def scrape_text_logic(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        paragraphs = [p.get_text().strip() for p in soup.find_all('p') if p.get_text().strip()]
        return "\n\n".join(paragraphs) if paragraphs else "No text found."
    except Exception as e:
        return f"Error: {str(e)}"


# --- TOOL 2: Document Finder ---
def fetch_docs_logic(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        docs = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if any(href.lower().endswith(ext) for ext in ['.pdf', '.docx', '.txt', '.csv']):
                full_url = urljoin(url, href)
                docs.append(f"File: {link.text.strip() or 'Download'} -> {full_url}")

        return "\n".join(docs) if docs else "No documents found."
    except Exception as e:
        return f"Error: {str(e)}"


# --- ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scrape_text', methods=['POST'])
def scrape_text_route():
    url = request.form.get('url_input')
    result = scrape_text_logic(url)
    return render_template('index.html', content=result, url=url, active_tab='text')


@app.route('/fetch_docs', methods=['POST'])
def fetch_docs_route():
    url = request.form.get('url_input')
    result = fetch_docs_logic(url)
    return render_template('index.html', content=result, url=url, active_tab='docs')


if __name__ == '__main__':
    app.run(debug=True)