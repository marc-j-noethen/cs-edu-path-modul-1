import hashlib


def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()


def find_password(target_hash, candidates):
    for candidate in candidates:
        if hash_text(candidate) == target_hash:
            return candidate
    return None


if __name__ == "__main__":
    target = hash_text("pass")
    candidates = ["admin", "password", "test", "pass", "letmein"]
    print(find_password(target, candidates))
