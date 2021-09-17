import hashlib
import string
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# num_of_bits_for_tests = {8, 12, 16, 24, 32}
# num_of_bits_for_tests = [8, 12, 16, 24, 32]
num_of_bits_for_tests = [8, 10, 16, 20, 24]
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

    make_line_plot(results, "PlotCol", 34, "Average Attempts for Collision Attack", "collision")

    make_box_plot(results, "BoxCol", "Variation in Attempts for Collision Attack")


def make_box_plot(results, filename, title):
    x = []
    y = []
    for num_bits in results:
        for num in results[num_bits]:
            x.append(num_bits)
            y.append(num)
    sns.boxplot(x, y)
    plt.title(title)
    plt.xlabel("Number of Bytes")
    plt.ylabel("Attempts")
    plt.yscale("log")
    plt.savefig(f'{filename}.png', bbox_inches='tight')
    plt.show()


def make_line_plot(results, filename, max, title, mode):
    x = []
    y = []
    for num_bits in results:
        x.append(num_bits)
        y.append(sum(results[num_bits]) / len(results[num_bits]))
    plt.plot(x, y, linestyle='None', marker="o")
    x = np.linspace(6, max, 100)

    y_equation = None
    if mode == "collision":
        y_equation = 2 ** (x / 2)
    else:
        y_equation = 2 ** x

    plt.plot(x, y_equation, 'r')
    plt.title(title)
    plt.xlabel("Number of Bytes")
    plt.ylabel("Attempts")
    plt.yscale("log")
    plt.savefig(f'{filename}.png', bbox_inches='tight')
    plt.show()


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
            print(f'i: {i}')
            num_attempts.add(pre_image_attack(num_bits))

        results[num_bits] = num_attempts
        print(f'Attempts for {num_bits}: {num_attempts}'
              f'\nAverage num attempts: {sum(num_attempts) / len(num_attempts)}'
              f'\nExpected num of attempts: {2 ** (num_bits / 2)}'
              f'\nLargest Value: {max(num_attempts)}'
              f'\nSmallest Value: {min(num_attempts)}\n\n')

    make_line_plot(results, "PlotPre", 26, "Average Attempts for Pre-Image Attack", "pre-image")
    make_box_plot(results, "BoxPre", "Variation in Attempts for Pre-Image Attack")



if __name__ == '__main__':
    # string_to_hash = input("String to hash: ")
    # num_bits = int(input("Num bits: "))

    # print(my_sha_1(string_to_hash, num_bits))
    # print(collision_attack(32))
    # print(pre_image_attack(12))
    # run_pre_image_attack_test()
    run_pre_image_attack_test()
