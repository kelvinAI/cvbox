import os

__all__ = ['setumask']

def setumask(mask=0o077):
    """Sets umask to specified octal value. Used to protect intellectual property on shared resources such as HPC.

    Args:
        mask (Octal, optional): The umask value to set to, in Octal format (0oXXX). Defaults to 0o077.
    """
    os.umask(mask)