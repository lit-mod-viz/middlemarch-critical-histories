paper.pdf: paper.md bibliography.bib
	pandoc -o $@ $< --filter=pandoc-crossref --citeproc --reference-location=document --bibliography=bibliography.bib --csl=harvard.csl
