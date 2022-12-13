# -------------------------------------------------------  Method 1:To read  -------------------------------------------------------------------------
# file  = open("my_file.txt")
# contents = file.read()

# print(contents)

# print(file.writable())

# -------------------------------------------------------  Method 2:To read  -------------------------------------------------------------------------
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# -------------------------------------------------------  Method 3:To write  -------------------------------------------------------------------------
with open("my_file.txt", "w") as file:
    file.write("New Text.")

# -------------------------------------------------------  Method 3:To write without deleting   -------------------------------------------------------
with open("my_file.txt", mode = "a") as file:
    file.write("\nNew Text1")

