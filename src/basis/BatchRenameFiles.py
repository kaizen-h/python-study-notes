import os

def batch_rename_files(folder_path, prefix, start_number, extension_filter=None):
    # 获取文件夹下的所有文件
    files = os.listdir(folder_path)
    # 初始化编号
    current_number = start_number
    # 遍历文件夹下的所有文件
    for file in files:
        # 获取文件的完整路径
        file_path = os.path.join(folder_path, file)
        # 检查是否为文件
        if os.path.isfile(file_path):
            # 如果有扩展名筛选条件，检查文件扩展名是否符合条件
            if extension_filter is not None and not file.lower().endswith(extension_filter.lower()):
                continue
            # 获取文件的扩展名
            file_extension = os.path.splitext(file)[1]
            # 生成新的文件名
            new_file_name = f"{prefix}{current_number}{file_extension}"
            # 生成新的文件完整路径
            new_file_path = os.path.join(folder_path, new_file_name)
            # 重命名文件
            os.rename(file_path, new_file_path)
            print(f"已将 {file} 重命名为 {new_file_name}")
            # 编号加 1
            current_number += 1

if __name__ == "__main__":
    # 获取用户输入的文件夹路径
    folder_path = input("请输入要重命名的文件夹路径: ")
    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print("指定的文件夹路径不存在，请检查后重新输入。")
    else:
        # 获取用户输入的新文件名前缀
        prefix = input("请输入新文件名的前缀: ")
        # 获取用户输入的起始编号
        try:
            start_number = int(input("请输入起始编号: "))
        except ValueError:
            print("输入的起始编号不是有效的整数，请重新运行程序并输入有效的整数。")
        else:
            # 获取用户输入的文件扩展名筛选条件
            extension_filter = input("请输入文件扩展名筛选条件（留空则不筛选）: ")
            if extension_filter == "":
                extension_filter = None
            # 调用批量重命名函数
            batch_rename_files(folder_path, prefix, start_number, extension_filter)