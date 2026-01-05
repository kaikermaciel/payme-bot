import smtplib
import ssl
import datetime
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Carrega variáveis
load_dotenv()

# --- CONFIGURAÇÕES ---
EMAIL_SENDER = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

# --- DADOS DE PAGAMENTO ---
CHAVE_PIX = os.environ.get('EMAIL_USER')
NOME_TITULAR = "Kaike Maciel"
VALOR_INDIVIDUAL = "R$ 6.81"

# --- LISTA DA FAMÍLIA ---
ASSINANTES = [
    {
        "nome": "Gui",
        "email": "g.martiins.silva15@gmail.com"
    },
    {
        "nome": "Kaike",
        "email": "kaiker.maciel@gmail.com"
    }, 
    {
        "nome": "Gabriela",
        "email": "gabriela.malveira22@gmail.com"
    },
    {
        "nome": "Tay Tay",
        "email": "taycruz424242@gmail.com"
    },
    {
        "nome": "Aline",
        "email": "aline.silmara.m@gmail.com"
    },
    {
        "nome": "Tedy",
        "email": "tedypristt@gmail.com"
    }
]

def enviar_cobranca():
    # Pega o mês atual para o assunto do e-mail
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    mes_atual = meses[datetime.datetime.now().month - 1]
    ano_atual = datetime.datetime.now().year

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)

            for membro in ASSINANTES:
                print(f"Enviando cobrança para: {membro['nome']}...")

                # Monta HTML bonito
                body = f"""
                <html>
                  <body style="font-family: Arial, sans-serif; color: #333;">
                    <h2 style="color: #1DB954;">Spotify - {mes_atual}</h2>
                    <p>Olá, <strong>{membro['nome']}</strong>!</p>
                    <p>Passando para lembrar do pagamento mensal da nossa assinatura do Spotify Família.</p>
                    
                    <div style="background-color: #f4f4f4; padding: 15px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #1DB954;">
                        <p style="margin: 5px 0;"><strong>Valor:</strong> {VALOR_INDIVIDUAL}</p>
                        <p style="margin: 5px 0;"><strong>Chave Pix:</strong> {CHAVE_PIX}</p>
                        <p style="margin: 5px 0;"><strong>Titular:</strong> {NOME_TITULAR}</p>
                    </div>

                    <p>Se já pagou, desconsidere este e-mail. Vamos continuar ouvindo música sem anúncios! 🎧</p>
                    
                    <p style="font-size: 12px; color: #777;">Bot de Cobrança Automática</p>
                  </body>
                </html>
                """

                msg = EmailMessage()
                msg['From'] = EMAIL_SENDER
                msg['To'] = membro['email']
                msg['Subject'] = f"Spotify Family: Fatura de {mes_atual}/{ano_atual}"
                msg.set_content(body, subtype='html')

                smtp.send_message(msg)
                print(f"E-mail enviado para {membro['nome']}!")

    except Exception as e:
        print(f"Erro CRÍTICO no envio: {e}")

if __name__ == "__main__":
    enviar_cobranca()