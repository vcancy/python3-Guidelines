"""
python3 能指定变量的类型，IDE会根据类型定义检测(只会警告)

"""
def fun(word:str):
	print(f'hi{word}')

fun(None)
