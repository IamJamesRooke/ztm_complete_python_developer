from flask import Flask, render_template, url_for
app = Flask(__name__, static_folder='static')
app.config['DEBUG'] = True  # Enable debug mode

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode when running directly