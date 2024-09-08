from flask import Flask, render_template, request
import os
from pathlib import Path

app = Flask(__name__)

# Function to create a secure folder
def create_secure_folder(folder_name="secure_folder"):
    folder_path = Path(folder_name)
    if not folder_path.exists():
        folder_path.mkdir(parents=True)
    return folder_path

# Custom encryption function (Caesar cipher)
def encrypt(message, key):
    encrypted = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                encrypted += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            encrypted += char
    return encrypted

# Custom decryption function (Caesar cipher)
def decrypt(encrypted_message, key):
    decrypted = ""
    for char in encrypted_message:
        if char.isalpha():
            if char.islower():
                decrypted += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            else:
                decrypted += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        else:
            decrypted += char
    return decrypted

# Save the message to a file
def save_to_file(folder_path, file_name, data):
    file_path = folder_path / file_name
    with open(file_path, 'w') as file_out:
        file_out.write(data)

# Home route to show the form
@app.route('/')
def index():
    return render_template('index.html')

# Encrypt route that processes the form data
@app.route('/encrypt', methods=['POST'])
def encrypt_message():
    folder = create_secure_folder()

    message = request.form['message']
    key = int(request.form['key'])

    # Encrypt the message
    encrypted_message = encrypt(message, key)

    # Save the encrypted message to a file
    save_to_file(folder, "encrypted_message.txt", encrypted_message)

    # Optionally decrypt based on user input
    if 'show_decrypted' in request.form and request.form['show_decrypted'] == 'yes':
        decrypted_message = decrypt(encrypted_message, key)
        save_to_file(folder, "decrypted_message.txt", decrypted_message)
    else:
        decrypted_message = None

    return render_template('result.html', encrypted_message=encrypted_message, decrypted_message=decrypted_message)

if __name__ == '__main__':
    app.run(debug=True)
