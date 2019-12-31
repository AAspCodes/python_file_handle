"""Some examples of how to read, write and append a file. """


def read_from_file():
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
