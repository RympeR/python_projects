import re
import pyperclip

phoneNumRegex = re.compile(r'''(
    (\d{3})|\(\d{3}\)?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.\s{2,3}?)
    )''', re.VERBOSE)

urlRegex = re.compile(r'''(
            (http://)|(https://)?
            ([a-z]{3,5}[.])?
            ([a-zA-Z-,+_]+)
            ([.][a-zA-Z]{3})
            ([.][a-zA-Z]{2})*
        )''', re.VERBOSE)

persInfoRegex = re.compile(r'''(((\d{4})(\d{12}))|(\d{4}[ ]*){4}?)
                        ''', re.VERBOSE | re.IGNORECASE)

text = pyperclip.paste()
matches = []
sub_text = persInfoRegex.sub(r'\4************', text)
print(sub_text)
for groups in phoneNumRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[0] != '':
        phoneNum += ' x' + groups[0]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
for groups in urlRegex.findall(text):
    matches.append(groups[0])
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('\n'.join(matches))
else:
    print("no nums or email")