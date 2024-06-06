from flask import Flask, render_template, request
import smtp_code as bird

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Return.html')

@app.route('/return', methods=['POST'])
def save_data():
    email_sender = request.form['email_sender']
    email_password = request.form['email_password']
    email_receiver = request.form['email_receiver']
    email_subject = request.form['email_subject']
    email_body = request.form['email_body']
    email_file = request.form['email_file']
    bird.Send_Email(email_sender, email_password, email_receiver, email_subject, email_body, email_file)
    return render_template('Return.html')

if __name__ == '__main__':
    app.run(debug=True)
