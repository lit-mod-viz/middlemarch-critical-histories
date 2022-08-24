paper.pdf: paper.md bibliography.bib
	pandoc -o $@ $< --template=template.tex --filter=pandoc-crossref --citeproc --reference-location=document --bibliography=bibliography.bib --csl=harvard-dsh.csl

paper.tex: paper.md bibliography.bib
	pandoc -o $@ $< --template=template.tex --filter=pandoc-crossref --citeproc --reference-location=document --bibliography=bibliography.bib --csl=harvard-dsh.csl
