odt: 
	pandoc -o middlemarch-abstract.odt middlemarch-abstract.md \
		--latex-engine=xelatex \
		--filter pandoc-crossref \
		--filter pandoc-citeproc \
		--variable urlcolor=blue
	gvfs-open middlemarch-abstract.odt

middlemarch-abstract.pdf : middlemarch-abstract.md
	pandoc -o $@ $< \
		--latex-engine=xelatex \
		--filter pandoc-crossref \
		--filter pandoc-citeproc \
		--variable urlcolor=blue
	gvfs-open $@ &

middlemarch-abstract.md: ../../middlemarch-critical-histories.wiki/DH2017-Abstract.md images
	# Assumes that the wiki is already cloned to the parent directory. 
	cp $< $@

images: 
	cp -R ../../middlemarch-critical-histories.wiki/images .

clean: 
	rm *.md *.pdf
