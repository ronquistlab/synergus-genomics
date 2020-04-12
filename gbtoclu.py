#turn the Gblocks txt output into a clustal format file
#usage: python gbtoclu.py input_file.fasta-gb.txt output_file.clu

#read comand line arguments
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("input_txt", help="gblock txt file to be processed")
parser.add_argument("output", help="output file")
args=parser.parse_args()

#read the input
with open(str(args.input_txt), 'r') as txt:
        gb=txt.readlines()

#write the output file
with open(str(args.output), 'w') as clu:
        clu.write("""CLUSTAL W

""") #header of clustal file format
        for line in gb:
                if "Number of sequences:" in line: #first part of input is discarded
                        nseq=int(line.split(':')[1].strip()) #except information on number of sequences
                        break
        alnblock=False #variable needed to determin if a line in the input is part of the relevant info
        for line in gb:
                if alnblock==False and "=========+" in line: #skip lines with this symbol
                        alnblock=True #the lines that follows are to be written
                elif alnblock==True and line[0]!=' ': #discard lines beginning with a white-space
                        if line[:7]=="Gblocks": #lines that tell if the positions above are conserved or not
                                clu.write("       "+line[7:]) #replace the "Gblocks" at the start of this lines with white-spaces
                        elif "Parameters used" in line: #don't need this lines
                                alnblock=False
                        else:
                                clu.write(line) #ewrithing else stays
