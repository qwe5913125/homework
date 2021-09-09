def read_file(nam):
    try:
        f = open(nam)
        content = f.read()
    finally:
        f.close()
    return content


print(read_file("text.txt"))
