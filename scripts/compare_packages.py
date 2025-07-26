#!/usr/bin/env python3

import sys

def read_packages(file_path):
    with open(file_path) as f:
        return set(line.split()[0] for line in f if line.strip())

def compare_package_lists(working_file, nonworking_file):
    working_pkgs = read_packages(working_file)
    nonworking_pkgs = read_packages(nonworking_file)

    only_in_working = sorted(working_pkgs - nonworking_pkgs)
    only_in_nonworking = sorted(nonworking_pkgs - working_pkgs)

    print(f"\n✅ Packages present in working system but missing in nonworking:")
    for pkg in only_in_working:
        print(f"  {pkg}")

    print(f"\n⚠️ Packages present in nonworking system but not in working:")
    for pkg in only_in_nonworking:
        print(f"  {pkg}")

    print(f"\n📦 Common packages: {len(working_pkgs & nonworking_pkgs)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 compare_packages.py <working_file> <nonworking_file>")
        sys.exit(1)

    compare_package_lists(sys.argv[1], sys.argv[2])
