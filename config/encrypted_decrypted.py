from cryptography.fernet import Fernet
from config.secret_keys import telegram_token


def fernet_key():
    key = Fernet.generate_key()
    return Fernet(key)


def encrypt_telegram_key():
    fernetcito = fernet_key()
    token = telegram_token.encode()
    encrypted_token = fernetcito.encrypt(token)
    # decrypt_telegram_token(fernetcito, encrypted_token)
    return decrypt_telegram_token(fernetcito, encrypted_token)


def decrypt_telegram_token(fernetcito, encrypted_token):
    decrypted_telegram_token = fernetcito.decrypt(encrypted_token).decode()
    return decrypted_telegram_token
