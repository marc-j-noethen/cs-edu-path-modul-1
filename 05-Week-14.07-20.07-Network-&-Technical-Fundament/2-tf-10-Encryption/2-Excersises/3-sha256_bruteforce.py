import hashlib
import itertools
import string


def sha256_text(text):
    return hashlib.sha256(text.encode()).hexdigest()


def brute_force_sha256(target_hash, max_length=4):
    alphabet = string.ascii_lowercase
    for length in range(1, max_length + 1):
        for chars in itertools.product(alphabet, repeat=length):
            candidate = "".join(chars)
            if sha256_text(candidate) == target_hash:
                return candidate
    return None


if __name__ == "__main__":
    target = sha256_text("pass")
    print(brute_force_sha256(target, 4))
