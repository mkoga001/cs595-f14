all:
	pdflatex main.tex 
	bibtex main.aux
	pdflatex main.tex 
	pdflatex main.tex 
	mv main.pdf mallika-A4.pdf

clean:
	rm mallika-A4.pdf *.aux *.log *.toc *.bbl
	

