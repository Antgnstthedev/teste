from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(_name_)

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'seu_email@gmail.com'
SMTP_PASSWORD = 'sua_senha_ou_app_password'

EMAIL_BARB = 'email_do_barbeiro@gmail.com'

@app.route('/')
def index():
    # Aqui você pode servir seu HTML, por simplicidade retornando uma mensagem
    return 'Página principal'

@app.route('/enviar-email', methods=['POST'])
def enviar_email():
    nome = request.form.get('nome')
    email_cliente = request.form.get('email')
    celular = request.form.get('celular')
    mensagem_cliente = request.form.get('mensagem')

    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = EMAIL_BARB
    msg['Subject'] = f'Novo agendamento de {nome}'
    msg.add_header('Reply-To', email_cliente)  # importante para responder direto ao cliente

    corpo = f"""
    Novo agendamento pelo site:

    Nome: {nome}
    Email: {email_cliente}
    Celular: {celular}
    Mensagem: {mensagem_cliente}
    """

    msg.attach(MIMEText(corpo, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, EMAIL_BARB, msg.as_string())
        server.quit()
        return "E-mail enviado com sucesso!"
    except Exception as e:
        return f"Erro ao enviar e-mail: {str(e)}"

if _name_ == '_main_':
    app.run(debug=True)
