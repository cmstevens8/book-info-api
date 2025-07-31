from flask import Flask, request, jsonify
import requests
import urllib.parse

app = Flask(__name__)

@app.route('/book', methods=['GET'])
def get_book_info():
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Please provide a book title using the 'title' query parameter."}), 400

    encoded_title = urllib.parse.quote(title)
    url = f'https://openlibrary.org/search.json?title={encoded_title}'

    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch book data."}), 500

    data = response.json()
    if not data['docs']:
        return jsonify({"error": "No books found for that title."}), 404

    book = data['docs'][0]

    summary = {
        "title": book.get("title", "N/A"),
        "author": book.get("author_name", ["Unknown"])[0],
        "first_publish_year": book.get("first_publish_year", "Unknown"),
        "edition_count": book.get("edition_count", 0),
    }

    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)