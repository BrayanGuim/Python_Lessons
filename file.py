#Manipulation of text files.
#To open other text files, use the function open('file_name','opening')
#In the 'opening' argument, it was used the 'r' below, which means : Only read. Therefore, we can't change the content, but just read

manipulator = open('GitProjects/PythonProjects/pyLessons/file.txt' , 'r', encoding='utf-8')
#if the output does not support characters with accent, add as a new argument "encoding = 'utf-8' "↑

print(f'read() Method: \n')
#to call the open() function, use print(variable_name.read())
print(manipulator.read())
#if you want the text to show only one line, use instead of read(), readline() 

#Below is a way to escape the Input-OutputError (IOError) and a way to search specific words of the file.
text = input('Which word would you like to find in the file? :')

try: 
    manipulator = open('GitProjects/PythonProjects/pyLessons/file.txt' , 'r', encoding='utf-8')
    for line in manipulator:
        if text in line:
            print(f'The word was found!')
            print(f'The string was found in the line: "{line}"')
            break
        elif text not in line:
            print(f'The word "{text}" was not found in the file.')
            break
except IOError:
    print('Unable to open the file.')
else: 
    manipulator.close()

#To write: open('file name' , 'w') and variable.write('...')
manipulator = open('GitProjects/PythonProjects/pyLessons/file.txt' , 'w', encoding='utf-8')
print(manipulator.write('Bóson Treinamentos.'))
#To write without deleting: open('file name', 'a') and variable.write('...')