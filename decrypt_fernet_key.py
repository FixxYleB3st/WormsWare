from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


with open("logs/fernet_key.txt", "rb") as f:
    rkey = f.read()

private_key = RSA.import_key(open("private.key").read())
cipher_rsa = PKCS1_OAEP.new(private_key)

dec_key = cipher_rsa.decrypt(rkey)

with open("logs/fernet_key.txt","wb") as f:
    f.write(dec_key)