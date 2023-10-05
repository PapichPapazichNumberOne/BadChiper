import tkinter as tk
import random
import tkinter.scrolledtext as tkst
from tkinter import ttk

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shift_amount = self.shift % 32  # Для русского языка 32 буквы
                if char.islower():
                    encrypted_char = chr(((ord(char) - ord('а') + shift_amount) % 32) + ord('а'))
                elif char.isupper():
                    encrypted_char = chr(((ord(char) - ord('А') + shift_amount) % 32) + ord('А'))
            else:
                encrypted_char = char
            encrypted_text += encrypted_char
        return encrypted_text

    def decrypt(self, text):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                shift_amount = -self.shift % 32  # Для расшифровки применяем обратный сдвиг
                if char.islower():
                    decrypted_char = chr(((ord(char) - ord('а') + shift_amount) % 32) + ord('а'))
                elif char.isupper():
                    decrypted_char = chr(((ord(char) - ord('А') + shift_amount) % 32) + ord('А'))
            else:
                decrypted_char = char
            decrypted_text += decrypted_char
        return decrypted_text

class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper()

    def encrypt(self, text):
        encrypted_text = ""
        keyword_length = len(self.keyword)
        keyword_index = 0

        for char in text:
            if char.isalpha():
                shift = ord(self.keyword[keyword_index % keyword_length]) - ord('А')
                if char.islower():
                    encrypted_char = chr(((ord(char) - ord('а') + shift) % 32) + ord('а'))
                elif char.isupper():
                    encrypted_char = chr(((ord(char) - ord('А') + shift) % 32) + ord('А'))
                keyword_index += 1
            else:
                encrypted_char = char
            encrypted_text += encrypted_char

        return encrypted_text

    def decrypt(self, text):
        decrypted_text = ""
        keyword_length = len(self.keyword)
        keyword_index = 0

        for char in text:
            if char.isalpha():
                shift = ord(self.keyword[keyword_index % keyword_length]) - ord('А')
                if char.islower():
                    decrypted_char = chr(((ord(char) - ord('а') - shift + 32) % 32) + ord('а'))
                elif char.isupper():
                    decrypted_char = chr(((ord(char) - ord('А') - shift + 32) % 32) + ord('А'))
                keyword_index += 1
            else:
                decrypted_char = char
            decrypted_text += decrypted_char

        return decrypted_text

class VernamCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        encrypted_text = ""
        for i, char in enumerate(text):
            if char.isalpha():
                key_char = self.key[i % len(self.key)]
                encrypted_char = chr(ord(char) ^ ord(key_char))
            else:
                encrypted_char = char
            encrypted_text += encrypted_char
        return encrypted_text

    class VigenereCipher:
        def __init__(self, keyword):
            self.keyword = keyword.upper()

        def encrypt(self, text):
            encrypted_text = ""
            keyword_length = len(self.keyword)
            keyword_index = 0

            for char in text:
                if char.isalpha():
                    shift = ord(self.keyword[keyword_index % keyword_length]) - ord('А')
                    if char.islower():
                        encrypted_char = chr(((ord(char) - ord('а') + shift) % 32) + ord('а'))
                    elif char.isupper():
                        encrypted_char = chr(((ord(char) - ord('А') + shift) % 32) + ord('А'))
                    keyword_index += 1
                else:
                    encrypted_char = char
                encrypted_text += encrypted_char

            return encrypted_text

        def decrypt(self, text):
            decrypted_text = ""
            keyword_length = len(self.keyword)
            keyword_index = 0

            for char in text:
                if char.isalpha():
                    shift = ord(self.keyword[keyword_index % keyword_length]) - ord('А')
                    if char.islower():
                        decrypted_char = chr(((ord(char) - ord('а') - shift + 32) % 32) + ord('а'))
                    elif char.isupper():
                        decrypted_char = chr(((ord(char) - ord('А') - shift + 32) % 32) + ord('А'))
                    keyword_index += 1
                else:
                    decrypted_char = char
                decrypted_text += decrypted_char

            return decrypted_text

    def decrypt(self, text):
        return self.encrypt(text)

def generate_vernam_key():
    key = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(32))
    key_entry.delete(0, "end")
    key_entry.insert(0, key)

def encrypt_button_clicked():
    selected_cipher = cipher_choice.get()
    text_to_encrypt = input_text.get("1.0", "end-1c")

    if selected_cipher == "Цезарь":
        shift = int(shift_entry.get())
        caesar_cipher = CaesarCipher(shift)
        encrypted_text = caesar_cipher.encrypt(text_to_encrypt)
    elif selected_cipher == "Виженер":
        keyword = keyword_entry.get()
        vigenere_cipher = VigenereCipher(keyword)
        encrypted_text = vigenere_cipher.encrypt(text_to_encrypt)
    elif selected_cipher == "Вернам":
        key = key_entry.get()
        vernam_cipher = VernamCipher(key)
        encrypted_text = vernam_cipher.encrypt(text_to_encrypt)
    else:
        encrypted_text = "Выберите шифр"

    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

def decrypt_button_clicked():
    selected_cipher = cipher_choice.get()
    text_to_decrypt = input_text.get("1.0", "end-1c")

    if selected_cipher == "Цезарь":
        shift = int(shift_entry.get())
        caesar_cipher = CaesarCipher(shift)
        decrypted_text = caesar_cipher.decrypt(text_to_decrypt)
    elif selected_cipher == "Виженер":
        keyword = keyword_entry.get()
        vigenere_cipher = VigenereCipher(keyword)
        decrypted_text = vigenere_cipher.decrypt(text_to_decrypt)
    elif selected_cipher == "Вернам":
        key = key_entry.get()
        vernam_cipher = VernamCipher(key)
        decrypted_text = vernam_cipher.decrypt(text_to_decrypt)
    else:
        decrypted_text = "Выберите шифр"

    output_text.delete("1.0", "end")
    output_text.insert("1.0", decrypted_text)
def copy_text():
    selected_text = output_text.get("1.0", "end-1c")
    app.clipboard_clear()
    app.clipboard_append(selected_text)
    app.update()

def paste_text():
    pasted_text = app.clipboard_get()
    input_text.delete("1.0", "end")
    input_text.insert("1.0", pasted_text)





app = tk.Tk()
app.title("Шифры Цезаря, Виженера и Вернама")





input_label = tk.Label(app, text="Введите текст:")
input_label.pack()

input_text = tkst.ScrolledText(app, width=40, height=5)
input_text.pack()

cipher_label = tk.Label(app, text="Выберите шифр:")
cipher_label.pack()

cipher_choice = tk.StringVar()
cipher_choice.set("Цезарь")
cipher_option_menu = ttk.Combobox(app, textvariable=cipher_choice, values=("Цезарь", "Виженер", "Вернам"))
cipher_option_menu.pack()

shift_label = tk.Label(app, text="Сдвиг (для Цезаря):")
shift_label.pack()

shift_entry = tk.Entry(app)
shift_entry.pack()

keyword_label = tk.Label(app, text="Ключ (для Виженера):")
keyword_label.pack()

keyword_entry = tk.Entry(app)
keyword_entry.pack()

key_label = tk.Label(app, text="Ключ (для Вернама):")
key_label.pack()

key_entry = tk.Entry(app)
key_entry.pack()

generate_key_button = tk.Button(app, text="Сгенерировать ключ (для Вернама)", command=generate_vernam_key)
generate_key_button.pack()

encrypt_button = tk.Button(app, text="Зашифровать", command=encrypt_button_clicked)
encrypt_button.pack()

decrypt_button = tk.Button(app, text="Расшифровать", command=decrypt_button_clicked)
decrypt_button.pack()

output_label = tk.Label(app, text="Результат:")
output_label.pack()

output_text = tkst.ScrolledText(app, width=40, height=5)
output_text.pack()

copy_button = tk.Button(app, text="Копировать", command=copy_text)
copy_button.pack()

paste_button = tk.Button(app, text="Вставить", command=paste_text)
paste_button.pack()

app.mainloop()
