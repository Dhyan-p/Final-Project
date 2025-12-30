from flask import Flask, render_template, request, redirect, url_for, session, flash
import hashlib
import os

# ==============================
# Application Configuration
# ==============================
app = Flask(__name__)

# Secret key used for session management and security
app.secret_key = 'power-shop-secret-key-2025'

# ==============================
# Product Data
# ==============================
# Each product contains pricing, category, image path, and a maximum quantity allowed per user in the cart.
PRODUCTS = [
    {"id": 1, "name": "Wireless Pro Headphones", "price": 299.99, "category": "Electronics", "image": "/static/images/headphones.jpg", "max_quantity": 5},

    {"id": 2, "name": "Smart Watch Series X", "price": 449.99, "category": "Electronics", "image": "/static/images/smartwatch.jpg", "max_quantity": 4}, 

    {"id": 3, "name": "Minimalist Leather Bag", "price": 189.99, "category": "Fashion", "image": "/static/images/purse.jpg", "max_quantity": 5},

    {"id": 4, "name": "Premium Running Shoes", "price": 159.99, "category": "Sports", "image": "/static/images/running-shoes.jpg", "max_quantity": 5},

    {"id": 5, "name": "Sunglasses", "price": 129.99, "category": "Fashion", "image": "/static/images/glasses.jpg", "max_quantity": 8},

    {"id": 6, "name": "Portable Speaker JBL", "price": 79.99, "category": "Electronics", "image": "/static/images/jbl-speaker.jpg", "max_quantity": 4},

    {"id": 7, "name": "Ceramic Coffee Mug", "price": 49.99, "category": "Home", "image": "/static/images/coffee-mug.jpg", "max_quantity": 10},

    {"id": 8, "name": "Premium Yoga Mat", "price": 89.99, "category": "Sports", "image": "/static/images/yoga-mat.jpg", "max_quantity": 10},
]

# ==============================
# Functions
# ==============================

def hash_password(password):
    """ 
    Hashes a plain-text password using SHA-256

    Args:
        Password (str): The user's plain-text password.
        
    Returns:
        Str: A securely hashed version of the password.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def save_user(email, name, password):
    """ 
    Saves a new user's details to the user.txt file.

    Args:
    email (str): User's email address.
    name (str): User's name.
    password (str): User's plain-text password (will be hashed).
    """
    hashed = hash_password(password)

    with open('users.txt', 'a') as f:
        f.write(f"{email}|{name}|{hashed}\n")


def verify_user(email, password):
    """ 
    Verifies user credentials during login.
    
    Args: 
        email (str): User's email address.
        password (str): User's plain-text password.

    Returns:
        dict or None: User dictionary if credentials are valid, otherwise None.
    """
    if not os.path.exists('users.txt'):
        return None 
    
    hashed = hash_password(password)

    with open('users.txt', 'r') as f:
        for line in f:
            parts = line.strip().split('|')

            if len(parts) == 3 and parts[0] == email and parts[2] == hashed:
                return {"email": parts[0], "name": parts[1]}
            
    return None


def user_exists(email):
    """ 
    Checks whether a user with the give email already exists.

    Args: 
        email (str): Email address to check.

    Returns:
        bool: Ture if user exists, False otherwise.
    """
    if not os.path.exists('users.txt'):
        return False
    
    with open('users.txt', 'r') as f:
        for line in f:
            if line.startswith(email + '|'):
                return True
            
    return False


# ==============================
# Routes
# ==============================

@app.route('/')
def index():
    """ 
    Renders the home page.
    Shows a different homepage if the user is logged in.
    """
    if 'user' in session:
        return render_template('index_logged_in.html')
    
    return render_template('index.html')

# ------------------------------
# Login Route
# ------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles user login functionality.

    - Validates email existence
    - Validates password correctness
    - Creates user session on success
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check if the email exists before validating password
        if not user_exists(email):
            flash('Email not registered')
            return render_template('login.html')
        
        user = verify_user(email, password)

        if not user: 
            flash('password not matched')
            return render_template('login.html')

        # Successful login
        session['user'] = user
        session['cart'] = {}

        return redirect(url_for('index'))
    
    return render_template('login.html')

# ------------------------------
# Signup Route
# ------------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Handles user registration.

    - Checks password confirmation
    - Prevents duplicate email registration
    - Saves new user data
    """
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match')
            return render_template('signup.html')
        
        if user_exists(email):
            flash('Email already registered')
            return render_template('signup.html')
        
        save_user(email, name, password)

        # Auto-login after successful signup
        session['user'] = {"email": email, "name": name}
        session['cart'] = {}

        return redirect(url_for('index'))
    
    return render_template('signup.html')

# ------------------------------
# logout
# ------------------------------
@app.route('/logout')
def logout():
    """
    Logs the user out by clearing the session.
    """
    session.clear()
    return redirect(url_for('index'))

# ------------------------------
# Profile Page
# ------------------------------
@app.route('/profile')
def profile():
    """
    Displays the user's profile page.
    Redirects to login if user is not authenticated.
    """
    if 'user' not in session:
        return redirect(url_for('login'))
    
    return render_template('profile.html')

# ------------------------------
# Cart Page
# ------------------------------
@app.route('/cart')
def cart():
    """
    Displays the shopping cart.
    
    - Requires the user to be logged in.
    - Shows empty cart view if no items exist
    - Calculates totals dynamically for cart items
    """
    if 'user' not in session:
        return redirect(url_for('login'))

    cart_data = session.get('cart', {})

    if not cart_data:
        return render_template('cart_empty.html')

    cart_items = []
    total = 0

    # Build cart item list with product details
    for product_id, quantity in cart_data.items():
        product = next(p for p in PRODUCTS if p['id'] == int(product_id))
        item_total = product['price'] * quantity
        total += item_total

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "item_total": item_total
        })

    return render_template('cart.html', cart_items=cart_items, total=total )

# ------------------------------
# Add to Cart
# ------------------------------
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    """
    Adds a product to the user's cart.

    - If product exists, increase quantity (up to max limit).
    - If not, add as new cart item.
    """
    if 'user' not in session:
        return redirect(url_for('login'))

    if 'cart' not in session or not isinstance(session['cart'], dict):
        session['cart'] = {}

    cart = session['cart']

    # Find product by ID
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return redirect(url_for('index'))

    pid = str(product_id)
    current_quantity = cart.get(pid, 0)

    if current_quantity < product['max_quantity']:
        cart[pid] = current_quantity + 1

    session['cart'] = cart
    return redirect(url_for('cart'))

# ------------------------------
# Decrease Quantity
# ------------------------------
@app.route('/decrease/<int:product_id>')
def decrease_quantity(product_id):
    """
    Decreases the quantity of a product in the cart by 1.
    Removes the product completely if quantity reaches 0.
    """
    if 'user' not in session:
        return redirect(url_for('login'))

    cart = session.get('cart', {})
    pid = str(product_id)

    if pid in cart:
        cart[pid] -= 1

        if cart[pid] <= 0:
            del cart[pid]

    session['cart'] = cart
    return redirect(url_for('cart'))


# ------------------------------
# Remove from Cart
# ------------------------------
@app.route('/remove-from-cart/<int:product_id>')
def remove_from_cart(product_id):
    """
    Removes a product from the user's cart.

    Args:
        product_id (int): ID of the product to remove.
    """
    if 'cart' in session:
        cart = session['cart']
        cart.pop(str(product_id), None)
        session['cart'] = cart

    return redirect(url_for('cart'))

# ------------------------------
# Checkout
# ------------------------------
@app.route('/checkout')
def checkout():
    """
    Clears the cart after checkout is completed.

    (No payment processing - demo behavior only)
    """
    if 'user' not in session:
        return redirect(url_for('login'))
    
    session['cart'] = {}
    return redirect(url_for('index'))

# ------------------------------
# Application Runner
# ------------------------------
if __name__ == '__main__':
    app.run(debug=True)