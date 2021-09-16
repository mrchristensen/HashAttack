import hashlib, string, random
# print(f'Hi, {name}')

num_of_bits_for_tests = {8, 12, 16, 24, 32}
num_of_test_iter = 100


def random_word():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(16))


def my_sha_1(string_to_hash, num_bits):  # https://www.kite.com/python/examples/3150/hashlib-construct-a-sha1-hash
    hex_digest = hashlib.sha1(string_to_hash.encode('utf-8')).hexdigest()
    bin_digest = bin(int(hex_digest, base=16)).lstrip('0b')
    digest_truncated = bin_digest[0:num_bits]
    return digest_truncated


def collision_attack(num_bits):
    hashes = set()
    attempts = 0

    while True:
        attempts += 1
        hash = my_sha_1(random_word(), num_bits)

        if hashes.__contains__(hash):
            return attempts
        else:
            hashes.add(hash)


if __name__ == '__main__':
    # string_to_hash = input("String to hash: ")
    # num_bits = int(input("Num bits: "))

    # print(my_sha_1(string_to_hash, num_bits))
    print(collision_attack(12))
