import hashlib
# print(f'Hi, {name}')

number_or_bits_for_tests = {8, 12, 16, 24, 32}

def my_sha_1(string_to_hash, num_bits):  # https://www.kite.com/python/examples/3150/hashlib-construct-a-sha1-hash
    hex_digest = hashlib.sha1(string_to_hash.encode('utf-8')).hexdigest()
    bin_digest = bin(int(hex_digest, base=16)).lstrip('0b')
    digest_truncated = bin_digest[0:num_bits]
    return digest_truncated


if __name__ == '__main__':
    string_to_hash = input("String to hash: ")
    num_bits = int(input("Num bits: "))

    print(my_sha_1(string_to_hash, num_bits))
