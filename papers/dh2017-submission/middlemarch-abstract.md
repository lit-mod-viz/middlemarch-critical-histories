---
title: |
	Frequently Cited Passages Across Time: New Methods for Studying the Critical Reception of Texts
author: Jonathan Reeve, Milan Terlunen, Sierra Eckert
---

Text reuse detection technology and approximate text matching have made possible the large-scale computational identification of intertextuality. These technologies have often been used in plagiarism detection and in studies of journalistic text reuse (Bär, D. et al, 2012). Fewer studies, however, have applied these methods to humanities research. Our project uses this technology to analyze the precise location, density and chronology of citations of a source text, as a way to rethink and extend existing work on reception history. [Distinguish between "technology" and "methodology"]

Our work develops a new method for detecting text re-use and applies it to an under-researched realm of literary history. Recent scholarship and projects, such as [The Viral Texts](http://viraltexts.org/) project and [Digital Breadcrumbs of Brothers Grimm](http://www.etrap.eu/digital-breadcrumbs-of-brothers-grimm/) have shown how algorithmic detection can illuminate the afterlife of a text through quotation or patterns of circulation and textual borrowing in fields from nineteenth-century popular press, nineteenth century French fiction, Biblical quotations and folklore (Büchler, M., et al., 2014; Ganascia, J.-G., 2014; Smith, D.A. et al, 2013; Smith, D.A. et al, 2014). In these projects, the focus is on uncovering hidden networks of reuse in corpora without standardized conventions of citation. Our project seeks to take this work a step further, by applying similar methods in a different area of cultural production where more standardized citation conventions already exist: academic citations. 

Our project uses text-reuse to trace changes in when, how, and what critics cite from a given text. We focus on a single text, using a text matching algorithm that matches tri-grams in a literary text to tri-grams in secondary criticism on that text, calculating the Levenshtein distance for fuzzy matching. [Jonathan, can you double check this language?] In doing so, on recent quantitative studies that take academic articles and scholarly journals as the units for analyzing literary history (Tenen, 2017; Goldstone and Underwood, 2014), and on two recent JSTOR Labs projects that visualize the textual reception of a corpus like [Shakespeare's plays](https://labs.jstor.org/shakespeare/) or the [U.S. Constitution](http://labs.jstor.org/constitution-site/) through the passages cited in scholarly articles.  Like these projects, we hope to leverage the explicit and institutionalized nature of academic citation in studying text-reuse patterns, using text reuse to ask questions of critical attention in canon formation and in the sociology of citation practices. 

In applying these methods to literary scholarship, we've chosen to start on a relatively small scale. George Eliot's novel _Middlemarch_ is an ideal test case, due to its length, copyright status, stable editorial history and canonicity. We have worked with JSTOR Labs to assemble a corpus of around 2,000 articles in its collection that discuss _Middlemarch_. The figures below display preliminary results with a smaller 483-sample corpus.

![Citation Frequency Heat Map for _Middlemarch_, by Decade](images/heatmap.png)

At the largest scale, Figure 1 shows the frequency of citations across the whole of _Middlemarch_ as a heat map segmented by decade, with yellow signifying the highest citation and black, no citations. The novel is broken into its chapters along the horizontal axis, and each segment is colored according to the number of times its text has appeared in the critical literature. Apart from the most-quoted Chapter 20, the beginning and end of the novel show the most numbers of quotations. 

Viewed chronologically, we see that critical interest in certain sections---as expressed in numbers of quotations---appears to shift over time. In the 1950s, most of the critical citation was concentrated on the end of the novel, but this interest has shifted to the beginning by the present day. 

![Citation Frequency Text Browser for _Middlemarch_](images/annotated2.png)

Figure 2 shows a finer grained analysis, no longer segmented by decade, displaying an excerpt from [our paragraph-level text browser for _Middlemarch_](https://lit-mod-viz.github.io/middlemarch-critical-histories/annotated.html). Here again, the color coding represents the density of quotations of each segments, ranging from unquoted black passages, to more frequently quoted purple and red passages. In this sample, the somewhat abstract contrast between "spiritual life" versus "gimp" and "drapery" remains unquoted, whereas the definitive and punchy “her mind was theoretic” has triggered numerous quotations. This annotated edition could provide scholars with a way to read the novel for passages that have been most discussed in secondary literature, and for passages that have been critically neglected.

Applying text reuse detection to study a work's afterlife in quotations has wide-ranging application across the humanities. Firstly, this methodology can be used in any discipline to investigate that discipline’s theoretical history. As with the 1980 study of Wundt's influence on the field of psychology (Brožek,  1980), our methodology could rapidly and easily produce similar investigations for the influence of Saussure in linguistics, Bourdieu in sociology, Mead in anthropology, Beauvoir in feminist theory, and so on. This analysis would be much more fine-grained, registering not only the frequency of *works* cited but also specific sections, passages and even key phrases within them.

[Since part of the contribution of this project is the fact that we're studying critical reception through ACADEMIC citations, I wonder if it might be with worth cutting the last paragraph below, for the purposes of the abstract.]

To return to literary studies, while our own initial project is focusing on academic literary criticism of the post-war period, the methodology could equally be applied to earlier aspects of literary reception. We are interested to examine whether patterns of citation change measurably since English literature is established as a discipline in the late nineteenth century. Going even further back, our methodology could equally be applied to quotations of literary works in non-academic formats, whether non-fiction (newspapers, journals, essays) or other literary works (citations of Shakespeare in Romantic poetry, say).

## References

**Bär, D., Zesch, T., Gurevych, I.,** (2012). "Text Reuse Detection Using a Composition of Text Similarity Measures." *Proceedings of COLING 2012* 1, pp. 167–184.

**Brožek, J.** (1980). “The Echoes of Wundt’s Work in the United States, 1887–1977: A Quantitative Citation Analysis.” *Psychological Research*, 42(1–2): 103–107.

**Büchler, M., Burns, P.R., Müller, M., Franzini, E., Franzini, G.,** (2014). "Towards a Historical Text Re-use Detection." In Biemann, C., Mehler, A. (eds.), *Text Mining, Theory and Applications of Natural Language Processing*. Springer International Publishing, pp. 221–238. 

**Ganascia, J.-G., Glaudes, P., Del Lungo, A.,** (2014). "Automatic detection of reuses and citations in literary texts." *Lit Linguist Computing* 29: 412–421. 

**Goldstone, A., Underwood, T.**, (2014). "The Quiet Transformations of Literary Studies: What Thirteen Thousand Scholars Could Tell Us." *New Literary History* 45: 359–384.

**Smith, D.A., Cordell, R., Dillon, E.M.,** (2013). "Infectious texts: Modeling text reuse in nineteenth-century newspapers." In *Proceedings of the 2013 IEEE International Conference on Big Data*. Santa Clara, CA: IEEE, pp. 86–94. 

**Smith, D.A., Cordell, R., Dillon, E.M., Stramp, N., Wilkerson, J.,** (2014). "Detecting and Modeling Local Text Reuse." In *Proceedings of the 14th ACM/IEEE-CS Joint Conference on Digital Libraries*. Piscataway, NJ: JCDL ’14 and IEEE Press, pp. 183–192.

**Tenen, D.** (forthcoming). "Digital Displacement." In Ursula K. Heise, Dudley Andrew, Alexander Beecroft, Jessica Berman, David Damrosch, Guillermina De Ferrari, César Domínguez, Barbara Harlow, and Eric Hayot (eds.), *Futures of Comparative Literature*,  London: Routledge.
