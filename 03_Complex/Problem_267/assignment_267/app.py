from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    name = request.form['name'].encode()
    encrypted_name = cipher_suite.encrypt(name)
    return render_template('result.html', result=encrypted_name.decode())

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_name = request.form['encrypted_name'].encode()
    decrypted_name = cipher_suite.decrypt(encrypted_name)
    return render_template('result.html', result=decrypted_name.decode())

if __name__ == '__main__':
    app.run(debug=True)
