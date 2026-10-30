#! /usr/bin/env python3


def my_command_quest() -> None:

    import sys

    args = sys.argv

    argc = len(args)

    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    if argc == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        i = 1
        while i < argc:
            print(f"Argument {i}: {args[i]}")
            i += 1
    print(f"Total arguments :{argc}\n")


if __name__ == "__main__":
    my_command_quest()
