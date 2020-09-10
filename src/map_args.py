from src.map_config import new_feature_branch, new_release_branch
from src.checkout.checkout import checkout
from src.utils import original_git

# 目前支持拦截的git方法
supported = {
    'checkout': checkout,
}

# 根据不同的参数，导向对应的处理方法
def map_args(args, config):
    if not config:
        # 没有配置，直接使用原生git
        original_git(args)
        return
    # 将方法分配到
    func = supported[args[0]] or original_git
    func(args)
