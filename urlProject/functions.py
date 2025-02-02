
import base64
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def pad(string):
        """Función que asegura que el texto sea múltiplo de 16 bytes (AES necesita bloques de 16)"""
        result = string + (16 - len(string) % 16) * chr(16 - len(string) % 16) 
        return result

def AESCipher128Cbc(string, AESKey):
    
    bytesKey   = AESKey.encode('utf-8')[:16] # Convertir clave a bytes (debe tener exactamente 16 bytes)
    iv         = os.urandom(16) # Generar un IV aleatorio de 16 bytes
    paddedText = pad(string).encode('utf-8')

    cipher     = Cipher(algorithms.AES(bytesKey), modes.CBC(iv), backend = default_backend()) # Configurar AES en modo CBC
    encryptor  = cipher.encryptor()
    cipherText = encryptor.update(paddedText) + encryptor.finalize()

    base64Result = base64.b64encode(iv + cipherText).decode('utf-8') # Codifica el resultado en Base64
    
    return base64Result

def stringSanitizer(string):
      """Función para cambiar /, + y = por %2F, %2B y %3D, respectivamente"""
      result = string.replace("=","%3D").replace("/","%2F").replace("+","%2B")
      return result
      
