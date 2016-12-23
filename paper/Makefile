paper.pdf: paper.md
	pandoc -o $@ $< \
		-V colorlinks \
		--latex-engine=xelatex \
		--filter pandoc-crossref \
		--filter pandoc-citeproc
	evince '$@'

mla: 
	pandoc -o paper-mla.pdf paper.md \
		-V colorlinks \
		--latex-engine=xelatex \
		--filter pandoc-crossref \
		--filter pandoc-citeproc \
		--template mla-template.tex
	evince paper.pdf
