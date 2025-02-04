from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True  # Enable debug mode

@app.route('/')
def index():
    print(url_for('static', filename='favicon.ico'))
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode when running directly