import hashlib
# print(f'Hi, {name}')


def my_sha_1(string_to_hash, num_bits):
    digest = hashlib.sha1(string_to_hash.encode('utf-8')).hexdigest()
    digest_truncated = digest  # todo: truncate the digest to the num of bits
    return digest_truncated


if __name__ == '__main__':
    string_to_hash = input("String to hash: ")
    num_bits = int(input("Num bits: "))

    print(my_sha_1(string_to_hash, num_bits))
