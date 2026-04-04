# ============================================
# Task 1 — File Read & Write Basics
# ============================================

# Part A — Write
notes = [
    "Topic 1: Variables store data. Python is dynamically typed.\n",
    "Topic 2: Lists are ordered and mutable.\n",
    "Topic 3: Dictionaries store key-value pairs.\n",
    "Topic 4: Loops automate repetitive tasks.\n",
    "Topic 5: Exception handling prevents crashes.\n",
]

with open("python_notes.txt", "w", encoding="utf-8") as file:
    for line in notes:
        file.write(line)

print("File written successfully.")

with open("python_notes.txt", "a", encoding="utf-8") as file:
    file.write("Topic 6: Functions make code reusable and organized.\n")
    file.write("Topic 7: Modules allow importing pre-built code.\n")

print("Lines appended.")

# Part B — Read
print("\n--- File Contents ---")

with open("python_notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  

for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.strip()}")

# Count and print total number of lines
print(f"\nTotal lines in file: {len(lines)}")

# Ask user for keyword and search
print("\n--- Keyword Search ---")
keyword = input("Enter a keyword to search: ")

# Find all lines containing the keyword
# .lower() makes search case-insensitive
matching_lines = []

for line in lines:
    if keyword.lower() in line.lower():
        matching_lines.append(line.strip())

# Print results
if matching_lines:
    print(f"\nLines containing '{keyword}':")
    for match in matching_lines:
        print(f"  → {match}")
else:
    print(f"\nNo lines found containing '{keyword}'. Try a different keyword!")

# =====================================================================================
# Task 2 — API Integration
# =====================================================================================

import requests

# ============================================
# Step 1: Fetch and Display 20 Products
# ============================================
print("=" * 75)
print("Step 1 — Fetching 20 Products from DummyJSON API")
print("=" * 75)

# Make GET request to fetch 20 products
url      = "https://dummyjson.com/products?limit=20"
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data     = response.json()
    products = data["products"]
    print(f"✓ Successfully fetched {len(products)} products\n")
else:
    print(f"✗ Failed to fetch products. Status code: {response.status_code}")

# Print formatted table header
print(f"{'ID':<4} | {'Title':<30} | {'Category':<15} | {'Price':<9} | {'Rating'}")
print(f"{'-'*4}-|-{'-'*30}-|-{'-'*15}-|-{'-'*9}-|-{'-'*6}")

# Print each product
for product in products:
    pid      = product["id"]
    title    = product["title"][:28]   # trim long titles
    category = product["category"][:13] # trim long categories
    price    = f"${product['price']}"
    rating   = product["rating"]

    print(f"{pid:<4} | {title:<30} | {category:<15} | {price:<9} | {rating}")

# ============================================
# Step 2: Filter rating >= 4.5 and sort by
#         price descending
# ============================================
print("\n" + "=" * 75)
print("Step 2 — Products with Rating >= 4.5 (sorted by price descending)")
print("=" * 75)

# Filter products with rating >= 4.5
filtered = [p for p in products if p["rating"] >= 4.5]

# Sort by price descending
sorted_products = sorted(filtered, key=lambda p: p["price"], reverse=True)

print(f"Found {len(sorted_products)} products with rating >= 4.5\n")

# Print filtered and sorted table
print(f"{'ID':<4} | {'Title':<30} | {'Price':<9} | {'Rating'}")
print(f"{'-'*4}-|-{'-'*30}-|-{'-'*9}-|-{'-'*6}")

for product in sorted_products:
    pid    = product["id"]
    title  = product["title"][:28]
    price  = f"${product['price']}"
    rating = product["rating"]

    print(f"{pid:<4} | {title:<30} | {price:<9} | {rating}")

# ============================================
# Step 3: Search by Category — laptops
# ============================================
print("\n" + "=" * 75)
print("Step 3 — Laptops Category")
print("=" * 75)

# Make GET request for laptops category
laptop_url      = "https://dummyjson.com/products/category/laptops"
laptop_response = requests.get(laptop_url)

if laptop_response.status_code == 200:
    laptop_data     = laptop_response.json()
    laptops         = laptop_data["products"]

    print(f"✓ Found {len(laptops)} laptops\n")
    print(f"{'Name':<40} {'Price'}")
    print("-" * 50)

    for laptop in laptops:
        print(f"{laptop['title']:<40} ${laptop['price']}")
else:
    print("✗ Failed to fetch laptops")

# ============================================
# Step 4: POST Request — Add a new product
# ============================================
print("\n" + "=" * 75)
print("Step 4 — POST Request: Adding a New Product")
print("=" * 75)

# The product we want to add
new_product = {
    "title":       "My Custom Product",
    "price":       999,
    "category":    "electronics",
    "description": "A product I created via API"
}

# Send POST request
post_response = requests.post(
    "https://dummyjson.com/products/add",
    json=new_product
)

if post_response.status_code == 200 or post_response.status_code == 201:
    result = post_response.json()
    print("✓ Product created successfully!\n")
    print("Server Response:")
    print(f"  ID          : {result.get('id')}")
    print(f"  Title       : {result.get('title')}")
    print(f"  Price       : ${result.get('price')}")
    print(f"  Category    : {result.get('category')}")
    print(f"  Description : {result.get('description')}")
    print("\nNote: DummyJSON is a test API — no data is actually stored on the server.")
else:
    print(f"✗ POST request failed. Status code: {post_response.status_code}")

# ============================================
# Task 3 — Exception Handling
# ============================================

import requests

# ============================================
# Part A — Guarded Calculator
# ============================================
print("=" * 50)
print("Part A — Safe Divide")
print("=" * 50)

def safe_divide(a, b):
    try:
        result = a / b
        return result

    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

    except TypeError:
        return "Error: Invalid input types"

print(f"safe_divide(10, 2)      = {safe_divide(10, 2)}")
print(f"safe_divide(10, 0)      = {safe_divide(10, 0)}")
print(f"safe_divide('ten', 2)   = {safe_divide('ten', 2)}")

# ============================================
# Part B — Guarded File Reader
# ============================================
print("\n" + "=" * 50)
print("Part B — Safe File Reader")
print("=" * 50)

def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        print(f"✓ File '{filename}' read successfully!")
        return content

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

    finally:
        print("File operation attempt complete.")

print("\nTesting with python_notes.txt:")
content = read_file_safe("python_notes.txt")
if content:
    print(content)

print("\nTesting with ghost_file.txt:")
read_file_safe("ghost_file.txt")

# ============================================
# Part C — Robust API Calls
# ============================================
print("\n" + "=" * 50)
print("Part C — Robust API Calls")
print("=" * 50)

def fetch_products():
    try:
        # timeout=5 means give up if no response in 5 seconds
        url      = "https://dummyjson.com/products?limit=20"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            products = response.json()["products"]
            print(f"✓ Fetched {len(products)} products successfully")
            return products
        else:
            print(f"✗ Failed. Status code: {response.status_code}")
            return []

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
        return []

    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
        return []

    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def fetch_laptops():
    try:
        url      = "https://dummyjson.com/products/category/laptops"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            laptops = response.json()["products"]
            print(f"✓ Fetched {len(laptops)} laptops successfully")
            return laptops
        else:
            print(f"✗ Failed. Status code: {response.status_code}")
            return []

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
        return []

    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
        return []

    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def add_product():
    try:
        new_product = {
            "title":       "My Custom Product",
            "price":       999,
            "category":    "electronics",
            "description": "A product I created via API"
        }

        response = requests.post(
            "https://dummyjson.com/products/add",
            json=new_product,
            timeout=5
        )

        if response.status_code in [200, 201]:
            result = response.json()
            print(f"✓ Product added! ID: {result.get('id')}, "
                  f"Title: {result.get('title')}")
            return result
        else:
            print(f"✗ Failed. Status code: {response.status_code}")
            return None

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
        return None

    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Run all API calls
print("\nFetching products...")
fetch_products()

print("\nFetching laptops...")
fetch_laptops()

print("\nAdding new product...")
add_product()

# ============================================
# Part D — Input Validation Loop
# ============================================
print("\n" + "=" * 50)
print("Part D — Product Lookup Loop")
print("=" * 50)
print("Enter a product ID (1-100) or 'quit' to exit\n")

while True:

    # Ask user for input
    user_input = input("Enter a product ID to look up (1-100), or 'quit' to exit: ")

    # Check if user wants to quit
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # Validate input is a number
    try:
        product_id = int(user_input)
    except ValueError:
        print(f"⚠ Warning: '{user_input}' is not a valid number. Please enter a number between 1 and 100.\n")
        continue

    # Validate number is in range 1-100
    if product_id < 1 or product_id > 100:
        print(f"⚠ Warning: {product_id} is out of range. Please enter a number between 1 and 100.\n")
        continue

    # Make API call only if input is valid
    try:
        url      = f"https://dummyjson.com/products/{product_id}"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            product = response.json()
            print(f"✓ Product found!")
            print(f"  Title : {product['title']}")
            print(f"  Price : ${product['price']}\n")

        elif response.status_code == 404:
            print(f"Product not found.\n")

        else:
            print(f"Unexpected response: {response.status_code}\n")

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.\n")

    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.\n")

    except Exception as e:
        print(f"Unexpected error: {e}\n")
    
    