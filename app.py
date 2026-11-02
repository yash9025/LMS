from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Sample in-memory book database
books = [
    {"id": 1, "title": "Fluent Python", "author": "Luciano Ramalho", "isbn": "978-1491952443", "available": True},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin", "isbn": "978-0132350884", "available": True},
    {"id": 3, "title": "Design Patterns", "author": "Erich Gamma et al.", "isbn": "978-0201633610", "available": False},
    {"id": 4, "title": "Introduction to Algorithms", "author": "Thomas H. Cormen", "isbn": "978-0262033848", "available": True},
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Library Management System</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f4f6f9; color: #333; }
        h1 { color: #2c3e50; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background: #34495e; color: white; }
        .badge { padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; }
        .available { background: #2ecc71; color: white; }
        .borrowed { background: #e74c3c; color: white; }
        input[type="text"] { padding: 8px; width: 300px; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 8px 16px; background: #3498db; color: white; border: none; border-radius: 4px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>📚 Library Management System (LMS)</h1>
    <div class="card">
        <form method="get" action="/">
            <input type="text" name="q" placeholder="Search by title or author..." value="{{ query }}">
            <button type="submit">Search</button>
            {% if query %}<a href="/" style="margin-left: 10px;">Clear</a>{% endif %}
        </form>
    </div>
    <div class="card">
        <h2>Book Catalog</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>Title</th>
                <th>Author</th>
                <th>ISBN</th>
                <th>Status</th>
            </tr>
            {% for b in books %}
            <tr>
                <td>{{ b.id }}</td>
                <td>{{ b.title }}</td>
                <td>{{ b.author }}</td>
                <td>{{ b.isbn }}</td>
                <td>
                    {% if b.available %}
                        <span class="badge available">Available</span>
                    {% else %}
                        <span class="badge borrowed">Borrowed</span>
                    {% endif %}
                </td>
            </tr>
            {% else %}
            <tr><td colspan="5">No books found matching your query.</td></tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    query = request.args.get("q", "").strip().lower()
    if query:
        filtered = [b for b in books if query in b["title"].lower() or query in b["author"].lower()]
    else:
        filtered = books
    return render_template_string(HTML_TEMPLATE, books=filtered, query=query)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "Library Management System",
        "total_books": len(books)
    }), 200

@app.route("/books", methods=["GET"])
def get_books():
    query = request.args.get("q", "").strip().lower()
    if query:
        filtered = [b for b in books if query in b["title"].lower() or query in b["author"].lower()]
        return jsonify(filtered), 200
    return jsonify(books), 200

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json(silent=True) or request.form
    if not data or not data.get("title") or not data.get("author"):
        return jsonify({"error": "Title and author are required"}), 400
    
    new_book = {
        "id": len(books) + 1,
        "title": data.get("title"),
        "author": data.get("author"),
        "isbn": data.get("isbn", "N/A"),
        "available": True
    }
    books.append(new_book)
    return jsonify({"message": "Book added successfully", "book": new_book}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

