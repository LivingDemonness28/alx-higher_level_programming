#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    i = 0
    while i < len(names):
        if names[i][:2] != "__":
            print(names[i])
        i += 1
