from Crypto.PublicKey import RSA

key = RSA.generate(2048)
enc_privkey = key.export_key()
enc_pubkey = key.export_key()

with open('private.key', 'wb') as f:
    f.write(enc_privkey)

with open('public.key', 'wb') as f:
    f.write(enc_pubkey)