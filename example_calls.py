import requests


def encrypt_data(base_url, password, key):
    encrypt_url = base_url + "/encrypt"
    data = {
        "password": password,
        "key": key
    }
    response = requests.post(encrypt_url, json=data)

    if response.status_code == 200:
        encrypted_data = response.json()
        return encrypted_data['encrypted_password']
    else:
        print("Failed to encrypt data. Status code:", response.status_code)
        return None


def decrypt_data(base_url, encrypted_password, key):
    decrypt_url = base_url + "/decrypt"
    data = {
        "encrypted_password": encrypted_password,
        "key": key
    }
    response = requests.post(decrypt_url, json=data)

    if response.status_code == 200:
        decrypted_data = response.json()
        return decrypted_data['decrypted_password']
    else:
        print("Failed to decrypt data. Status code:", response.status_code)
        return None


if __name__ == "__main__":
    base_url = "http://127.0.0.1:9001"
    password = "secret-password"
    key = "encryption-key"

    encrypted_password = encrypt_data(base_url, password, key)
    if encrypted_password:
        print("Encrypted Data:", encrypted_password)

    decrypted_password = decrypt_data(base_url, encrypted_password, key)
    if decrypted_password:
        print("Decrypted Data:", decrypted_password)
