import tkinter as tk
from tkinter import ttk

class KriptografiApp:
    def __init__(self, root):  # Perbaikan di sini
        self.root = root
        self.root.title("Program Enkripsi & Dekripsi")
        self.root.geometry("600x400")
        
        # Dictionary untuk mapping karakter enkripsi dan dekripsi
        self.enc_map = {
            'a': '!', 'b': '@', 'c': '#', 'd': '$', 'e': '%',
            'f': '^', 'g': '&', 'h': '*', 'i': '(', 'j': ')',
            'k': '-', 'l': '_', 'm': '+', 'n': '=', 'o': '{',
            'p': '}', 'q': '[', 'r': ']', 's': '|', 't': ':',
            'u': ';', 'v': '"', 'w': '<', 'x': '>', 'y': '?',
            'z': '~', ' ': '/'
        }
        
        # Membuat dictionary untuk dekripsi (membalik enc_map)
        self.dec_map = {v: k for k, v in self.enc_map.items()}
        
        # Create tabs
        self.tab_control = ttk.Notebook(root)
        
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.tab1, text='Enkripsi')
        self.tab_control.add(self.tab2, text='Dekripsi')
        self.tab_control.pack(expand=1, fill="both")
        
        # Enkripsi tab
        self.setup_enkripsi_tab()
        
        # Dekripsi tab
        self.setup_dekripsi_tab()
    
    def setup_enkripsi_tab(self):
        # Label dan input untuk plainteks
        tk.Label(self.tab1, text="Masukkan Plainteks:").pack(pady=10)
        self.plaintext_input = tk.Text(self.tab1, height=5, width=50)
        self.plaintext_input.pack(pady=5)
        
        # Button enkripsi
        tk.Button(self.tab1, text="Enkripsi", command=self.encrypt).pack(pady=10)
        
        # Label dan output untuk cipherteks
        tk.Label(self.tab1, text="Hasil Enkripsi (Cipherteks):").pack(pady=10)
        self.cipher_output = tk.Text(self.tab1, height=5, width=50)
        self.cipher_output.pack(pady=5)
    
    def setup_dekripsi_tab(self):
        # Label dan input untuk cipherteks
        tk.Label(self.tab2, text="Masukkan Cipherteks:").pack(pady=10)
        self.cipher_input = tk.Text(self.tab2, height=5, width=50)
        self.cipher_input.pack(pady=5)
        
        # Button dekripsi
        tk.Button(self.tab2, text="Dekripsi", command=self.decrypt).pack(pady=10)
        
        # Label dan output untuk plainteks
        tk.Label(self.tab2, text="Hasil Dekripsi (Plainteks):").pack(pady=10)
        self.plain_output = tk.Text(self.tab2, height=5, width=50)
        self.plain_output.pack(pady=5)
    
    def encrypt(self):
        # Ambil teks dari input
        plaintext = self.plaintext_input.get("1.0", tk.END).strip().lower()
        
        # Proses enkripsi
        ciphertext = ''
        for char in plaintext:
            if char in self.enc_map:
                ciphertext += self.enc_map[char]
            else:
                ciphertext += char
        
        # Tampilkan hasil
        self.cipher_output.delete("1.0", tk.END)
        self.cipher_output.insert("1.0", ciphertext)
    
    def decrypt(self):
        # Ambil teks dari input
        ciphertext = self.cipher_input.get("1.0", tk.END).strip()
        
        # Proses dekripsi
        plaintext = ''
        for char in ciphertext:
            if char in self.dec_map:
                plaintext += self.dec_map[char]
            else:
                plaintext += char
        
        # Tampilkan hasil
        self.plain_output.delete("1.0", tk.END)
        self.plain_output.insert("1.0", plaintext)

if __name__ == "__main__":  # Perbaikan di sini
    root = tk.Tk()
    app = KriptografiApp(root)
    root.mainloop()
