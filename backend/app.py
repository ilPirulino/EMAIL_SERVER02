from flask import Flask, render_template, request
import smtp_code as bird

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sendemail', methods=['POST'])
def sendemail():
    email_sender = 'alebig2006@gmail.com'
    email_password = 'wlbp kpds qtqr ximv'
    email_receiver = email_sender
    email_subject = "Prova invio mail attraverso sito html"
    link = "https://ilpirulino.github.io/EMAIL_SERVER02/"
    email_body = f"""<br>Prova avvenuta con successo!<br><br>Link: <a href="{link}">Visita il sito</a>"""
    bird.Send_Email(email_sender, email_password, email_receiver, email_subject)
    return "Email sent with success!"

if __name__ == '__main__':
    app.run()
