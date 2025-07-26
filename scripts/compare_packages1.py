#!/usr/bin/env python3

import sys

def read_packages(file_path):
    with open(file_path) as f:
        return set(line.split()[0] for line in f if line.strip())

def compare_package_lists(working_file, nonworking_file, plain=False):
    working_pkgs = read_packages(working_file)
    nonworking_pkgs = read_packages(nonworking_file)

    only_in_working = sorted(working_pkgs - nonworking_pkgs)

    if only_in_working:
        header = "Packages present in working system but missing in nonworking:"
        print(f"\n{header}")
        for pkg in only_in_working:
            print(f"  {pkg}")
    else:
        print("No missing packages from nonworking system.")

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2 or len(args) > 3:
        print("Usage: python3 compare_packages.py <working_file> <nonworking_file> [--plain]")
        sys.exit(1)

    working_file = args[0]
    nonworking_file = args[1]
    plain_output = '--plain' in args

    compare_package_lists(working_file, nonworking_file, plain_output)
