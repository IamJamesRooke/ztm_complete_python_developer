from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['DEBUG'] = True  # Enable debug mode

@app.route('/')
@app.route('/<username>/<post_id>')
def index(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode when running directly