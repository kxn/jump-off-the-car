#!/usr/bin/env python3
#
#   某国内改版引擎跳车
#
#   本程序用于将某国内改版引擎加密的资产 guid 解密并保存，防止被骗上车下不来。
#
#   需要电脑安装 python3 版本，并 pip3 install cryptography
#  
#   python3 tiaoche.py <your_unity_project_path>
#

import os
import base64
import re
import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# 解密函数
key = b"Q2cwAAA9AqaYc6Km"
iv = b"00000000"

backend = default_backend()
cipher = Cipher(algorithms.Blowfish(key), modes.CFB(iv), backend=backend)

def decrypt_guid(encrypted):
    decryptor = cipher.decryptor()
    return (decryptor.update(base64.b64decode(encrypted)) + decryptor.finalize())[:32].decode()

# 检查和解密 .meta 文件中的 guid 字段
def process_meta_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # 查找 guid 字段
    match = re.search(r'guid:\s*(\S+)', content)
    if match:
        guid = match.group(1)
        
        # 检查是否是合法的Hex字符串（排除这些合法的Hex字符串）
        if re.fullmatch(r'[0-9a-fA-F]{32}', guid):
            return
        
        # 检查是否是合法的Base64编码
        if re.fullmatch(r'[A-Za-z0-9+/=]{22,}', guid):
            try:
                decrypted_guid = decrypt_guid(guid)
                new_content = content.replace(guid, decrypted_guid)

                # 保存解密后的内容
                with open(file_path, 'w') as file:
                    file.write(new_content)
                print(f"解密并更新了文件: {file_path}")
            except Exception as e:
                print(f"解密失败: {file_path}, 错误信息: {e}")

# 遍历指定目录，处理所有 .meta 文件
def process_directory(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".meta"):
                file_path = os.path.join(subdir, file)
                process_meta_file(file_path)

# 主函数，处理命令行输入
def main():
    parser = argparse.ArgumentParser(description="解密Unity项目中的.meta文件中的Base64编码的guid字段")
    parser.add_argument("path", metavar="path", type=str, help="Unity项目的根目录路径")

    args = parser.parse_args()
    process_directory(args.path)

if __name__ == "__main__":
    main()
