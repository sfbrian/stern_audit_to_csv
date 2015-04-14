#!/usr/bin/python
import re
import sys
import getopt
from os import path

def main(argv):
    inputfile = ''

    try:
        opts, args = getopt.getopt(argv,"hf:",["file=","help"])
    except getopt.GetoptError:
        print 'stern_audit_to_csv.py -f <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'stern_audit_to_csv.py -f <inputfile>'
            sys.exit()
        elif opt in ("-f", "--file"):
            inputfile = arg

    if not inputfile:
        sys.exit("File name required")

    try:
        f = open(inputfile, 'r')
    except IOError:
        sys.exit("File not found: %s" % inputfile)

    columns = ""
    rows = ""
    for line in f:
        m = re.search('(\d+)\t([a-zA-Z0-9_.\-\+\(\)\#\:\/ ]*)\s*(.*)', line)
        try:
            columns += "%s," % m.group(2).strip().title().replace(",","")
            rows += "%s," % m.group(3).strip().title().replace(",","")
        except:
            pass

    output_name = path.splitext(inputfile)
    csv = open(output_name[0] + '.csv', 'w')
    csv.write(columns.rstrip(',') + "\n")
    csv.write(rows.rstrip(','))

    f.close()
    csv.close()
    sys.exit("%s.csv Written" % output_name[0])

if __name__ == '__main__':
    main(sys.argv[1:])