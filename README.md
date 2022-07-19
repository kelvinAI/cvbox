## Computer Vision ToolBox  
#### A collection of commonly used tools for general Computer Vision or other Deep Learning projects.

## Installation
```bash
pip install cvbox
```


## File search and filtering utilities
### Utilities to scan files and folders, with options to filter by extension, folders to ignore, etc. Works on both Windows and Linux

```python
from cvbox.search import listfiles, listfiles_gen

dir_to_list = "/path/to/project"

# Store all found files in an array
files = listfiles(dir_to_list)
print(files) # Show all the filtered files in dir_to_list


    
# Only include .jpg, .png and .jpeg files
image_paths = listfiles(dir_to_list, extensions=(".jpg",".png","jpeg"))
print(image_paths)

# Return as string instead of pathlib object
image_paths = listfiles(dir_to_list, extensions=(".jpg",".png","jpeg"),return_as_pathlib=False)
print(image_paths)

# Return filenames only
image_names = listfiles(dir_to_list, extensions=(".jpg",".png","jpeg"),return_filename_only=True)
print(image_names)

# Exclude certain extensions (Should not be used together with extensions= argument)
# List all files in dir_to_list that are not .txt or .doc files.
files_exclude_txt = listfiles(dir_to_list,extensions_exclude=(".txt",".doc")) 


# Use generator and process each file lazily. This works on very large folders with 
# large number (>500k) of files
# Just replace listfiles with listfiles_gen (Same function signature as listfiles)
for f in listfiles_gen(dir_to_list):
    # Operate on files lazily
    print(f)
```

## File IO functions
### Exporting python pickle objects and restoring state from files  
```python
from cvbox.fileio import save_json, load_json, save_pkl, load_pkl

### Quickly serialize/export python objects (can be arrays, dicts, etc) into
### files that can be re-used again (object must be pickle-able)
arr = [1,2,3,4,5]
save_pkl(arr, "arr_output.pkl") # Generates arr_output.pkl in the current directory


arr_loaded = load_pkl("arr_output.pkl") # Restore the array object from file
print(arr_loaded) # [1, 2, 3, 4, 5]
```

### Exporting dictionary objects into JSON text files
```python
dic = [ {"category":"Car","movement": lambda :  "Drive" },
      {"category":"Plane","movement": lambda :  "Fly" }]
save_json("json_output.txt", dic) # Dictionary object is serialized into txt

# Load dictionary from json formatted text
dic_loaded = load_json("json_output.txt")
print(dic_loaded)
# [{'category': 'Car', 'movement': '<not serializable>'},
# {'category': 'Plane', 'movement': '<not serializable>'}]

# Note that non-pickle-able objects such as lambda functions are converted into <not serializable> by default

```
