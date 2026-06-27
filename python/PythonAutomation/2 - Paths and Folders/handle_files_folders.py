import shutil
from pathlib import Path

# 创建文件夹
new_folder = Path.home() / '__playground' / 'documents'
new_folder.mkdir(exist_ok=True)

# 递归地创建文件夹
another_folder = new_folder / 'sub' / 'sub_of_sub'
another_folder.mkdir(exist_ok=True, parents=True)

src = Path.home() / '__playground' / 'memo.md'
dest = Path.home() / '__playground' / 'documents' / 'memo.md'

# 文件复制
if not src.exists():
    print('The source file does not exist.')
elif dest.exists():
    print('The file already exists in the destination folder.')
else:
    shutil.copy(src, dest)

# 递归地进行copy文件夹
# shutil.copytree(src, dest, dirs_exist_ok=True)
# 移动文件或者文件夹（也可用于重命名）
# shutil.move(src, dest)

# 移除文件
p = Path.home() / '__playground' / 'documents' / 'memo.md'
p.unlink(missing_ok=True)

# 移除文件夹
p = Path.home() / '__playground' / 'documents' / 'sub'

# if p.exists():
# p.rmdir()

p2 = Path.home() / '__playground' / 'documents'

if p2.exists():
    # 删除一个不是空的folder
    shutil.rmtree(p2)
