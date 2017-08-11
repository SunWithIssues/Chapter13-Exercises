#prob 1

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
