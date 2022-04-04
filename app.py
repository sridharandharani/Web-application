from flask import Flask
app = Flask(__name__)

@app.route('/')
def Welcome():
    return "Welcome to my website"

@app.route('/contact')
def Contact_page():
    return "Contact page"

@app.route('/home')
def Home_page():
    return "Home page"

@app.route('/gallery')
def Gallery_page():
    return "Gallery page"

if __name__ == "__main__":
    app.run()