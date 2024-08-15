from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

key = b"Q2cwAAA9AqaYc6Km"
iv = b"00000000"

backend = default_backend()
cipher = Cipher(algorithms.Blowfish(key), modes.CFB(iv), backend=backend)

def decrypt_guid(encrypted):
    decryptor = cipher.decryptor()
    return (decryptor.update(base64.b64decode(encrypted)) + decryptor.finalize())[:32]

print(decrypt_guid('W3hMtyulAijmxALMih7oT6/lTN6eYQASIvNyaq+/UdyushUItKPn1W0='))
