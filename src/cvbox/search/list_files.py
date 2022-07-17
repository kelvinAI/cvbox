
__all__ = ["listfiles","listfiles_gen", "lsfn"]

from os import walk
from pathlib import Path

def strs_exist_in(str_patterns: list, target_string: str):
    """Check if any string pattern exist (supplied in a List or Tuple) in a string

    Args:
        str_patterns (List or Tuple of strings): An iterable containing string patterns to check.
        target_string (str): The target string to check if any of the string patterns exist.

    Returns:
        bool : If the target string contains any of the string patterns, returns True. Else returns False
    """
    for s in str_patterns:
        if s in target_string:
            return True
    return False

FOLDER_IGNORE_PATTERNS= ('.ipynb_checkpoints','__pycache__')
def listfiles(root,extensions=None, extensions_exclude=None, return_filename_only=False, return_as_pathlib=True, ignore_folders=FOLDER_IGNORE_PATTERNS):
    """List files from a root directory recursively, stops recursion into folders by pattern matching and also option to filter by extensions.

    Args:
        root ( str ): Absolute path to where file scanning will begin, recursively.
        extensions ( list|tuple, optional): List or Tuple of file extensions to filter by. If not None, the results will only include files that ends with the given extensions.
            Example: (".jpg",".png") all files that does not end with .jpg or .png. will NOT show up in the search results. Defaults to None.
            If set as None (default), files with any extension will be included in the results. If this is set, extensions_exclude should be redundant.
        extensions_exclude (list|tuple, optional): List or tuple of strings to be specifically Excluded from the search results. Eg. If set as (".txt"),
            all files ending with ".txt" will not be included in the search results. Typically used to filter a minority of files and retain the majority.
        return_filename_only (bool, optional): True to return filename only. Otherwise return the full path relative to the root folder. Defaults to False.
        return_as_pathlib (bool, optional): True to return as pathlib object. False returns the string representation. Defaults to True.
        ignore_folders ( list|tuple, optional): List or tuple of folder patterns to ignore. If any folder name matches, the folder is skipped and
            it will not further recurse into its subfolders. Can be used to prevent recursing into cache directories such as .ipynb_notebooks. 
            Defaults to ('.ipynb_checkpoints','__pycache__')

    Returns:
        list: List of files obtained from the search
    """
    files = []
    for dirpath, dirnames, filenames in walk(root):
        # Skip recursion into these folders
        if strs_exist_in(ignore_folders, dirpath): continue
        for f in filenames:
            if extensions and not f.lower().endswith(extensions): continue
            if extensions_exclude and f.lower().endswith(extensions_exclude): continue
            # Stick to using Pathlib although loading is slower, however it will work on windows as well as linux
            # Instead of hard coding the path separator
            file = Path(dirpath)/f
            if return_filename_only:
                # Should be relative to root path
                file = str(file.relative_to(root)) 
                # file = file.name
            if not return_as_pathlib:
                file = str(file)
            files.append(file)
    return files

def listfiles_gen(root,extensions=None, extensions_exclude=None, return_filename_only=False, return_as_pathlib=True, ignore_folders=FOLDER_IGNORE_PATTERNS):
    """List files from a root directory recursively, stops recursion into folders by pattern matching and also option to filter by extensions. Same as listfiles 
    but returns a Generator object instead.

    Args:
        root ( str ): Absolute path to where file scanning will begin, recursively.
        extensions ( list|tuple, optional): List or Tuple of file extensions to filter by. If not None, the results will only include files that ends with the given extensions.
            Example: (".jpg",".png") all files that does not end with .jpg or .png. will NOT show up in the search results. Defaults to None.
            If set as None (default), files with any extension will be included in the results. If this is set, extensions_exclude should be redundant.
        extensions_exclude (list|tuple, optional): List or tuple of strings to be specifically Excluded from the search results. Eg. If set as (".txt"),
            all files ending with ".txt" will not be included in the search results. Typically used to filter a minority of files and retain the majority.
        return_filename_only (bool, optional): True to return filename only. Otherwise return the full path relative to the root folder. Defaults to False.
        return_as_pathlib (bool, optional): True to return as pathlib object. False returns the string representation. Defaults to True.
        ignore_folders ( list|tuple, optional): List or tuple of folder patterns to ignore. If any folder name matches, the folder is skipped and
            it will not further recurse into its subfolders. Can be used to prevent recursing into cache directories such as .ipynb_notebooks. 
            Defaults to ('.ipynb_checkpoints','__pycache__')

    Yields:
        Path | str : Yields a pathlib object or str for each file 
    """
    for dirpath, dirnames, filenames in walk(root):
        # Skip recursion into these folders
        if strs_exist_in(ignore_folders, dirpath): continue
        for f in filenames:
            if extensions and not f.lower().endswith(extensions): continue
            if extensions_exclude and f.lower().endswith(extensions_exclude): continue
            # Stick to using Pathlib although loading is slower, however it will work on windows as well as linux
            # Instead of hard coding the path separator
            file = Path(dirpath)/f
            if return_filename_only:
                # Should be relative to root path
                file = str(file.relative_to(root)) 
                # file = file.name
            if not return_as_pathlib:
                file = str(file)
            yield file
            
def lsfn(generator=False):
    if generator:
        return listfiles
    return listfiles_gen 