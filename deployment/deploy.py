### Before running this script, please make sure you've installed the following Pythondependencies: ###
### case-convert
### re

import os, re
from case_convert import pascal_case, snake_case

### Copied from https://blog.csdn.net/u012206617/article/details/121673782 ###
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

def godot_pascal(string):
    
    s = pascal_case(string)
    for i in range(len(s)):
        if i > 0 and s[i - 1] in "0123456789":
            # Copied from https://blog.csdn.net/qq_41542989/article/details/119054359 #
            s = list(s)
            s[i] = s[i].capitalize()
            s = ''.join(s)
            break

    return s

original_name = "example" 
answer = input("Do you want to rename the \"example\" extension? (y/n) ").lower()
if answer == "y":
    pass
elif answer == "n":
    original_name = snake_case(input("Please enter the old name of your extension: "))
else:
    print("Invalid input, exiting and please restart the script.")
    exit()

name = snake_case(input("Please enter the file name you hope your extension will be named: "))
errors = 0

# Prepare the variables for renaming
original_name_upper = original_name.upper()
name_upper = name.upper()
original_name_pascal = godot_pascal(original_name)
name_pascal = godot_pascal(name)

# Rename orignal_names in SConstruct file
alter("SConstruct", original_name, name)
# Rename the file name and contents of {}.gdextension.gd
gdextension_dir = "gdextensions/{}/".format(original_name)
target_gdextension_dir = "gdextensions/{}/".format(name)
gdextension_file = target_gdextension_dir + "bin/{}.gdextension".format(original_name)
target_gdextension_file = target_gdextension_dir + "bin/{}.gdextension".format(name)
gdextension_icon = target_gdextension_dir + "bin/{}.svg".format(original_name)
target_gdextension_icon = target_gdextension_dir + "bin/{}.svg".format(name)

if os.path.exists(gdextension_dir):

    os.rename(gdextension_dir, target_gdextension_dir)

    if os.path.exists(gdextension_file):

        os.rename(gdextension_file, target_gdextension_file)
        alter(target_gdextension_file, original_name_pascal, name_pascal)
        alter(target_gdextension_file, original_name, name)

        os.rename(gdextension_icon, target_gdextension_icon)

        print("Successfully renamed gdextensions/{}/bin/ files and updated contents.".format(original_name))
    
    else:
        print("Error: {}.gdextension file not found in bin folder, skipped...".format(original_name))
        errors += 1

    

# Rename the register_types files
alter("src/register_types.h", original_name_upper, name_upper)
alter("src/register_types.cpp", original_name, name)
alter("src/register_types.cpp", original_name_pascal, name_pascal)
print("Successfully renamed src/register_types files and updated contents.")

# Rename the {} files
h_file = "src/{}.h".format(original_name)
target_h_file = "src/{}.h".format(name)
cpp_file = "src/{}.cpp".format(original_name)
target_cpp_file = "src/{}.cpp".format(name)

if os.path.exists(h_file):
    os.rename(h_file, target_h_file)
    alter(target_h_file, original_name, name)
    alter(target_h_file, original_name_upper, name_upper)
    print("Successfully renamed src/{}.h file and updated contents.".format(original_name))
else:
    print("Error: src/{}.h file not found in bin folder, skipped...".format(original_name))
    errors += 1

if os.path.exists(cpp_file):
    os.rename(cpp_file, target_cpp_file)
    alter(target_cpp_file, original_name, name)
    alter(target_cpp_file, original_name_pascal, name_pascal)
    print("Successfully renamed src/{}.cpp file and updated contents.".format(original_name))
else:
    print("Error: src/{}.cpp file not found in bin folder, skipped...".format(original_name))
    errors += 1

# Rename the doc file
doc_file = "src/doc_classes/{}.xml".format(original_name_pascal)
target_doc_file = "src/doc_classes/{}.xml".format(name_pascal)

if os.path.exists(doc_file):
    alter(doc_file, original_name_pascal, name_pascal)
    os.rename(doc_file, target_doc_file)
    print("Successfully renamed src/doc_classes/{}.xml file and updated contents.".format(original_name_pascal))
else:
    print("Error: src/doc_classes/{}.xml file not found in bin folder, skipped...".format(original_name_pascal))
    errors += 1

# Print ending message
if errors == 0:
    print("Successfully renamed files and updated contents.")
else:
    print("Renamed some files successfully, but some errors occurred during renaming. Please check the output for details.")