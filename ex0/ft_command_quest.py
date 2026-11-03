#! /usr/bin/env python3

import sys


def my_command_quest() -> None:

    argv = sys.argv
    argc = len(argv)

    print("=== Command Quest ===")
    print(f"Program name: {argv[0]}")

    if argc == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        i = 1
        while i < argc:
            print(f"Argument {i}: {argv[i]}")
            i += 1

    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    my_command_quest()
