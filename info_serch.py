from twitter2 import parser


def pershe(twi='_komashka_', info_input_str='location, description'):
    js = dict(parser(twi))
    info_input = ['name, ']
    for i in info_input_str:
        info_input[0] += i
    info_input = info_input[0].split(', ')
    info_to_return = []
    for line in js['users']:
        little = []
        for i in info_input:
            if i not in line: return "Wrong parametr"
            my_line = i + ': ' + line[i]
            little.append(my_line)
        info_to_return.append(little)
    return info_to_return
