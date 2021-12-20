import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


files_dict = {}

files = os.listdir()
for data in files:
    file, extention = data.split(".")
    if extention in files_dict:
        files_dict[extention] += [file]
    else:
        files_dict[extention] = [file]


with open(desktop + "/report.txt", "w") as file:
    for extention, files in sorted(files_dict.items()):
        file.writelines('.' + extention + "\n")
        for name in sorted(files):
            file.writelines("- - - " + name + "." + extention + "\n")

