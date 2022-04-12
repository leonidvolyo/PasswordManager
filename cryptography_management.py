import cryptography_keys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

key_object = cryptography_keys.Keys()

print(key_object.get_private_key())   # <cryptography.hazmat.backends.openssl.rsa._RSAPrivateKey object at 0x000001CFAEB38B50>
print(key_object.get_public_key())    # <cryptography.hazmat.backends.openssl.rsa._RSAPublicKey object at 0x000001CFAEB7A430>

def encryption(message):
    ciphertext = key_object.get_public_key().encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decryption(ciphertext):
    plaintext = key_object.get_private_key().decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()



# SOME TESTS
"""encrypted_message = encryption(input("Enter string: ").encode(encoding="utf-8"))
print("It is encrypted")
print("Sending encrypted message")
print(f">>>>>>>>>>>>>>>>>>\n  {encrypted_message}\n >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" )
if input("Do you want do decrypt") == "ok":
    print("Decrypted message:   ")
    print(decryption(encrypted_message))"""