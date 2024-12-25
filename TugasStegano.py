from stegano import lsb
import os

def get_image_path():
    while True:
        img_path = input("Masukkan Path Gambar (contoh: c:/path/to/image.png): ")
        if os.path.exists(img_path) and img_path.endswith(('.png', '.jpg')):
            return img_path
        else:
            print("Path gambar tidak valid atau format file salah. Silakan coba lagi.")

def hide_message():
    img_path = get_image_path()
    message = input("Masukkan pesan rahasia yang akan disembunyikan: ")

    save_path = input("Masukkan path untuk menyimpan gambar dengan pesan tersembunyi (contoh: c:/path/to/hidden_image.png): ")
    if not save_path.endswith('.png'):
        print("Format file untuk menyimpan harus .png")
        return

    try:
        secret = lsb.hide(img_path, message)
        secret.save(save_path)
        print(f"Pesan berhasil disembunyikan dalam gambar. Gambar disimpan di: {save_path}")
    except Exception as e:
        print(f"Gagal menyimpan gambar: {e}")

def show_message():
    img_path = get_image_path()

    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
            print(f"Pesan tersembunyi: {clear_message}")
        else:
            print("Tidak ada pesan tersembunyi dalam gambar ini.")
    except Exception as e:
        print(f"Gagal menampilkan pesan dari gambar: {e}")

def main():
    while True:
        print("\nSteganography Tool - Terminal Version")
        print("1. Sembunyikan pesan")
        print("2. Tampilkan pesan")
        print("3. Keluar")
        choice = input("Pilih opsi (1/2/3): ")

        if choice == "1":
            hide_message()
        elif choice == "2":
            show_message()
        elif choice == "3":
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
    main()