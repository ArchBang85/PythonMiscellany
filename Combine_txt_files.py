### Petriautio@wateraid.org 17/05/2013 ###
import os
import re

### VARIABLES ###

# Folder structure to scan (double backslashes are needed because backslash is an escape character in Python):
rootdir = 'C:\\test\\'
# Output path and file
O_Path = 'C:\\test\\'
O_File = 'All_combined.txt'

# File filter #
# Name start
start = "E17098_ClientExport_"
# File ending
ending = ".txt"
# *Additional fine-tuning should be done below

# Line filter - Use this is you want to bring in only the lines containing the set string
filter_lines = False # If you want all the lines from the files, set this to False
line_criterion = "V0968435/01"
#"20060619-00947696"

# Counters 
file_counter = 0
line_counter = 0

# Creates file for output from given path and file
Resultfile = open(O_Path + O_File, 'w')

# Array to keep track of files that have been read
done_files = []

# Array to keep track of which files have contained hits
lines_found_in_files = []

### FUNCTIONS ###

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def combine_files(path):
    file_counter = 0
    line_counter = 0
    # Cycle through folder structure
    for root, dirs, files in os.walk(path):
        for name in files:
            # Specify how filename should begin and end
            # * additional file filtering criteria should be set HERE
            if name.startswith(start) and name.endswith(ending) and is_number(name[20:22]) and len(name) == 27:
                file_counter = file_counter + 1
                # Check against files that have already been scanned
                if name not in done_files:  
                    done_files.append(name)
                    csv_path = os.path.join(root, name)
                    try:
                        # Write contents of file into output file
                        with open(csv_path, 'rb') as f:
                            for line in f:
                                # Specify if the line needs to contain anything special:
                                if filter_lines == True: 
                                    if line_criterion in line:
                                        line_counter = line_counter + 1
                                        Resultfile.write(line)
                                        lines_found_in_files.append(name)
                                else:
                                    line_counter = line_counter + 1
                                    Resultfile.write(line)
                               

                    except IOError, e:
                        print e

    print "I have scanned the following %s files for occurrences of %s:\n\n%s" % (file_counter, '"'+line_criterion+'"',"\n".join(done_files))
    print "\n matches in: %s" % "\n".join(lines_found_in_files)

    print "\nAnd written %s lines to %s" % (line_counter, O_Path + O_File)
    print "\nGood Bye"

combine_files(rootdir)

