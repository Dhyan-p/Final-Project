# CS20 Major Project: Power-Shop

**Power-Shop** is a Python web application built as the **CS20 Major Project**.
It is a partially functional demo e-commerce website featuring user authentication, a shopping cart system, and dynamic product pages. This project demonstrates full-stack development using **Python, Flask, Jinja2 templating, and custon CSS**, with a focus on clean UI, usability, and maintainable backend code.

---

## 🚀 Table of Contents
- [About](#-about)
- [Features](#️-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Pages and Functionality](#️-pages-and-functionality)
- [Installation & Running the App](#️-installation--running-the-app)
- [Usage](#usage)
- [Code Overview](#-code-overview)
- [ Styling & UI Design](#-styling--ui-design)
- [Credits](#-credits)
- [Notes](#️-notes)

---

## 💡 About
**Power-Shop** is a demo e-commerce website built with **Python, Flask, and Jinja2 templating**.
The website demonstrates:

- User authentication (signup, login, logout)
- Dynamic shopping cart system
- Interactive homepage with categories, featured products, and promotional offers
- Profile page to display user information
- Clean and responsive frontend using HTML and CSS 

**Jinja2 templates** were used to render dynamic content for different pages, including logged-in and guest users, cart updates, and product listings. This allows the website to maintain a consistent layout while showing personalized or dynamic content.

---

## 🛠️ Features

### Authentication
- Sign up, login, and logout functionality  
- Password confirmation on signup to prevent mismatches  
- Flash messages for errors like duplicate accounts, incorrect password, or unregistered emails  
- Styled toast notifications for better user experience  

### Homepage
- **Hero section** with headline, description, and CTA buttons  
- **Categories section** displaying product categories and counts  
- **Featured products** section with images, names, prices, descriptions, and “Add to Cart” buttons  
- **Promotional offers** with badges, descriptions, and call-to-action buttons  

### Shopping Cart
- Add items to the cart from homepage or product sections  
- Update quantity or remove items  
- Automatic calculation of total amount  
- Empty cart page with friendly messaging  

### Profile Page
- Displays logged-in user information  
- Navigation menu for account management  
- Maintains consistent styling across all pages  

---

## 🧰 Tech Stack
- **Backend:** Python, Flask
- **Templateing Engine:** Jinja2
- **Frontend:** HTML, CSS
- **Other Tools:** Git & GitHub, AI tools for images and documentation/log entries

---

## 📂 Project Structure
The project is organized to separate templates, static assets, and backend logic.

```
project_root/
├── app.py                 # Main Flask app with routing, backend logic, and session management
├── requirements.txt       # Python dependencies
├── users.txt              # Sample user data for authentication
├── templates/             # HTML templates with Jinja2 for dynamic content
│   ├── cart_empty.html
│   ├── cart.html
│   ├── index_logged_in.html
│   ├── index.html
│   ├── login.html
│   ├── profile.html
│   └── signup.html
├── static/                # Static assets for styling and interactivity
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── (All images & logo for website)
└── README.md              # Project documentation
```

---

## 🖥️ Pages and Functionality

### 1. Homepage (`index.html`)
- Hero section with headline, description, and CTA buttons  
- Categories section with icons and product counts  
- Featured products section with product cards, images, names, prices, descriptions, and “Add to Cart” buttons  
- Promotional offer section with badge, description, and CTA buttons  

### 2. Login Page (`login.html`)
- Two-column layout with custom form styling  
- Flash messages for authentication errors  
- CTA button to redirect to signup  

### 3. Signup Page (`signup.html`)
- Email, password, and confirm password fields  
- Validation for duplicate accounts and password mismatch  
- Styled consistent with homepage and login page  

### 4. Profile Page (`profile.html`)
- Displays user information  
- Menu for account-related actions  
- Consistent layout with other pages  

### 5. Cart Pages (`cart.html` / `cart_empty.html`)
- Shows products added to cart with images, names, quantities, and prices  
- Update or remove items from the cart  
- Empty cart page with friendly messaging

---

## ⚙️ Installation & Running the App
1. Clone the repository:
    ```bash
    gh repo clone Dhyan-p/Final-Project

2. Nabigate into the project directory:
    cd Final-Project

3. Install dependencies:
    pip install -r requirements.txt

4. Start the web app locally:
    Open new terminal and enter following.
    python app.py

    ---

    The terminal will show a local URL (eg., http://127.0.0.1:5000). Open this link in your browser to access the website. 

---

## Usage
Sign up for a new account
Login to start purchasing
Add items to cart, update quantities, or remove items
Visit profile page to view user information

---

## 📝 Code Overview
app.py: Handles all backend routes, session management, and cart operations
templates/: Contains all HTML templates rendered via Jinja2 for dynamic content
static/css/style.css: Contains all custom styling, hover effects, and layout design
user.txt: Stores demo user credentials
All backend functions include docstrings and section headers for clarity. 

---

## 🎨 Styling & UI Design
Modern and responsive layout
Hero, Categories, Featured Products, and Promotional sections styled for clarity
Buttons, hover effects, and forms enhance interactivity
Toast notifications for authentication feedback
Consistent branding and color palette across all pages

---

## 🏆 Credits

**Power-Shop** was developed as part of the CS20 Major Project. Special thanks and credits go to the following contributors and tools:

| Contribution | Details |
|-------------|---------|
| **Project Author** | Dhyan P – full design, coding, and implementation of the backend and frontend |
| **AI Assistance** | ChatGPT – helped with writing documentation, planning development log entries, generating text and product descriptions |
| **AI Image Tools** | Genspark AI Image Prompt Creator – assisted in creating product and branding image prompts <br> E-Commerce Product Image Pro – generated product images for homepage and categories |
| **Libraries & Frameworks** | Flask – backend framework <br> Jinja2 – templating engine for dynamic content rendering |

> This project emphasizes learning and demo purposes. All AI-generated resources were used to assist design, context, and documentation clarity.

---

## ⚠️ Notes

This is a demo project. No real database or payment gateway is connected.
User data is stored in users.txt for demonstration purposes only.
Images were generated using AI tools, and ChatGPT helped create documentation and context for the website content.
