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
# Last Modified: 2022-02-17 12:22:19 am                                        #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2022 Zacks Shen                                                #
################################################################################


import os
import json


inputfile = 'leetcode_sql.json'
outputfile = 'output.txt'


def parser():
    with open(inputfile, 'r') as f:
        sql = json.load(f)
    with open(outputfile, 'a') as f:
        for tb, rows in sql['rows'].items():
            for row in rows:
                columns = ', '.join(sql['headers'][tb])
                values = ', '.join(map(lambda x: f'"{x}"', row))
                insert_statement = f"""insert into {tb} ({columns}) values ({values});"""
                f.write(insert_statement + "\n")


def main():
    if os.path.exists(outputfile):
        os.remove(outputfile)
    if os.path.exists(inputfile):
        if os.path.getsize('leetcode_sql.json'):
            parser()
        else:
            print(
                f'Please paste the SQL statement from your LeetCode test case to {inputfile}'
            )
    else:
        with open(inputfile, 'w') as f:
            f.write('')
            print('The program has created a json file for you at the same directory.')
            print(f'Please paste the SQL statement from your LeetCode test case to {inputfile}')


if __name__ == '__main__':
    main()
