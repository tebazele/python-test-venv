from flask import current_app, jsonify
from flask_mailing import Mail, Message


current_app.config['MAIL_USERNAME'] = "jeanne@craftranker.com"
current_app.config['MAIL_PASSWORD'] = "Myname1sn0*"
current_app.config['MAIL_PORT'] = 587
current_app.config['MAIL_SERVER'] = "mail.privateemail.com"
current_app.config['MAIL_USE_TLS'] = True
current_app.config['MAIL_USE_SSL'] = False
# current_app.config['USE_CREDENTIALS'] = True
# current_app.config['VALIDATE_CERTS'] = True
# current_app.config['MAIL_DEFAULT_SENDER'] = "jeanne@craftranker.com"

mail = Mail(current_app)
# current_app.app_context()

html = """<p>I love you<p>"""


@current_app.get("/email")
async def simple_send():
    message = Message(
        subject="Hi Bryan",
        recipients=["tebazele@gmail.com"],
        body=html,
        subtype="html"
    )

    await mail.send_message(message)
    return jsonify(status_code=200, content={"message": "email has been sent"})
