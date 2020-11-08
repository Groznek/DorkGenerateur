# by groznek

import os
import sys
import time

def main():
	print(banner())
	
	try:
		a = input("Entrez Votre Prefix (i.e., \"INURL:\") File Location: "); open(a).close()
		b = input("Entrez Votre KeyWord (i.e., \"Fortnite\") File Location: "); open(b).close()
		c = input("Entrez Votre FileType (i.e., \".php?\") File Location: "); open(c).close()
		d = input("Entrez Votre Parameter (i.e., \"id=\") File Location: "); open(d).close()
		e = input("Entrez Votre Afterfix (i.e., \"Game\") File Location: "); open(e).close()
	except:
		print("\nPas de chemin trouver... exit")
		sys.exit()
	
	output = input("Entre ton File Location: ")
	output_file = open(output, "w")
	
	read_by_line = lambda file: [l[:-1] for l in file.readlines()]
	
	start = int(time.time())
	
	print(f"Commencement de la générations de vos dorks{output}")
	
	with open(a, 'r') as af:
		for prefix in read_by_line(af):
			with open(b, 'r') as bf:
				for keyword in read_by_line(bf):
					with open(c, 'r') as cf:
						for filetype in read_by_line(cf):
							with open(d, 'r') as df:
								for parameter in read_by_line(df):
									with open(e, 'r') as ef:
										for afterfix in read_by_line(ef):
											output_file.write(f'{prefix} {keyword} {filetype} {parameter} "{afterfix}"')
											output_file.write('\n')

	print(f"Fini dans {int(time.time()) - start} seconds")
	
def banner():
	return """
.._|\______________ _,,_
.../ `-------- ' --------------|
./_==©__'______-___ _|
.. ),---.(_(__) /
..// (\) ),----".'.
//___//
`------                    
	"""

if __name__ == "__main__":
	main()