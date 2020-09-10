import sys
import subprocess
import io
import json
import os
from src.map_args import map_args


def has_git():
    """
    检查是否安装了git
    :return: Boolean
    """
    cmd_result = subprocess.Popen('git --version', shell=True, stderr=subprocess.PIPE, bufsize=-1)
    stderr = io.TextIOWrapper(cmd_result.stderr, encoding='utf-8').read()

    if not stderr:
        return True
    return False

def get_config():
    path = './gitf.config.json'
    if os.path.exists(path):
        with open(path, 'r') as file:
            config_dict = json.load(file)
            return config_dict
    # 没有设置config文件
    return None

if __name__ == '__main__':
    if not has_git():
        tips = 'Can not find git in your machine, please install it first.\nYou can download it here: https://git-scm.com/'
        sys.exit(tips)
    config = get_config()
    if not config:
    
    # 只获取参数
    args = sys.argv[1:]
    # 参数根据配置打到正确的处理句柄
    map_args(args, config)