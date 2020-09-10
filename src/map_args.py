from src.map_config import new_feature_branch, new_release_branch
from src.checkout.checkout import checkout
from src.utils import original_git

# 目前支持拦截的git方法
supported = {
    'checkout': checkout,
}

def map_args(args):
    print(args)
    print(supported)
    func = getattr(supported, args[0], original_git)
    func(args)

