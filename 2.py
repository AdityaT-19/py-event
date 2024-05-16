"""
Copy a file
"""

srcFileName =  input("Enter a file name with extension : ")
destFileName = input("Enter the destination file name with extension : ")

with open(srcFileName, 'r') as srcFile:
    data = srcFile.read()

with open(destFileName, 'w') as destFile:
    destFile.write(data)
    
print("File copied successfully!")