"""
python3.4引入pathlib可以很方便的替换之前经常使用的os.path.join
代码更安全，简洁，易读
# doc: https://docs.python.org/3/library/pathlib.html
# readme: https://pymotw.com/3/pathlib/
p.exists()
p.is_dir()
p.parts()
p.chmod()
p.rmdir()
"""

import os
from pathlib import Path

dir = os.getcwd()

path = Path(dir)

test_path = path / 'test'


for image_path in path.iterdir():
	with image_path.open(encoding='utf-8') as f:
		print(f.readlines())

# 递归文件夹的通配符
Path('/path/').glob('**/*.jpg')