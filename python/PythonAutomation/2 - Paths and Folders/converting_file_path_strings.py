from pathlib import Path

# r 表示 raw string 可以解放转义符
# p = r'C:\Users\travi\PycharmProjects\paths_and_folders'
# p = r'C:/Users/travi/PycharmProjects/paths_and_folders'

p = input('Please enter the target folder')

path = Path(p)

if path.exists():
    print('I exist!')
