def read_file(nam):
    try:
        f = open(nam)
        content = f.read()
    finally:
        f.close()
    return content


def way_better(filename):
    with open(filename) as f: #Контекстный менеджер
        return f.read()

def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as f:
        f.write(content)





write_to_file('text.txt', 'test ivan', 'w')
print(way_better("text.txt"))

