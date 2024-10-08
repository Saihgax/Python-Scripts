# try:
#     with open('example.txt', 'w') as file:
#         file.write("This is a test line.")
#     print("File created and content written successfully.")
# except Exception as e:
#     print(f"An error occurred: {e}")


try:
    with open('example.txt', 'r') as file:
        data = file.read()
    print(f"Contents of the file: {data}")
except Exception as e:
    print(f"Error occurred: {e}")

try:
    with open('example.txt', 'a') as file:
        file.write("\nAppending to the file")
    print("Appended.")
except Exception as e:
    print(f"Error occurred: {e}")

