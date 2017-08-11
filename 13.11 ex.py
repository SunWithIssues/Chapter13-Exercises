#prob 1 
##Write a program that reads a file and writes out a new file with the lines in reversed order (i.e. the first line in the old file becomes the last one in the new file.)
def reversed_file(oldfile, newfile):
    infile = open(oldfile, "r")
    

    sortedfile = infile.readlines()
    infile.close()
    

    length = len(sortedfile)
    x = 1
    outfile = open(newfile, "w")
    while True:
        outfile.write(sortedfile[length-x])
        x += 1
        if x == length + 1:
            break
    outfile.close()
    return newfile

#prob 2
##Write a program that reads a file and prints only those lines that contain the substring snake.
def print_snake(file):
    infile = open(file)
    while True:
        theline = infile.readline()
        if len(theline) == 0:
            break
        if theline.find("snake") >= 0:
            print(theline, end="")
    infile.close()

#prob 3
##Write a program that reads a text file and produces an output file which is a copy of the file, except the first five columns of each line contain a four digit line number, followed by a space. Start numbering the first line in the output file at 1. Ensure that every line number is formatted to the same width in the output file. Use one of your Python programs as test data for this exercise: your output should be a printed and numbered listing of the Python program.
def num_the_lines(oldfile, newfile):
    outfile = open(newfile, "w")
    infile = open(oldfile)
    x = 1
    while True:
        oldLine = infile.readline()
        if len (oldLine) == 0:
            break
        outfile.write("{0:<4}".format(x) + " " + oldLine)
        x += 1
    outfile.close()
    infile.close()
    return newfile

#prob 4
##Write a program that undoes the numbering of the previous exercise: it should read a file with numbered lines and produce another file without line numbers.
def scratch_the_num(oldfile, newfile):
    infile = open(oldfile)
    outfile = open(newfile, "w")
    while True:
        theline = infile.readline()
        if len(theline) == 0:
            break
        outfile.write(theline[5:])
    outfile.close
    infile.close

#creating a file
myfile = open("test.txt", "w")
myfile.write("My fisnakerst file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world! I'm snake\n")
myfile.write("This is the fourth line of this file.\n")
myfile.close()

#test for prob 1
backwardsFile = reversed_file("test.txt", "otherfile.txt")
content = open(backwardsFile)
print(content.read())

#test for prob 2
print_snake("test.txt")

#test for prob 3
numbering = num_the_lines("test.txt", "otherfile.txt")
content = open(numbering)
print(content.read())

#test for prob 4 w/ answer from prob 3
scratch_the_num("otherfile.txt", "otherfile2.txt")
content = open("otherfile2.txt")
print(content.read())
