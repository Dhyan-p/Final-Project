from flask import Flask, render_template, request, redirect, url_for, session, flash
import hashlib
import os

app = Flask(__name__)
app.secret_key = 'power-shop-secret-key-2025'

PRODUCTS = [
    {"id": 1, "name": "Wireless Pro Headphones", "price": 299.99, "category": "Electronics", "image": "/static/images/headphones.jpg"},

    {"id": 2, "name": "Smart Watch Series X", "price": 449.99, "category": "Electronics", "image": "/static/images/smartwatch.jpg"}, 

    {"id": 3, "name": "Minimalist Leather Bag", "price": 189.99, "category": "Fashion", "image": "/static/images/purse.jpg"},

    {"id": 4, "name": "Premium Running Shoes", "price": 159.99, "category": "Sports", "image": "/static/images/running-shoes.jpg"},

    {"id": 5, "name": "Sunglasses", "price": 129.99, "category": "Fashion", "image": "/static/images/glasses.jpg"},

    {"id": 6, "name": "Portable Speaker JBL", "price": 79.99, "category": "Electronics", "image": "/static/images/jbl-speaker.jpg"},

    {"id": 7, "name": "Ceramic Coffee Mug", "price": 49.99, "category": "Home", "image": "/static/images/coffee-mug.jpg"},

    {"id": 8, "name": "Premium Yoga Mat", "price": 89.99, "category": "Sports", "image": "/static/images/yoga-mat.jpg"},
]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_user(email, name, password):
    hashed = hash_password(password)
    with open('users.txt', 'a') as f:
        f.write(f"{email}|{name}|{hashed}\n")

def verify_user(email, password):
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
    if not os.path.exists('users.txt'):
        return False
    with open('users.txt', 'r') as f:
        for line in f:
            if line.startswith(email + '|'):
                return True
    return False

@app.route('/')
def index():
    if 'user' in session:
        return render_template('index_logged_in.html')
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = verify_user(email, password)
        if not user_exists(email):
            flash('Email not registered')
            return render_template('login.html')
        
        user = verify_user(email, password)
        if not user: 
            flash('password not matched')
            return render_template('login.html')

        session['user'] = user
        session['cart'] = []
        return redirect(url_for('index'))
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
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
        session['user'] = {"email": email, "name": name}
        session['cart'] = []
        return redirect(url_for('index'))
    
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('profile.html')

@app.route('/cart')
def cart():
    if 'user' not in session:
        return redirect(url_for('login'))
    cart_items = session.get('cart', [])
    if len(cart_items) == 0:
        return render_template('cart_empty.html')
    return render_template('cart.html')

@app.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    if 'user' not in session:
        return redirect(url_for('login'))
    if 'cart' not in session:
        session['cart'] = []
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        cart = session['cart']
        cart.append(product)
        session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/remove-from-cart/<int:product_id>')
def remove_from_cart(product_id):
    if 'cart' in session:
        cart = session['cart']
        cart = [item for item in cart if item['id'] != product_id]
        session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    if 'user' not in session:
        return redirect(url_for('login'))
    session['cart'] = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)