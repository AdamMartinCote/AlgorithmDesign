import sys
from contextlib import contextmanager
from io import StringIO


@contextmanager
def capture_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def get_exemplaire_path_from_name(name: str) -> str:
    return f'../exemplaires/{name}.txt'

