from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask('__name__')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page>')
def html_page(page):
    page_name = page + '.html'
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', newline='\n', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


def write_to_csv2(data):
    with open('database.csv', 'a', newline='') as database:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(database, fieldnames=fieldnames)

        # 'prints first_name,last_name' on first row
        writer.writeheader()

        # 'prints 'Baked,Beans' ib second row, etc.
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou')
        except:
            return 'Could not save to database.'

    else:
        return 'Something went wrong.'
