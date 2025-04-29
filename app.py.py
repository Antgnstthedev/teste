from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import os
import traceback

app = Flask(__name__)
CORS(app)

# Configuração do servidor de e-mail (exemplo com Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jotaprxdx19@gmail.com'  # SEU E-MAIL
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
# app.config['MAIL_PASSWORD'] = 'stnog asiu tekm jdkg'           # SENHA DE APP GERADA
app.config['MAIL_DEFAULT_SENDER'] = ('Barbearia', 'jotaprxdx19@gmail.com')

mail = Mail(app)

@app.route("/contato", methods=["POST"])
def contato():
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email")  # usamos "email" agora, não "emailCliente"
    horario = dados.get("horario")

    if not nome:
        return "Campo 'nome' obrigatório.", 400
    if not email or not horario:
        return "Todos os campos são obrigatórios.", 400

    try:
        msg = Message(
            subject="Confirmação de Agendamento - Barbearia",
            recipients=[email],
            body=f"Olá, {nome}!\n\nSeu horário foi agendado com sucesso para: {horario}.\n\nAgradecemos pela preferência!"
        )
        mail.send(msg)
        return jsonify({"mensagem": "Agendamento realizado e e-mail enviado!"}), 200

    except Exception as e:
        print("Erro ao enviar e-mail:", e)
        traceback.print_exc()
        return "Erro ao enviar e-mail.", 500

if __name__ == "__main__":
    app.run(debug=True)
