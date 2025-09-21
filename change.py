import os
import re

def fix_empty_image_tags(directory):
    # 编译正则表达式模式，匹配 ![]() 或 ![]
    pattern = r'!\[(.*?)\](?:\((.*?)\))?'
    
    # 遍历目录下的所有 .md 文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 定义替换函数
                def replace_empty_tags(match):
                    alt_text = match.group(1)
                    url = match.group(2) if match.group(2) else ''
                    
                    # 如果 alt 文本为空，替换为 "img"
                    if not alt_text:
                        return f'![img]({url})' if url else '![img]'
                    
                    # 如果 alt 文本不为空，保持原样
                    return match.group(0)
                
                # 替换内容
                new_content = re.sub(pattern, replace_empty_tags, content)
                
                # 如果内容有变化，写回文件
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f'已更新文件: {file_path}')

# 使用示例
if __name__ == '__main__':
    # 替换为你要处理的目录路径
    directory_path = './_posts'
    fix_empty_image_tags(directory_path)
