"""
工具类
@author iimT 2020.09.10
"""

import re

def git_diff(branch_a, branch_b):
    
    return

# 检查args是否与给出的规则相匹配
def check_args(args, rules):
    args_string = "".join(args)
    for rule in rules:
        print(rule, args_string, bool(re.search(rule, args_string)))
    return True

def original_git(args):
    print('执行原生git: git ' + "".join(args))
    return