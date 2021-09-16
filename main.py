import hashlib, string, random
# print(f'Hi, {name}')

# num_of_bits_for_tests = {8, 12, 16, 24, 32}
num_of_bits_for_tests = {8, 12, 16, 24}
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
    attempts = 0
    hashes = set()

    while True:
        hash = my_sha_1(random_word(), num_bits)

        if hashes.__contains__(hash):
            return attempts
        else:
            hashes.add(hash)
            attempts += 1


def run_collision_attack_test():
    results = {}

    for num_bits in num_of_bits_for_tests:
        # print(f'num_bits: {num_bits}')
        num_attempts = set()

        for i in range(num_of_test_iter):
            # print(f'i: {i}')
            num_attempts.add(collision_attack(num_bits))

        results[num_bits] = num_attempts
        print(f'Attempts for {num_bits}: {num_attempts}'
              f'\nAverage num attempts: {sum(num_attempts) / len(num_attempts)}'
              f'\nExpected num of attempts: {2 ** (num_bits / 2)}'
              f'\nLargest Value: {max(num_attempts)}'
              f'\nSmallest Value: {min(num_attempts)}\n\n')

    # Todo: make pretty charts and stuff from results


def pre_image_attack(num_bits):
    attempts = 0
    hash = my_sha_1(random_word(), num_bits)

    while True:
        attempts += 1

        new_hash = my_sha_1(random_word(), num_bits)

        if hash == new_hash:
            return attempts


def run_pre_image_attack_test():
    results = {}

    for num_bits in num_of_bits_for_tests:
        # print(f'num_bits: {num_bits}')
        num_attempts = set()

        for i in range(num_of_test_iter):
            # print(f'i: {i}')
            num_attempts.add(pre_image_attack(num_bits))

        results[num_bits] = num_attempts
        print(f'Attempts for {num_bits}: {num_attempts}'
              f'\nAverage num attempts: {sum(num_attempts) / len(num_attempts)}'
              f'\nExpected num of attempts: {2 ** (num_bits / 2)}'
              f'\nLargest Value: {max(num_attempts)}'
              f'\nSmallest Value: {min(num_attempts)}\n\n')

    # Todo: make pretty charts and stuff from results



if __name__ == '__main__':
    # string_to_hash = input("String to hash: ")
    # num_bits = int(input("Num bits: "))

    # print(my_sha_1(string_to_hash, num_bits))
    # print(collision_attack(32))
    # print(pre_image_attack(12))
    # run_pre_image_attack_test()
    run_collision_attack_test()
