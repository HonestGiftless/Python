# Pretty print

def pretty_print(data, side='-', delimiter='|'):
    text = ''
    for i in range(len(data)):
        if i != len(data) - 1:
            text += f'{delimiter} {data[i]} '
        else:
            text += f'{delimiter} {data[i]} {delimiter}'
    
    border_text = ' ' + side*(len(text)-2) + ' '

    print(border_text)
    print(text)
    print(border_text)