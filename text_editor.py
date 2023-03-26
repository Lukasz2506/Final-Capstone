# Text Editor - Notepad style application that can open, edit,
# and save text documents.


def edit(filepath):
    with open(filepath, mode='a') as f:
        f.write(input('Type your text'))

def read(filepath):
    with open(filepath, mode='r') as f:
        f.seek(0)
        text = f.readlines()
    print(text)
filepath = input('type a file location: ')
change = edit(filepath)
whole_text = input('Would you like to see whole text (y / n)?')
if whole_text == 'y'.lower().strip():
    read(filepath)
else:
    pass

