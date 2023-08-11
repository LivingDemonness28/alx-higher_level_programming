#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    argc = len(sys.argv) - 1
    args = sys.argv[1:]

    print("{} argument{}{}".format(argc, "" if argc == 1 else "s", ":" if argc > 0 else "."))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
