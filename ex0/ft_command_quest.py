#!/usr/bin/env python3
import sys


def command_quest() -> None:
    """
    This function prints the program name, counts the number of arguments
    shows each argument and its index and prints total number
    of argument including program name"
    """
    print("=== Command Quest ===\n")
    arg_count = len(sys.argv)
    if arg_count == 1:
        print("No arguments provided!")
    program_name = sys.argv[0]
    print(f"Program name: {program_name}")
    if arg_count > 1:
        print(f"Arguments received: {arg_count - 1}")
        for i in range(1, arg_count):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {arg_count}\n")


if __name__ == "__main__":
    command_quest()
