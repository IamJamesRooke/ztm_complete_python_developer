from flask import Flask, render_template, url_for, request, redirect
import os, csv

app = Flask(__name__, static_folder='static')
app.config['DEBUG'] = True  # Enable debug mode


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name):
    return render_template(f'{page_name}')

def write_to_file(data):
    current_folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_folder, 'database.txt')
    with open(file_path, mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'{email}, {subject}, {message}\n')

def write_to_csv(data):
    current_folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_folder, 'database.csv')
    with open(file_path, mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, 
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database.'
    else:
        return 'Error: Form submission failed!'

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode when running directly