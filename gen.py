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
import re
import argparse
from pathlib import Path
from pprint import pprint
import shutil
import traceback

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


def get_ignore_files(path, name='.gitignore'):
    """
    获取gitignore文件列表
    :param path: ~/.gen 下的目录
    :param name: 默认名称
    :return: list
    """
    with open(path / Path(name)) as f:
        files = f.readlines()
    files = [file.strip('\n') for file in files if not file.startswith('#') if file]
    files = [file for file in files if file]
    files += ['.git']
    return files


def delete_path_by_ignore(paths, ignores):
    """
    删除路径通过正则匹配
    :param paths:
    :param ignores: .gitignore list
    :return: list
    """
    for path in paths[::]:
        for ignore in ignores:
            if ignore.startswith('*'):
                ignore = '.' + ignore
            if re.search(ignore, path):
                paths.remove(path)
                break
    return paths


def get_cwd():
    """
    get the work dir
    :return: Path
    """
    p = Path.home() / Path('.gen')
    return p


def parser_file_tree(root='.'):
    """
    解析目录树
    :return: list
    """
    paths = []

    def parser(root):
        root_path = Path(root)
        if root_path.is_file():
            print(root_path.resolve_to('~/.git'))
            paths.append(str(root_path.relative_to('~/.git')))
            return
        for path in root_path.iterdir():
            sub_path = Path(path)
            parser(sub_path)

    parser(root)
    return paths


def copy_file(p, name):
    """
    拷贝文件
    将文件一个一个拷贝到目录
    """
    current = Path(p)
    project_path = Path.home() / Path('.gen') / Path(name)
    paths = parser_file_tree(project_path)
    paths = delete_path_by_ignore(paths, get_ignore_files(project_path))
    for path in paths:
        shutil.copy(project_path / Path(path), Path('.') / path)


def gen_files(name):
    p = get_cwd()
    # names = [i for i in os.listdir(p) if Path(i).is_dir()]
    try:
        copy_file(p, name)
    except Exception as e:
        traceback.print_exc()
        print(failed)
        print(e)
    else:
        print(success)


def main():
    parser = argparse.ArgumentParser(description='gen your projects')
    parser.add_argument('name', help='the project you want to gen')

    args = parser.parse_args()
    gen_files(args.name)


if __name__ == '__main__':
    main()
    # paths = parser_file_tree()
    # delete_path_by_ignore(paths, get_ignore_files('gen'))
