import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
import base64

class DESApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DES Encryption/Decryption")
        self.key = None

        # GUI Components
        tk.Label(root, text="Key (8 characters):").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.key_entry = tk.Entry(root, width=30)
        self.key_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Message:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="Result:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.result_entry = tk.Entry(root, width=50, state='readonly')
        self.result_entry.grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        tk.Button(root, text="Encrypt", command=self.encrypt_message).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(root, text="Decrypt", command=self.decrypt_message).grid(row=3, column=1, padx=10, pady=10, sticky="w")

    def encrypt_message(self):
        key = self.key_entry.get()
        if len(key) != 8:
            messagebox.showerror("Error", "Key must be 8 characters long!")
            return

        message = self.message_entry.get()
        if not message:
            messagebox.showerror("Error", "Message cannot be empty!")
            return

        try:
            cipher = DES.new(key.encode(), DES.MODE_ECB)
            padded_message = pad(message.encode(), DES.block_size)
            encrypted_message = cipher.encrypt(padded_message)
            encoded_message = base64.b64encode(encrypted_message).decode()

            self.result_entry.config(state='normal')
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, encoded_message)
            self.result_entry.config(state='readonly')
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt_message(self):
        key = self.key_entry.get()
        if len(key) != 8:
            messagebox.showerror("Error", "Key must be 8 characters long!")
            return

        encrypted_message = self.message_entry.get()
        if not encrypted_message:
            messagebox.showerror("Error", "Encrypted message cannot be empty!")
            return

        try:
            cipher = DES.new(key.encode(), DES.MODE_ECB)
            decoded_message = base64.b64decode(encrypted_message)
            decrypted_message = unpad(cipher.decrypt(decoded_message), DES.block_size).decode()

            self.result_entry.config(state='normal')
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, decrypted_message)
            self.result_entry.config(state='readonly')
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DESApp(root)
    root.mainloop()
