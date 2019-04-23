#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
usage: gen name [-n] a=name
# __version__ = '2019.4.22'

# 流程
1. 检测是否存在'~/.gen' dir 不存在则抛出异常
2.
"""
import os
import argparse
from pathlib import Path
import shutil

success = """
███████╗██╗   ██╗ ██████╗ ██████╗███████╗███████╗███████╗
██╔════╝██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
███████╗██║   ██║██║     ██║     █████╗  ███████╗███████╗
╚════██║██║   ██║██║     ██║     ██╔══╝  ╚════██║╚════██║
███████║╚██████╔╝╚██████╗╚██████╗███████╗███████║███████║
╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝
"""

failed = """
███████╗ █████╗ ██╗██╗     ███████╗██████╗
██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
█████╗  ███████║██║██║     █████╗  ██║  ██║
██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
██║     ██║  ██║██║███████╗███████╗██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝
"""


def get_cwd():
    # get the work dir
    p = Path.home() / Path('.gen')
    return p


def copy_files(p, name):
    for file in os.listdir(p / name):
        if (p / Path(name) / Path(file)).is_dir():
            shutil.copytree(str(p / Path(name) / Path(file)), str(Path.cwd() / Path(file).name))
        else:
            shutil.copy(str(p / Path(name) / Path(file)), str(Path.cwd() / Path(file).name))



def gen_files(name):
    p = get_cwd()
    # names = [i for i in os.listdir(p) if Path(i).is_dir()]
    try:
        copy_files(p, name)
    except Exception as e:
        print(failed)
        print(e)
    else:
        print(success)


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    # parser.add_argument('--name', help='gen files name')
    # parser.add_argument('-n', help='gen files name')
    parser.add_argument('name', help='name')

    args = parser.parse_args()
    gen_files(args.name)


if __name__ == '__main__':
    main()
