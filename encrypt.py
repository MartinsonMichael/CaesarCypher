import argparse


def decrypt(shift: int):
    s = input()
    decrypted = "".join([
        chr((ord(x) + shift) % 255)
        for x in s
    ])
    print(decrypted)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("shift", type=int, default=3)
    args = parser.parse_args()
    decrypt(args.shift)
