"""Some examples of how to read, write and append a file. """


# option 1
def read_from_file():
    f = open("text_file", "r")
    contents = f.read()
    f.close()
    return contents


def write_to_file(text):
    f = open("text_file", "w")
    f.write(text)
    f.close()


def append_file(text):
    f = open("text_file", "a")
    f.write(text)
    f.close()


# option 2
"""Using 'with open' automatically closes the file when indentation
 is in line with the 'with' keyword."""


def with_read_from_file():
    with open("text_file", "r") as f:
        contents = f.read()
    return contents


def with_write_to_file(text):
    with open("text_file", "w") as f:
        f.write(text)


def with_append_file(text):
    with open("text_file", "a") as f:
        f.write(text)
