#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    tot = 0
    i = 1  # Start from the second argument (index 1)
    while i < len(sys.argv):
        tot += int(sys.argv[i])
        i += 1
    print("{}".format(tot))
