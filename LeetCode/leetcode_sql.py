#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: leetcode_sql.py                                                   #
# File Path: /leetcode_sql.py                                                  #
# Created Date: 2022-02-12                                                     #
# -----                                                                        #
# Company: Zacks Shen                                                          #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2022-02-12 10:35:07 pm                                        #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2022 Zacks Shen                                                #
################################################################################


import os
import json


filename = 'leetcode_sql.json'


def parser():
    with open(filename, 'r') as f:
        sql = json.load(f)
    for tb in sql['rows']:
        for row in sql['rows'][tb]:
            print(f"""insert into {tb} ({', '.join(sql['headers'][tb])}) values ({', '.join(map(lambda x: '"' + str(x) + '"', row))});""")


def main():
    if os.path.exists(filename):
        if os.path.getsize('leetcode_sql.json'):
            parser()
        else:
            print(
                f'Please paste the SQL statement from your LeetCode test case to {filename}'
            )
    else:
        with open(filename, 'w') as f:
            f.write('')
            print('The program has created a json file for you at the same directory.')
            print(f'Please paste the SQL statement from your LeetCode test case to {filename}')


if __name__ == '__main__':
    main()
