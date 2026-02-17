# Custom Action 实现模块
# 在这里导出所有 action 类，供注册中心使用
# 添加新的 Custom Action 后，在此处 import 并加入 __all__ 列表

from .general import MyCustomAction

__all__ = [
    "MyCustomAction",
]
