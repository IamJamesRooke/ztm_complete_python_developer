from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__, static_folder='static')
app.config['DEBUG'] = True  # Enable debug mode


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name):
    return render_template(f'{page_name}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        return redirect('/thankyou.html')
    else:
        return 'Error: Form submission failed!'

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode when running directly