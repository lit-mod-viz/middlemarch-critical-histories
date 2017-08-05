poster.pdf : poster.md
	pandoc -f markdown -t beamer -o $@ $< \
		--template=default.beamer
	evince $@
