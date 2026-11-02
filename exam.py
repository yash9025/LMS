from app import app, books

print("=== Running Library Management System Tests ===")
client = app.test_client()

# 1. Health check test
health_res = client.get("/health")
assert health_res.status_code == 200, f"Expected 200, got {health_res.status_code}"
print("✓ Health check endpoint working:", health_res.get_json())

# 2. Book list test
books_res = client.get("/books")
assert books_res.status_code == 200
data = books_res.get_json()
assert len(data) >= 4
print(f"✓ Book catalog retrieved ({len(data)} books found)")

# 3. Book search test
search_res = client.get("/books?q=Python")
assert search_res.status_code == 200
search_data = search_res.get_json()
assert any("Python" in b["title"] for b in search_data)
print("✓ Book search test passed (query='Python')")

print("=== All tests passed successfully! ===")
