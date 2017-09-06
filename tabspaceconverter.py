import fileinput
import sys

#Quick script that takes a file with either tab or space indentation and reverses it.
#   Must provide pathname to file in intial arguments.

#Take in a secondary argument, that being the textfile to be altered.
argfile = str(sys.argv[1])

#Ask the user if they prefer spaces or being wrong.
print("Tabs or Spaces?")
userInput = input();

#Open the file with read-only permissions and copy all of its contents.
with open(argfile, 'r') as file:
    fileContents = file.read()

#Accept the user's input and replace indentation accordingly.
if userInput.lower() in ("tabs", "tab", "t"):
    print("How many spaces does your current indentation use?")
    spaceCount = int(input());
    fileContents = fileContents.replace(spaceCount * ' ', '\t')
    
elif userInput.lower() in ("spaces", "space", "s"):
    print("How many spaces would you like to indent by?")
    spaceCount = int(input());
    fileContents = fileContents.replace('\t', spaceCount * ' ')

#Open the file with write-only permissions and overwrite with updated contents.
with open(argfile, 'w') as file:
    file.write(fileContents)
