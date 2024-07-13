# txt_to_dict()

def txt_to_dict():
    file = open('planets.txt', encoding='utf-8')
    file_lines = (line.split('\n') for line in file.read().split('\n\n'))
    dcts = ({item.split(" = ")[0]: item.split(" = ")[1] for item in line} for line in file_lines)

    return dcts