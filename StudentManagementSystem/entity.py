import base64, hashlib, secrets

def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)
    password_hash = hashlib.scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=2**14,
        r=8,
        p=1,
        dklen=64,
    )
    encoded_salt = base64.b64encode(salt).decode("ascii")
    encoded_hash = base64.b64encode(password_hash).decode("ascii")
    return f"scrypt${encoded_salt}${encoded_hash}"

hashPassword = hash_password()