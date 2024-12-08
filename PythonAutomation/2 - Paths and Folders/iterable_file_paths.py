from pathlib import Path
from datetime import datetime

path = Path.home() / '__playground' / 'PythonAutomation'
print(path)

# for item in path.iterdir(): # 只会遍历第一层
for item in path.rglob('*'):  # 可以遍历所有子目录和文件
    if item.is_file() and item.suffix == '.txt':
        print(f'-----check text file: {item.stem}-----')

        stats = item.stat()

        print('Size:', stats.st_size)
        print('Last modified:', datetime.fromtimestamp(stats.st_mtime))
        print(f'--------------check over--------------')

    if item.is_dir():
        print(item.name, 'is a directory.#####')

    if 'read' in item.name.lower():
        print(item.name, 'contains the word "read"#####')
