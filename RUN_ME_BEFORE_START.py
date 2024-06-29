import os, shutil

# Copied from https://blog.csdn.net/u012206617/article/details/121673782
def alter(file, old_str, new_str):
    # param file: Path to the file to be modified
    # param old_str: String to be replaced
    # param new_str: String to replace with
    # return: None
    with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            if old_str in line:
                line = line.replace(old_str, new_str)
            f2.write(line)
    os.remove(file)
    os.rename("%s.bak" % file, file)

# Copied from https://blog.csdn.net/wuxiaobingandbob/article/details/41516003
def convert(string, space_character = "_"):    
    # param one_string: Original string
    # param space_character: The character used to separate words in the string
    # return: The string with the first word capitalized and the rest in lowercase, separated by the space_character
    string_list = str(string).split(space_character)
    first = string_list[0].lower()
    others = string_list[1:] 
 
    others_capital = [word.capitalize() for word in others]
 
    others_capital[0:0] = [first]
 
    hump_string = ''.join(others_capital)
 
    return hump_string

name = input("Please enter the file name you hope your extension will be named: ")

# Rename "example"s in SConstruct file
alter("SConstruct", "example", name)
# Rename the file name and contents of example.gdextension.gd
target_gdextension_folder = "gdextension/" + name
os.rename("gdextension/example", target_gdextension_folder)
target_gdextension_file = target_gdextension_folder + "/" + name + ".gdextension"
os.rename(target_gdextension_file + "/example.gdextension", )
alter(target_gdextension_file, "example", name)
# Rename the register_types files
alter("src/register_types.h", "EXAMPLE", name.upper())
alter("src/register_types.cpp", "example", name)
alter("src/register_types.cpp", "Example", name.capitalize())
# Rename the example files
os.rename("src/example.cpp", "src/" + name + ".cpp")
os.rename("src/example.h", "src/" + name + ".h")
alter("src/" + name + ".h", "example", name)
alter("src/" + name + ".h", "EXAMPLE", name.upper())
alter("src/" + name + ".cpp", "example", name)
alter("src/" + name + ".cpp", "Example", name.capitalize())
# Rename the doc file
os.rename("src/doc_classes/Example.xml", "src/doc_classes/" + name.capitalize() + ".xml")