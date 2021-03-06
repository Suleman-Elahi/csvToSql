import csv
import sys

filename = 'bd_corta.csv'
output_name = 'out.sql'
table_name = 'table'

#This function prints the first command of the SQL file (INSERT INTO table_name (column1, column2...)
#It gets the column1, column2, ..., columnN from
def printHeader(columns):
    print 'INSERT INTO `'+table_name+'` (',
    for field in columns:
        if field == columns[-1]:
            print '`' + field + '`) VALUES'
        else:
            print '`' + field + '`,',

# This function check each one of the columns with data and prints the insert command
# Ex: ('data1, 'data2', 'data3', ...., 'dataN'),
def printData(data):
    for row in data:
        print '(',
        for i, field in enumerate(row):
            if i < len(row)-1:
                print "'" + field + "',",
            else:
                print "'" + field + "'",
        print '),'

sys.stdout = open(output_name, 'w')
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    columns = next(reader)

    printHeader(columns)
    printData(reader)