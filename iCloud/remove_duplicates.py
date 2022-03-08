#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: remove_duplicates.py                                              #
# File Path: /remove_duplicates.py                                             #
# Created Date: 2022-02-15                                                     #
# -----                                                                        #
# Company: Zacks Shen                                                          #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2022-03-08 3:35:39 pm                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2022 Zacks Shen                                                #
################################################################################

import os
import sys
import time


def remove_duplicates(dirpath, filenames, mark=2):
    """remove_duplicates removes the duplicated files or dirs with specific mark that marked by MacOS.

    Args:
        mark (int, optional): The mark of duplicate files or dirs. Defaults to 2.
    """
    os.chdir(dirpath)
    files = sorted(filenames)

    duplicates, new_files = [], []
    for f in files:
        if f' {mark}' in f:
            duplicates.append(f)
        else:
            new_files.append(f)

    # duplicates may be:
    # - xx 2.doc
    # - xx.yy 2.doc
    # - xx 2
    # - .xx 2.doc.icloud
    # - xx.yy 2.doc.icloud
    # - xx 2.icloud
    for duplicate in duplicates:
        # try:
        #     filename, ext = duplicate.rsplit('.', 1)
        #     filename = filename.rsplit(' 2')[0]
        #     file = filename + '.' + ext
        # except ValueError:
        #     filename = duplicate.rsplit(' 2')[0]
        #     file = filename
        try:
            filename, ext = duplicate.rsplit(' 2', 1)
            if '.icloud' in ext:
                file = filename + ext
                file = file.split('.icloud')[0] # remove .icloud
                file = file.split('.', 1)[1] # remove ., which makes files hidden
            else:
                file = filename + ext
        except ValueError:
            filename = duplicate.rsplit(' 2')[0]
            file = filename

        # Test only
        # print("duplicate:", duplicate)
        # print("file:", file)
        # print(file in new_files)

        if file in new_files:
            file_size = os.path.getsize(file)
            duplicate_size = os.path.getsize(duplicate)
            file_mtime = os.path.getmtime(file)
            duplicate_mtime = os.path.getmtime(duplicate)

            duplicate_path = os.path.join(dirpath, duplicate)
            # Test only
            # print(file, file_size)
            # print(duplicate, duplicate_size)

            # Remove the old files retrived from iCloud since
            # new files may be larger than old files.
            if (file_size >= duplicate_size) | (file_mtime > duplicate_mtime):
                try:
                    os.remove(duplicate)
                    print(f'{duplicate_path} has been removed!')
                except:
                    print(f'{duplicate_path} cannot removed due to an issue!')
            else:
                print(f'{duplicate_path} cannot be removed since its size larger than or modified time later than {file}.')
                print(f'New file size: {file_size}')
                print(f'Duplicate size: {duplicate_size}')
                print(f'New file modified time: {time.ctime(file_mtime)}')
                print(
                    f'Duplicate modified time: {time.ctime(duplicate_mtime)}')


def main():
    if len(sys.argv) - 1 > 2:
        raise TypeError(f"This program takes 2 positional argument but {len(sys.argv) - 1} were given")
    elif len(sys.argv) - 1 == 0:
        raise TypeError("This program is required to pass a path such as '/Users/username/Desktop'")

    path = sys.argv[1]
    try:
        mark = sys.argv[2]
    except:
        mark = 2

    if not os.path.exists(path):
        raise ValueError(f"{path} is not exists in your machine")

    for dirpath, dirnames, filenames in sorted(os.walk(path, topdown=True)):
        remove_duplicates(dirpath, filenames, mark)


if __name__ == '__main__':
    main()
