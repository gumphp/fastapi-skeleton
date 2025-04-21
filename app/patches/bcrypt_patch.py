"""
为bcrypt模块添加缺失的__about__属性的补丁
"""

import bcrypt
import sys


class DummyAbout:
    """模拟bcrypt.__about__模块"""
    __version__ = getattr(bcrypt, "__version__", "0.0.0")


# 只有当bcrypt模块没有__about__属性时才添加
if not hasattr(bcrypt, "__about__"):
    # 创建模拟的__about__模块
    bcrypt.__about__ = DummyAbout()
    
    # 打印调试信息
    #print("Applied bcrypt patch: added __about__ attribute")