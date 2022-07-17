__all__ = ['load_json', 'save_json']

import json
def load_json(file_path):
    """Creates a dictionary object from a file containing JSON formatted string.

    Args:
        file_path ( str ): Path to the file containing JSON string.

    Returns:
        dict: Returns a dictionary object
    """
    with open(file_path) as f:
        obj = json.load(f)
    return obj

def save_json(file_path, object, indent=4):
    """Serializes a dictionary object into a file.

    Args:
        file_path ( str ): Absolute path of the generated output file.
        object ( dict ): Dictionary object that will be serialized into string. Non serializable objects will be output as "<not serializable>" 
        indent ( int ): Indentation used in pretty print. Defaults to 4 spaces.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(object,f, ensure_ascii=False, indent=indent, default = lambda i: '<not serializable>')
