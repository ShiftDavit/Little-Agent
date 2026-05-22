from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

print(f"calculator/main.py length: {len(get_file_content('calculator', 'main.py'))}")
print(f"calculator.py length: {len(get_file_content('calculator', 'pkg/calculator.py'))}")
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))