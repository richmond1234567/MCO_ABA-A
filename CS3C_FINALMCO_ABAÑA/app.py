from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import os
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/send', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        msg = Message(subject, sender=os.getenv('EMAIL_USER'), recipients=[email])
        msg.body = message
        mail.send(msg)
        return render_template('contact.html', email_sent=True)
    else:
        return "Method not allowed", 405
    

if __name__ == '__main__':
    app.run(debug=True)