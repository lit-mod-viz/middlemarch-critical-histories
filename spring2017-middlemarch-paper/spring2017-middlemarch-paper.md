---
title: "The very fact of frequency": what we can learn from 2,000 scholarly articles on *Middlemarch*
author: 
 - Milan Terlunen
 - Sierra Eckert
 - Jonathan Reeve
bibliography: Middlemarch.bib
figureTitle: Figure
figPrefix: Figure
---

# Introduction

Decades of research in linguistics have shown that when a large enough collection of texts (a corpus) is analysed, patterns emerge which aren't accessible at a smaller scale. In some cases these patterns confirm our intuitions and expectations, in other cases they are entirely unexpected or counter-intuitive. This study began with a simple question: what patterns might be revealed by analysing a large corpus of literary scholarship? Would it provide empirical confirmation of our own sense of the trends in literary scholarship, or would it reveal dynamics shaping the field and its practices of which scholars aren't consciously aware?

Literary texts are one of the most important raw materials of literary scholarship, and as such their deployment within a scholarly article by means of quotation struck us as a rewarding place to search for patterns. This approach has the virtue of being computationally relatively straightforward, broadly applicable across this genre of writing and offering results which directly reflect (in aggregate) the familiar activities of literary scholarship. We began this project curious to see what citation practices would look like at a scale beyond that which mere mortals can perceive, and approached the results not with hypotheses but with questions. Which parts of a text have been cited most frequently? Which parts haven't? Have these patterns changed over time? Can we detect a life-cycle for certain passages which rise and fall in popularity over time? Can this be connected to major movements within the field (e.g. feminist criticism, deconstruction) or even to a specific critic?

In reflecting on these questions, George Eliot's novel *Middlemarch* stood out as being an especially rich test case. Its first chapter compares the heroine's outstanding qualities to the way a Bible quotation stands out within a piece of journalism, and the novel itself repeatedly thematises more abstract questions of how a whole can be made up of heterogeneous parts, including ones that come from elsewhere (the newcomer Lydgate's struggle to find a place within the local community, for instance). Moreover, as Leah Price's work has shown, *Middlemarch*'s afterlife has also been characterised by unusually intensive quotation practices, starting with anthologisers of the time who extracted the novel's eminently quotable aphorisms into books such as *Wise, Witty and Tender Sayings of George Eliot* (even including, ironically enough, a plea against decontextualised wisdom such as: ".........").

Other practical considerations made *Middlemarch* seem ideal. Firstly, its canonical status within studies of English literature, ensuring the availability of a relatively large sample of articles. Secondly, its length: unlike short hyper-canonical works such as a Shakespeare sonnet, where every word is likely to have been quoted many times, novels in general, and long novels in particular, pose more acute problems for quotation, where a small part has to stand for a much larger whole. Whereas Franco Moretti has referred to the 99% of forgotten non-canonical literature of the past as "the great unread" (REF), we are curious to consider how large swathes of even a canonical novel can be "unread", as far as literary scholarship is concerned at least. Finally, on a practical level, *Middlemarch* occupies a sweet spot of being out of copyright, which facilitates acquiring a digital text, and yet not so old as to raise problems of variant spellings. It also has a relatively straightforward editorial history, so that we haven't had to keep track of multiple versions.

The first section of this article offers an account of our methodology, describing the construction of our corpus, the algorithm we created to detect quotations and the techniques we developed to visualise the data. The second section presents our results and discusses possible explanations for some of the most striking patterns we found. Specifically, we focus on......... . Finally, the article concludes by reflecting on the implications of this research for literary studies more broadly, in particular the contribution it makes to the sociology of scholarly activity.

# Methodology

## Creating the corpora

The foundation of this project is a comparison between two corpora, one relatively small, consisting of the entire novel *Middlemarch*, the other large and potentially endlessly expandable, consisting of as many scholarly articles on the novel as possible. The *Middlemarch* corpus posed far fewer problems: we took the digital text from Project Gutenberg, which aside from a minor issue involving British vs. American spellings seemed to be without visible errors.

As for our corpus of articles, we began by batch-downloading articles from online library JSTOR and then approached JSTOR Labs directly, which very helpfully supplied us with all the articles in their collection containing the word "Middlemarch". This proved to be a mixed bag. Firstly, of the 6,069 individual items we received from JSTOR, many were not articles but "Front Matter", "End Matter", tables of contents and other miscellaneous kinds of writing where the word "Middlemarch" appeared. While we assumed that such text types wouldn't affect our research, since they would simply return no quotations, the presence of book reviews was more troubling, since these might incidentally quote from a primary text such as *Middlemarch*, but to very different ends. Although the data JSTOR supplied tagged each item with a text type, these proved unreliable on closer inspection, both tagging some non-articles as articles and tagging some articles as other text types. Our best estimate (give more detail on how?) is that at most 2,000 items from the JSTOR collection are in fact scholarly articles. While at this scale it would have been feasible to manually check each item, the interest in this project is in analysing patterns across ever larger corpora of criticism, and as such the problem of constructing a good enough corpus of texts we can't examine directly will remain for any further projects of this kind.

Chronologically, JSTOR's corpus includes items as far back as ....., but is heavily skewed towards the present. Before the 19x0s, each decade accounts for fewer than .... articles. For these early decades, there's simply not enough data to make generalisations or argue for the existence of patterns; we therefore early on decided to focus only on the last .... decades, which account for the following numbers of items:

The text of the articles themselves also produced problems. Much (all?) of JSTOR's collection was produced through scanning of paper journals followed by optical character recognition (OCR). This can introduce a wide range of errors, such as registering an "l" or "I" as the number "1", or reading "m" as "rn" and vice versa. Not only did a random selection of articles we examined contain such errors, they were not consistent from one article to another, which presumably were scanned at different times and with different technologies. (Did we do anything to counteract this problem?)

Beyond these questions of quality control, there's also the issue of the representativeness of this corpus. Can this collection of articles from JSTOR fairly be said to represent the field of literary scholarship as a whole? We remain agnostic on the matter, and offer the results here as a first attempt using the most readily available resources. Two factors offer a degree of support here. Firstly, in corpus research, size matters. 2,000 articles from nnn journals gives a large spread that should in theory prevent the quirks of any one article, scholar or journal from appearing to be a general pattern. Secondly, the results from an initial test we carried out on around 400 articles gave very similar results to the full corpus. If these patterns appear in a much smaller subsection of the corpus, we might also expect they will scale up to larger corpora. This is all speculative, however, and only further research on larger corpora will confirm or revise these results. At any rate, it's by no means trivial to say that these results *are* representative of JSTOR's library, since this is in itself one of the major resources for literary scholars working today.

## *Middlematch*: the matching algorithm

Describe system first, then parameters

System:
pre-processing - remove punctuation, hyphen healing, stemmer, irregular verbs?
overlapping ngrams
fuzzy matching at edges







