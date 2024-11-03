from flask import Flask, render_template, send_from_directory
import os

app = Flask(
    __name__,
    static_folder=".",            # Root directory for static files
    template_folder="flask_app/templates"  # Template directory
)

@app.route('/')
def home():
    return render_template('index_flask.html')  # Use index_flask.html for Flask server



# Serve CSS file
@app.route('/index.css')
def serve_css():
    return send_from_directory(os.path.abspath("."), "index.css")

# Serve static HTML files as routes
@app.route('/joana')
def joana():
    return render_template('joana.html')

@app.route('/eric')
def eric():
    return render_template('eric.html')

@app.route('/lois')
def lois():
    return render_template('loispage.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
