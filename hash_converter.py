# DATA BASE FOR HASHES MD5
import hashlib
def sha_hash(filename):
    try:
        with open(filename, "rb") as f:
            bytes = f.read()
            shash = hashlib.sha256(bytes).hexdigest()
            f.close()
        return shash
    except:
        return 0
