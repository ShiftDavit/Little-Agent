from functions.list_files import get_file_info

print("Result for current directory:")
print(get_file_info("calculator", ".") + "\n")

print("Result for 'pkg' directory:")
print(get_file_info("calculator", "pkg") + "\n")

print("Result for '/bin' directory:")
print(get_file_info("calculator", "/bin") + "\n")

print("Result for '../' directory:")
print(get_file_info("calculator", "../"))