import hashlib

def hash_string_md5_sha1(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    md5_result = md5_hash.hexdigest()

    sha1_hash = hashlib.sha1()
    sha1_hash.update(md5_result.encode('utf-8'))
    sha1_result = sha1_hash.hexdigest()

    return sha1_result

target_hash = "3657473b03aeefde0725126a6a215749ac6f07fa"

rockyou_file_path = "rockyou.txt"

with open(rockyou_file_path, 'r', errors='ignore') as rockyou_file:
    for line in rockyou_file:
        password = line.strip()
        hashed_password = hash_string_md5_sha1(password)

        if hashed_password == target_hash:
            print(f"Password found: {password}")
            break
