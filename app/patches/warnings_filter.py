"""
过滤特定类型的警告
"""

import warnings
import re


# 过滤bcrypt相关的警告
warnings.filterwarnings("ignore", message=".*error reading bcrypt version.*") 