from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def scrape_text(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        # Extracting all paragraphs and joining them into one block of text
        paragraphs = [p.get_text().strip() for p in soup.find_all('p')]
        return "\n\n".join(paragraphs)
    except Exception as e:
        return f"Error: Could not retrieve content. {str(e)}"


@app.route('/', methods=['GET', 'POST'])
def index():
    scraped_content = ""
    url_input = ""

    if request.method == 'POST':
        url_input = request.form.get('url_input')
        if url_input:
            scraped_content = scrape_text(url_input)

    return render_template('index.html', content=scraped_content, url=url_input)


if __name__ == '__main__':
    app.run(debug=True)