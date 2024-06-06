import ssl
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

#credenziali d'accesso
email_sender = 'alebig2006@gmail.com'
email_password = 'ofhy qcsc xznf sdvo' #password esclusiva per le email inviate con python
filepath = "C:\\Users\\Alessio\\PycharmProjects\\SMTPLIB_Try01\\.venv\\Report_prova02.5.pdf"

#email ricevitore
email_receiver = 'a.bigon@orion-srl.it'

#struttura effettiva dell'email
subject = "Prova invio email 01"
body = """
Prova avvenuta con successo!

"""

def Send_Email(fromadd, password, toadd, subject, body, file):

    link = "https://ilpirulino.github.io/EMAIL_SERVER02/"
    #https://github.com/BigonAlessio/PCTO_Return_Email.git
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = fromadd
    msg['To'] = toadd
    part1 = MIMEText(body, 'plain')
    part2 = MIMEText(link, 'html')
    msg.attach(part1)
    msg.attach(part2)

    # apertura file pdf da inoltrare
    attachment = MIMEBase('application', 'octet-stream')
    with open(file, 'rb') as cargo:
        attachment.set_payload(cargo.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename=file[-20:])
    msg.attach(attachment)

    # creazione del messaggio
    context = ssl.create_default_context()
    print('>>Compilation of the message <COMPLETE>')

    # try per stabilire un collegamento e inviare la mail
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:  # utilizzo del protocollo SSL
            print('>>Creation of the connection <COMPLETE>')
            smtp.login(fromadd, password)  # login alla mail
            print(">>Login <COMPLETE>")
            smtp.sendmail(fromadd, toadd, msg.as_string())  # invio della mail
            print(">>Email sent <COMPLETE>")
    except Exception as e:
        print(f">>Mission Failed <ERROR>-: {e}")

def Sendback_Email(fromadd, file):
    # apertura file pdf da inoltrare
    with open(file, 'rb') as cargo:
        content = cargo.read()

    body = """
    Riconsegna del report compilato avvenuta con successo!
    
    """
    # compilazione del messaggio
    em = EmailMessage()
    em['From'] = fromadd
    em['To'] = fromadd #aggiungere l'indirizzo del tecnico principale
    em['Subject'] = "Consegna Report Compilato"
    em.set_content(body)  # assegnazione del corpo della mail
    em.add_attachment(content, maintype='application', subtype='pdf',
                      filename=file)  # aggiunta del pdf
    em.add_attachment(link, maintype='application', subtype='html')

    # creazione del messaggio
    context = ssl.create_default_context()
    print('>>Compilation of the message <COMPLETE>')

    # try per stabilire un collegamento e inviare la mail
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:  # utilizzo del protocollo SSL
            print('>>Creation of the connection <COMPLETE>')
            smtp.login(fromadd, 'ofhy qcsc xznf sdvo')  # login alla mail
            print(">>Login <COMPLETE>")
            smtp.sendmail(fromadd, fromadd, em)  # invio della mail     #assegnare al secondo fromadd l'indirizzo del tecnico principale
            print(">>Email sent <COMPLETE>")
    except Exception as e:
        print(f">>Mission Failed <ERROR>-: {e}")
    finally:
        smtp.quit()

Send_Email(email_sender, email_password, email_receiver, subject, body, filepath)
