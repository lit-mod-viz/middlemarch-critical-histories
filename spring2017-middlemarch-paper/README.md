#Editing this Paper

1. Navigate to [the paper’s markdown file](https://github.com/xpmethod/middlemarch-critical-histories/blob/master/paper/paper.md) on GitHub, and click the edit button with the pencil icon. 

2. After each substantial change, make sure to save and leave a descriptive commit message, documenting your changes. 

##Syntax

 - In-text citations are written `[@price_george_2003 23]`, where `price_george_2003` is the bibliographic key given in the first line of the entry in [Middlemarch.bib](https://github.com/xpmethod/middlemarch-critical-histories/blob/master/paper/Middlemarch.bib). They can also be written `[-@price_george_2003 23]` if the author’s name is not needed, and the brackets can be removed to remove the parentheses in the compiled version. These citations are styled automatically using `pandoc-citeproc`, and an entry in the Works Cited page is automatically generated. 
 - Figures are labeled with `{#fig:topics1}` and referenced with `[@fig:topics2]`. The `topics2` is just an internal reference key, and the final output will look like “Figure 2.” 
 - Footnotes are generally written `Here is a sentence^[Here is a footnote to that sentence.].`. They are automatically numbered. 
 - All other text is written using [Pandoc’s Markdown](http://pandoc.org/MANUAL.html#pandocs-markdown). 
