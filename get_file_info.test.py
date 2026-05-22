from functions.get_file_info import get_file_info

print("Result for current directory:")
print(get_file_info("../calculator", ".") + "\n")

print("Result for 'pkg' directory:")
print(get_file_info("../calculator", "pkg") + "\n")

print("Result for '/bin' directory:")
print(get_file_info("../calculator", "/bin") + "\n")

print("Result for '../' directory:")
print(get_file_info("../calculator", "../"))
# print(get_file_info("calculator", "/bin"))
# print(get_file_info("calculator", "../"))
# print(get_file_info("calculator", "main.py"))