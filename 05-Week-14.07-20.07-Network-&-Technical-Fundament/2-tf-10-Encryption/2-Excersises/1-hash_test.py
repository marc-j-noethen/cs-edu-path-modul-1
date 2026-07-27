import hashlib
from pathlib import Path


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


if __name__ == "__main__":
    file_path = Path("python-installer.exe")
    if file_path.exists():
        print(sha256_file(file_path))
    else:
        print("Place the downloaded installer as python-installer.exe and run again.")
