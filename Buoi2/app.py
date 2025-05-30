from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = CaesarCipher()
    encrypted_text = cipher.encrypt_text(text, key)
    return render_template("caesar.html", result={'type': 'Mã hóa', 'text': text, 'key': key, 'output': encrypted_text})

@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = CaesarCipher()
    decrypted_text = cipher.decrypt_text(text, key)
    return render_template("caesar.html", result={'type': 'Giải mã', 'text': text, 'key': key, 'output': decrypted_text})

# Vigenere Cipher
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    cipher = VigenereCipher()
    encrypted_text = cipher.encrypt_text(text, key)
    return render_template("vigenere.html", result={'type': 'Mã hóa', 'text': text, 'key': key, 'output': encrypted_text})

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    cipher = VigenereCipher()
    decrypted_text = cipher.decrypt_text(text, key)
    return render_template("vigenere.html", result={'type': 'Giải mã', 'text': text, 'key': key, 'output': decrypted_text})

# Rail Fence Cipher
@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputRails'])
    cipher = RailFenceCipher()
    encrypted_text = cipher.encrypt_text(text, key)
    return render_template("railfence.html", result={'type': 'Mã hóa', 'text': text, 'key': key, 'output': encrypted_text})

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputRails'])
    cipher = RailFenceCipher()
    decrypted_text = cipher.decrypt_text(text, key)
    return render_template("railfence.html", result={'type': 'Giải mã', 'text': text, 'key': key, 'output': decrypted_text})

# Transposition Cipher
@app.route("/transposition")
def transposition():
    return render_template("transposition.html")

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKey'])
    cipher = TranspositionCipher()
    encrypted_text = cipher.encrypt_text(text, key)
    return render_template("transposition.html", result={'type': 'Mã hóa', 'text': text, 'key': key, 'output': encrypted_text})

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])
    cipher = TranspositionCipher()
    decrypted_text = cipher.decrypt_text(text, key)
    return render_template("transposition.html", result={'type': 'Giải mã', 'text': text, 'key': key, 'output': decrypted_text})

# Playfair Cipher
@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    cipher = PlayFairCipher()
    encrypted_text = cipher.encrypt_text(text, key)
    return render_template("playfair.html", result={'type': 'Mã hóa', 'text': text, 'key': key, 'output': encrypted_text})

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    cipher = PlayFairCipher()
    decrypted_text = cipher.decrypt_text(text, key)
    return render_template("playfair.html", result={'type': 'Giải mã', 'text': text, 'key': key, 'output': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
