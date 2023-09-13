#!/usr/bin/python3
'''Search and update'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts a line of text to a file, after
    each line containing a specific string
    '''
    try:
        with open(filename, 'r') as f_r_only:
            my_text = f_r_only.readlines()
            new_text = []
            for line in my_text:
                new_text.append(line)
                if search_string in line:
                    new_text.append(new_string)
        with open(filename, 'w') as f_w_only:
            f_w_only.write("".join(new_text))

    except FileNotFoundError:
        pass


'''
append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
'''
