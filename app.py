from flask import Flask
import smtp_code as bird

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/sendemail')
def sendemail():
    email_sender = 'alebig2006@gmail.com'
    email_password = 'wlbp kpds qtqr ximv'
    email_receiver = email_sender
    email_subject = 'Prova invio email via html'
    email_body = f"""<br>Prova avvenuta con successo!<br><br>Link: <a href="{link}">Visita il sito</a>"""
    bird.Send_Email(email_sender, email_password, email_receiver, email_subject, email_body)
    return "Email sent with sccess!"

if __name__ == '__main__':
    app.run(debug=True)
