import os
import pickle


def print_lol(list_item, intend=False, level=0, fh=sys.stdout):
    for new_list in list_item:
        if isinstance(new_list, list):
            print_lol(new_list, intend, level+1, fh)
        else:
            if intend:
                for tab_space in range(level):
                    print("\t", end='', file=fh)
            print(new_list, file=fh)


os.chdir('D:/file1/file2')

man = []
other = []

try:
    with open('conversation.txt') as conversation:
        for each_line in conversation:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                line_spoken = line_spoken.strip()
                role = role.strip()
                if role == "Man":
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError as err:
    print("file error", err)

try:
    with open('man_said.txt', 'w') as man_file, open('other_man_said.txt', 'w') as other_man_file:
        nester.print_lol(man, fh=man_file)
        nester.print_lol(other, fh=other_man_file)
except IOError as err:
    print("file error", err)
                
            