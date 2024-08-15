If you can not read Chinese, this repo is totally useless to you.

国内某改版引擎的个人版在编辑国际版本工程的时候，会在需要修改 meta 文件的时候，偷偷把 guid 给加密了。于是你用了一段时间以后就会发现你的工程再也无法无法使用原来的引擎打开了，只能被迫花钱购买他的正式版本。但是他的文档里面从来没有说过这个事情，这种骗人上车又把车门焊死的行为实在是令人无语。

本工具就是用来让你在最后时间后悔跳车的。电脑需要安装 python3，并 pip3 install cryptography，之后只要执行

python3 tiaoche.py <your_unity_project_path>

鸣谢 chatgpt 的支持，代码都是他写的。
