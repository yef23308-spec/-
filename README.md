# 猜数字游戏

这是我的第一个 Python 小项目。

程序会随机生成一个 1 到 100 之间的数字。你输入猜测后，程序会提示太大、太小，直到你猜对为止。

## 运行方法

在这个文件夹里打开终端，然后运行：

```powershell
python main.py
```

如果 `python` 命令暂时不可用，也可以运行：

```powershell
C:\Users\39729\AppData\Local\Programs\Python\Python314\python.exe main.py
```

## 文件说明

- `main.py`：游戏主程序
- `test_game.py`：测试猜数字规则
- `README.md`：项目说明
- `LICENSE`：开源许可证

## 我学到了什么

- `print()` 输出文字
- `input()` 接收用户输入
- 变量保存数据
- `if / elif / else` 判断
- `while` 循环
- `random.randint()` 生成随机数
- 处理不是数字的输入

## 运行测试

```powershell
python -m unittest test_game.py
```
