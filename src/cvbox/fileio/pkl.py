__all__ = ['save_pkl', 'load_pkl']

import pickle

def save_pkl(_obj, file_path, protocol=2):
    """Serialize a python object into a file.

    Args:
        _obj ( Any ): Any object that can be serialized, such as dictionaries or arrays.
        filename ( str ): Absolute path to the output file.
        protocol (int, optional): Pickle dump protocol. Defaults to 2.
    """
    with open(file_path, 'wb') as f:
        pickle.dump(_obj, f, protocol=protocol)
        
def load_pkl(file_path):
    """Loads a python object from a file.

    Args:
        file_path ( str ): Absolute path of the pickle file on disk to be loaded.

    Returns:
        Object: Returns the python object loaded from disk. Object type depends on contents of the pickled file.
    """
    with open(file_path, 'rb') as f:
        obj = pickle.load(f)
    return obj

