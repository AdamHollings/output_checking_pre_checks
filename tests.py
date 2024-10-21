from auto_check_functions import *

c, i = detect_files("example_1")
print(c,i)

print(read_context(c))

print(check_file_type(i))

print(check_context_length(c))

