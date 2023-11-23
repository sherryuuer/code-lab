from pathlib import Path


p = Path('.')
list = [x for x in p.iterdir() if x.is_dir()]
print(list)

# [WindowsPath('.git'), WindowsPath('py-io'), WindowsPath('pytest'), WindowsPath('python-concepts'), WindowsPath('python-unittest')]
