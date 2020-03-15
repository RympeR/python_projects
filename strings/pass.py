import sys
import shelve
import pyperclip

""""
    TODO: save passwords into file
    or upgrade old pass project
"""
def operations( serv_name, action='-c', add_new=None,pass_value=None):
    global INFO
    if add_new == '-a':
        INFO[serv_name] = pass_value
    if action == '-c':
        pyperclip.copy(INFO[serv_name])
    elif acton == '-p':
        pyperclip.paste(INFO[serv_name])


INFO = {
    'email' : 'georg.rashkov@gmail.com',
}

if len(sys.argv) < 2:
    print("please enter pytho3 clip.py [pass name] [-c/-p] [add new -a] [pass-value]")
elif len(sys.argv) == 2:
    operations(sys.argv[1])
elif len(sys.argv) == 5:
    operations(sys.arg[1], sys.arg[2], sys.arg[3], sys.arg[4])