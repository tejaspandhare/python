#!/usr/bin/env python3

import sys

def read_packages(file_path):
    with open(file_path) as f:
        return set(line.split()[0] for line in f if line.strip())

def compare_package_lists(working_file, nonworking_file, plain=False):
    working_pkgs = read_packages(working_file)
    nonworking_pkgs = read_packages(nonworking_file)

    only_in_working = sorted(working_pkgs - nonworking_pkgs)
    only_in_nonworking = sorted(nonworking_pkgs - working_pkgs)

    prefix = "" if plain else "✅ "
    if only_in_working:
        print(f"\n{prefix}Packages present in working system but missing in nonworking:")
        for pkg in only_in_working:
            print(f"  {pkg}")

#    if only_in_nonworking:
#        prefix = "" if plain else "⚠️ "
#        print(f"\n{prefix}Packages present in nonworking system but not in working:")
#        for pkg in only_in_nonworking:
#            print(f"  {pkg}")

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2 or len(args) > 3:
        print("Usage: python3 compare_packages.py <working_file> <nonworking_file> [--plain]")
        sys.exit(1)

    working_file = args[0]
    nonworking_file = args[1]
    plain_output = '--plain' in args

    compare_package_lists(working_file, nonworking_file, plain_output)
