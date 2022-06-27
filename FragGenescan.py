
import subprocess
import sys
def FragGeneScan(input_file):
	print("\nRunning FragGeneScan for: "+input_file.split("/")[-1])
	subprocess.call(["run_FragGeneScan.pl -genome"+str(input_file)+"-out="+str("Frag_output") +"-complete=1" + "-train=complete"])

FragGeneScan("contigs.fasta")