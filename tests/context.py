#创建一个测试环境
import os 
import sys 
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(_file_),

import sample
from .context import sample #测试指令（可以在每一个测试环境中导入测试指令）
