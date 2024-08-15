If you can not read Chinese, this repo is totally useless to you.

在国内某引擎的个人版中，当你编辑国际版本的项目时，某些情况下需要修改 meta 文件，而此时引擎会偷偷将文件中的 GUID 加密。经过一段时间后，你可能会发现项目再也无法使用原版引擎打开，只能被迫购买正式版。然而，这一点在官方文档中从未提及。这种先让人上车再悄悄把车门焊死的行为，实在令人无语。

本工具的作用是让你在最后一刻决定跳车。使用该工具前，需要在电脑上安装 Python3，并运行 `pip3 install cryptography` 安装相关依赖。然后，只需执行以下命令：

```bash
python3 tiaoche.py <your_unity_project_path>

特别感谢 ChatGPT 的支持，所有代码均由其生成，甚至本 README 也是它写的。
