data1 = open('../dataset/input.txt', 'r').read() # should be simple plain text file

data2 = open('../dataset/temp_input.txt', 'r').read()

#print len(data1) - len(data2) 
# data_to_be_removed = """
# <<THIS ELECTRONIC VERSION OF THE COMPLETE WORKS OF WILLIAM
# SHAKESPEARE IS COPYRIGHT 1990-1993 BY WORLD LIBRARY, INC., AND IS
# PROVIDED BY PROJECT GUTENBERG ETEXT OF ILLINOIS BENEDICTINE COLLEGE
# WITH PERMISSION.  ELECTRONIC AND MACHINE READABLE COPIES MAY BE
# DISTRIBUTED SO LONG AS SUCH COPIES (1) ARE FOR YOUR OR OTHERS
# PERSONAL USE ONLY, AND (2) ARE NOT DISTRIBUTED OR USED
# COMMERCIALLY.  PROHIBITED COMMERCIAL DISTRIBUTION INCLUDES BY ANY
# SERVICE THAT CHARGES FOR DOWNLOAD TIME OR FOR MEMBERSHIP.>>
# """

# while data.find(data_to_be_removed) != -1:
# 	index = data.find(data_to_be_removed)
# 	print index
# 	data = data[:index]+data[index+len(data_to_be_removed):]

# with open("dataset/temp_input.txt", 'w') as output_file:
# 	output_file.write(data)
