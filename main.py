def read_from_file():
    with open("text_file", "r") as f:
        contents = f.read()
    return contents



def write_to_file(text):
    with open("text_file", "w") as f:
        f.write(text)
        

def append_file(text):
    with open("text_file", "a") as f:
        f.write(text)

        

