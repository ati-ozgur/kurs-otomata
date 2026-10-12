
from automata.fa.dfa import DFA

def save_files(dfa,dfa_name):
	file_path=f"../content/images/{dfa_name}"
	file_path_pdf = file_path + ".pdf"
	file_path_png = file_path + ".png"
	dfa.show_diagram(path=file_path_pdf)
	print("saved to",file_path_pdf)
	dfa.show_diagram(path=file_path_png)
	print("saved to",file_path_png)

