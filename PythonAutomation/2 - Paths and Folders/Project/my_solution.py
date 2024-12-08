from pathlib import Path
import shutil

# working in the Project folder
# get the user folder
enter_path = input("Please enter a path for clearing: ")
user_path = Path(enter_path)
while not user_path.exists():
    enter_path = input("The path is not exsits, please enter again: ")
    user_path = Path(enter_path)

# create closet folder
closet_folder = user_path / 'closet'
closet_folder.mkdir(exist_ok=True)

text_folder = closet_folder / 'text_files'
text_folder.mkdir(exist_ok=True)

csv_folder = closet_folder / 'csv_files'
csv_folder.mkdir(exist_ok=True)

folder_folders = closet_folder / 'folders'
folder_folders.mkdir(exist_ok=True)

office_folders = closet_folder / 'office_files'  # add by myself
office_folders.mkdir(exist_ok=True)

# clean up
for item in user_path.iterdir():
    # print(item.name)
    if item == closet_folder:
        continue
    elif item.is_dir():
        if "temp" in item.name.lower():
            shutil.rmtree(item)
        else:
            shutil.move(item, folder_folders / item.name)
    elif item.suffix == ".txt":
        shutil.move(item, text_folder / item.name)
    elif item.suffix == ".csv":
        shutil.move(item, csv_folder / item.name)
    elif item.suffix in [".xlsx", ".docx", ".pptx"]:
        shutil.move(item, office_folders / item.name)


print("Folder clean up complete.")
