#Q.3.Write a python program to create a text file. Write ‘I want to become a Data Scientist’ in that file. Then close the file. Open this file and read the content of the file.
f = open("file.text", "w")
f.write("I want to become a Data scientist")
# f.close()
f = open("file.text", "r")