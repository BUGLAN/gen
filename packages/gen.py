import click
import os
from pathlib import Path
import shutil


@click.command()
def hello():
    print('hello', end='')


class AutoGenFile(object):
    path = Path.home() / '.gen'

    def __init__(self, filename, custom=None):
        self.filename = filename
        if custom is not None:
            self.path = Path(custom)

    def copy(self, dst=None):
        src = self.path / self.filename
        if dst is None:
            dst = Path.cwd()

        for child in src.iterdir():
            if child.is_file():
                self._copy_file(child, dst / child.name)
            elif child.is_dir():
                self._copy_dir(child, dst / child.name)

    @staticmethod
    def _copy_file(src, dst):
        return shutil.copyfile(src, dst)

    @staticmethod
    def _copy_dir(src, dst):
        return shutil.copytree(src, dst)
