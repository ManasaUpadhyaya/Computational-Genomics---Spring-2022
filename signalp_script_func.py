#!/usr/bin/env python3

import os
from os import listdir
import os 
directory_name = signalp5_outputs
parent_dir = "/home/groupa/functional_annotation/tools/tool_outputs"
path = os.path.join(parent_dir,directory_name)
os.mkdir(path)
mypath = "/home/groupa/final_gene_prediction"
# toolpath = "/home/groupa/functional_annotation/tools/signalp-5.0b/bin/signalp"

#get the names of the directories in a list
dirs = listdir(mypath)

#iterate through the list of directories:
	#inside the directory, run the abyss command for the forward and reverse reads, continue the loop




'''for i in range(len(dirs)):
	if os.path.isdir(f"{mypath}{dirs[i]}"):
		#os.system(f"mkdir {dirs[i]}") #create a directory where the results of one abyss run will be stored
		os.system(f" signalp -fasta '{mypath}{dirs[i]}/consensus_and_fasta/contigs_uniq_consensus.faa' -org gram- -format short -gff3 -prefix '{dirs[i]}' ")
	else:
		continue'''

'''./signalp -fasta /home/groupa/final_gene_prediction/CGT1061/consensus_and_fasta/contigs_uniq_consensus.faa -org gram- -format short -gff3 -prefix CGT1061'''
#!/usr/bin/env python3

def signalP(mypath):
	for i in range(len(dirs)):
			os.system(f" signalp -fasta '{mypath}{dirs[i]}/consensus_and_fasta/contigs_uniq_consensus.faa' -org gram- -format short -gff3 -prefix sig_'{dirs[i]}' ")

signalP("/home/groupa/data/")
os.system(f"mv sig_* '{path}'")
