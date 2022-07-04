paper.pdf: paper.md bibliography.bib
	pandoc -o $@ $< --bibliography=bibliography.bib --filter=pandoc-crossref
