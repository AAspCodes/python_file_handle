def read_from_file():
    with open("text_file", "r") as f:
        contents = f.read()
        
    return contents



def write_to_file(text):
    with open("text_file", "w") as f:
        f.write(text)
        

# def append_file(text):
#     with open("text_file", "a+") as f:
#         f.append(text)

        
write_to_file("hello world")
print(read_from_file())
#
# append_file("heelo again")
