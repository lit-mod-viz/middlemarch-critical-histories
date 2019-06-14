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

# 1. Introduction

Decades of research in linguistics have shown that when a large enough collection of texts (a corpus) is analyzed, patterns emerge which aren't detectable at a smaller scale. In some cases these patterns confirm our intuitions and expectations, in other cases they are entirely unexpected or counter-intuitive. This study began with a simple question: what patterns might be revealed by analyzing a large corpus of literary scholarship? Would it provide empirical confirmation of our own sense of the trends in literary studies, or would it reveal dynamics shaping the field and its practices of which scholars aren't consciously aware?

Quotations of literary texts are some of the most important "raw materials" of literary scholarship, and as such their deployment within a scholarly article struck us as a rewarding place to search for patterns at this large scale. This approach has the virtue of being computationally relatively straightforward, broadly applicable across literary-critical writing and offering results which directly reflect (in aggregate) the familiar activities of literary scholarship. We began this project curious to see what citation practices would look like at a scale beyond that which mere mortals can perceive, and approached the results not with hypotheses but with questions. Which parts of a text have been cited most frequently? Which parts haven't? Have these patterns changed over time? Can we detect a life-cycle for certain passages which rise and fall in popularity over time? Can this be connected to major movements within the field (e.g. feminist criticism, deconstruction) or even to a specific critic?

In reflecting on these questions, George Eliot's novel *Middlemarch* stood out as being an especially rich test case. Its first chapter compares the heroine's outstanding qualities to the way a Bible quotation stands out within a piece of journalism, and the novel itself repeatedly thematizes more abstract questions of how a whole can be made up of heterogeneous parts, including ones that come from elsewhere (the newcomer Lydgate's struggle to find a place within the local community, for instance). [find pithier quotation]. Moreover, as Leah Price's work has shown, *Middlemarch*'s afterlife has also been characterized by unusually intensive quotation practices, starting with anthologizers of the time who extracted the novel's eminently quotable aphorisms into books such as *Wise, Witty and Tender Sayings of George Eliot* (even including, ironically enough, a plea against decontextualized wisdom such as: "........."). 

Other practical considerations made *Middlemarch* seem ideal for our purposes. Firstly, its canonical status within studies of English literature ensured the availability of a large sample of articles. Secondly, its length: unlike short hyper-canonical works such as a Shakespeare sonnet, where every word is likely to have been quoted many times, novels in general, and long novels in particular, pose more acute problems for quotation, where a small part has to stand for a much larger whole. Whereas Margaret Cohen (and, citing Cohen, Franco Moretti) has referred to the 99% of forgotten non-canonical literature of the past as "the great unread" [The Sentimental Education of
the Novel [@CohenSentimentalEducationNovel1999, 23; @MorettiSlaughterhouseLiterature2000, 208], we were curious to consider how large swathes of even a hyper-canonical novel can remain "unread" as far as literary scholarship is concerned. Finally, on a practical level, *Middlemarch* occupies a sweet spot of being out of copyright, which facilitates acquiring a digital text, and yet not so old as to raise problems of variant spellings. It also has a relatively straightforward editorial history, so that we haven't had to keep track of multiple versions. [Include more reflection on Middlemarch as a work that is both canonically quoted and also frequently referenced as its own unit]

Having mentioned Moretti, we should briefly position our project in relation to his conception of "distant reading". On the one hand, this project shares much of his spirit, seeking to detect patterns which are both above and below the level of the literary text: looking at "a very small formal unit and a very large one" [@MorettiSlaughterhouseLiterature2000, 217], and whose effects we register without necessarily being fully conscious [Moretti's term is "subliminal"]. On the other hand, our project diverges from his in focusing on a single work, and an extremely canonical one at that. We prefer to think of this as exploring a position somewhere between distant and close reading. Indeed, one of the repeated concerns of this paper will be to show what patterns are revealed or concealed *at different scales* within this middle-distant range. At the extremes, we connect these various scales to the "words on the page" on which close reading operates [footnote here, or is this obvious?], as well as to a distant-reading perspective encompassing hundreds of novels.

The first section of this article offers an account of our methodology, describing the construction of our corpus and the algorithm we developed to detect quotations. The next two sections present our results and discuss possible explanations for some of the most striking patterns we found. First, we examine the uneven attention given to the novel's parts, beginning with the most and least quoted of the eight "Books", before focusing in on chapters, paragraphs and finally sentences, before considering the shifts in critical emphasis over the last 50 years. Second, we use a ranking of the most frequently-quoted words and a comparison between specialist and generalist journals to gain insights into the dynamics of literary studies as a field. Finally, the article concludes by reflecting on the implications of this research for literary studies more broadly, in particular the contribution it makes to the sociology of scholarly activity and the implications it has for reception theory.

# 2. Methodology

## Creating the corpora

The foundation of this project is a comparison between two corpora, one relatively small, consisting of the entire novel *Middlemarch*, the other large and potentially endlessly expandable, consisting of as many writings citing the novel as possible. Of these two, the *Middlemarch* corpus posed far fewer problems: we took the digital text from Project Gutenberg, which aside from a minor issue involving British vs. American spellings seemed to be without visible errors.

As for our corpus of articles, we began by batch-downloading articles from online library JSTOR and then approached JSTOR Labs directly, which very helpfully supplied us with all the articles in JSTOR's collection containing the word "Middlemarch". This proved to be a mixed bag. Firstly, of the 6,069 individual items, many were not articles but "Front Matter", "End Matter", tables of contents and other miscellaneous kinds of writing where the word "Middlemarch" appeared. After running the text matcher (see below), 489 items contained at least one quotation from the novel. Of these, we excluded 7 items dating from between 1873 and 1949, since the coverage prior to the 1950s was so patchy as to prevent any meaningful generalizations. This restriction is justified not only quantitatively but also historically: since our object of study is a scholarly tradition, it's by no means clear how far back the field of literary studies and its institutional contexts remain meaningfully "the same". Certainly it would be dubious to conflate late nineteenth-century literary journals with scholarly journals today, but the early twentieth century is a grey area which for now we've chosen to avoid.

The remaining 482 items constitute our corpus for all the results reported below.

Chronologically, the corpus includes items from 1950 to 2016, but is heavily skewed towards the present. The number of items per decade is as follows:

1950s | 18
1960s | 28
1970s | 65
1980s | 76
1990s | 93
2000s | 106
2010s | 96

As mentioned above, we're interested in what can be seen at different scales of analysis: this means that the patterns we identify for our period wouldn't be invalidated if different patterns were found over a longer historical period. For now, we remain agnostic as to how far our results might generalise beyond our specific corpus.

The text types within this corpus are also somewhat erratic. While 361 items (74.9%) originate from journals, 121 items have not received a "journal code" in JSTOR's metadata. Some of these are classified as "chapter" or "preface" (JSTOR also includes some books) but the vast majority are simply labelled "miscellaneous".

Of the journals, 

While at this scale it *might* have been feasible to manually check each item, the interest in this project is in analysing patterns across ever larger corpora of criticism. As such the problem of constructing a good-enough corpus of texts without examining it directly is one which projects of this kind will need to make peace with.

The text of the articles themselves also produced problems. Much (all?) of JSTOR's collection was produced through scanning of paper journals followed by optical character recognition (OCR). This can introduce a wide range of errors, such as registering an "l" or "I" as the number "1", or reading "m" as "rn" and vice versa. Not only did a random selection of articles we examined contain such errors, but they were not consistent from one article to another, which presumably were scanned at different times and with different technologies. [Did we do anything to counteract this problem?]

Beyond these questions of quality control, there's also the issue of the representativeness of this corpus. Can this collection of articles from JSTOR fairly be said to represent the field of literary scholarship as a whole? We remain agnostic on the matter, and offer the results here as a first attempt using the most readily available resources. Two factors offer a degree of support here. Firstly, in corpus research, size matters. Almost 500 articles from  journals gives a large spread that should in theory prevent the quirks of any one article, scholar or journal from appearing to be a general pattern. Secondly, the results from an initial test we carried out on around 400 articles gave very similar results to the full corpus. If these patterns appear in a much smaller subsection of the corpus, we might also expect they will scale up to larger corpora. This is all speculative, however, and only further research on larger corpora will confirm or revise these results. At any rate, it's by no means trivial to say that these results *are* representative of JSTOR's library, since this is in itself one of the major resources for literary scholars working today.

## *Middlematch*: the matching algorithm

The matching algorithm develops and makes use of existing research in the field of "text reuse detection" (a technology also used to detect plagiarism). Since we're writing this paper with a generalist scholarly audience in mind, we won't go into great detail about the mechanics of our matching algorithm, but interested readers can consult our Github repository [link] or await a more technical paper we intend to write on our methodology.

The algorithm begins by pre-processing both corpora (*Middlemarch* and the criticism), removing punctuation and hyphens which break up words. The Lancaster stemmer is applied, which reduces words with multiple endings to a single "stem", e.g. [......]. This deals with both British/American spelling variants and many cases where scholars adapt the syntactic category of a word in quotation to fit their own sentence. [Do we do anything about irregular verbs?] We experimented with removing so-called "stop words", highly-frequent words such as "the" and "with", but decided against this on the basis that such small words are by no means trivial to literary scholars, and so shouldn't be excluded on principle. We found confirmation for this stance in finding an article which quoted and discussed the phrase "you and me", entirely consisting of stop words.

Next the algorithm searches for overlapping sequences of n-grams (phrases consisting of n words) in both corpora. Based on previous work in text reuse detection and our own process of trial and error, we settled on searching for three overlapping trigrams (three-word sequences), meaning that the shortest possible match we detect is a five-word sequence. [Give example - I think this is a little counterintuitive to non techie people.] Where both corpora contained the same sequence of three overlapping trigrams this was counted as a match. Manual examination of results for various parameters suggested that this configuration provided the best balance of accuracy without detecting false positives. Because we found that the algorithm sometimes struggled to capture the entirety of a quoted passage, we added a final phase in which the algorithm examines the words immediately before and after every match: if a word either side is close enough [by what measure? Levenstein distance of n?] then it's added to the match and the process is repeated until the match is maximally long. To further improve the quality of the matches, a subsequent algorithm compared all the matches within an article, and merged them if they were [exactly? almost?] contiguous: the aim here was to join a single quotation split across two pages, although it would also merge two separate quotations which happened to be contiguous portions of the text.


# 3. Parts of the novel

In this section, we analyze the distribution of quotations across parts of the novel, starting with the largest unit of the novel as a whole, and moving through the major subdivisions of the 8 Books and 86 chapters, before focusing on the detail of specific paragraphs, sentences and phrases. At each level, we find that the passages quoted are distributed very unevenly. Patterns which emerge at one level may not be visible at larger scales, or may reveal more complex patterns at smaller scales.

## 3a. Halves and Books

The simplest division of the novel is into two halves. We divided the text into two segments comprising Books 1-4/Chapters 1-42/....... words and Books 5-8/Chapters 43-86/........ words respectively. Even this two-part division already reveals a striking disparity: ... of the ... quotations, or ...%, come from the first half of the novel, with only ...% of quotations originating from the novel's second half.

While we could search for explanations based on the content of the novel *Middlemarch*, the results of a larger-scale research project at Stanford ........ analyzing quotations from novels in British Periodicals from the 18....s to the 19........s has independently found that this pattern holds true for quotations from novels in general. While we wouldn't want to suggest that scholars are failing to make it all the way through this long novel, there may be general patterns in the ways readers attend to earlier vs later parts of a novel, and which they deem to be worthy of comment.

Across all the articles, quotations from the first half range from 0-..... tokens, while quotations from the second half range from 0-..... tokens. ......% of all the articles contain at least one quotation from each half.

The most extreme instance of first-half bias is ........'s article .......... (year), which features ...... quotations from the first half and ...... from the second. It's notable that this article is also............

Conversely, the most extreme exception to this bias is .......'s article .......... (year), which features ...... quotations from the first half and ...... from the second. It's notable that this article is also............

What these extreme cases allow us to see is that...... . On the other hand, in most articles, the bias towards the first half is........ .

Moving to a slightly smaller scale, the novel is divided into 8 "Books", each of which was initially published separately as a serial instalment between 1871 and 1872. These books vary in length from .......... words (Book .....) to ......... words (Book .....). [^1]

[^1]: It's noteworthy that George Eliot and her publisher were very aware of the discrepancies in length among the Books, even considering publishing shorter Books on thicker paper to compensate [Martin, pp.184-5].

Once again the quotations are drawn very unevenly from across the 8 Books, with Book ...... most frequently cited with ...... of the hits (....%), and Book in last place with ....... of the hits (....%).

As with the division into two halves, most articles don't limit themselves exclusively to discussing just one Book. In fact, ......% of articles include quotations from at least....... Books. [Does proximity play a role? Do quotations tend to cluster around adjacent Books?]

The most extreme outlier, then, is ........'s article ........ (year), which includes ...... quotations from Book ....... (the least popular) and only ...... quotations/no quotations at all from other Books. It is notable that this article is also........ .

In conclusion, 


## 3b. Chapter 20: the critics' favorite





# OLD - Integrate into section 3 above: *Middlemarch* in parts: the distribution of quotations

As said before, despite the enormous amount of scholarly attention *Middlemarch* has received, its size means that large swathes of it have probably never been quoted. This raised for us two questions: is there a pattern to the distribution of quotations, and how (if at all) can we best explain these? As we will show, the question of patterns also requires reflection on the *scale* of analysis. In this section, we examine distributions in descending order of size, starting with a division into the first and second halves of the novel, then comparison between the eight "Books", then the 88 chapters and finally focusing in on paragraphs within a single chapter. In the final part of this section, we introduce a decade-by-decade breakdown of these patterns at the chapter level, in order to examine trends and changes over time.

But first a few words on our results. Of the ..... articles in the corpus, only ..... yielded a single match. In total there were ....... matches, which gives an average of ...... among the articles that produced any matches. Throughout our discussion, it will be important to distinguish clearly between two measures of quantity: the number of quotations (i.e. matches) and the number of words quoted. While the minimum length of quotation our algorithm detects is five words, the range is from five to .......... . These two measures sometimes produce different distributions, and in these cases we state both, since we don't want to adjudicate on the informative value of each.

At the largest scale, the first half of the novel has received substantially more attention than the second half: ...... quotations are taken from the first half compared to ..... for the second half. In other words, the first half accounts for ...% of all quotations. [Difference for word counts?]. While we don't want to suggest that scholars are failing to make it all the way through, the latter parts of the novel certainly seem to have been less generative of discussion. Partly, such a tendency may simply be self-sustaining: if all other scholars have discussed and continue to discuss sections from earlier in the novel, any given scholar will be biased in that direction if they want to engage in those discussions (a point we treat more extensively in section 5 on the sociology of the discipline). An intriguing possibility, however, is that this privileging of the first half isn't unique to *Middlemarch*, or even just to long texts, but can be detected across scholarly writing on all kinds of texts. A project at Stanford has found this to be the case for articles in journals from the 1870s to 1920s [check?] quoting not only *Middlemarch* but some 150 [check] other texts. Important to note is that these were not *scholarly* journals, and that literary scholarship such as it was looked very different at that time, but the trend is certainly suggestive.

Once we shift to the level of the novel's eight "Books", a more complex though not entirely unexpected picture emerges. Within the first half, we see that







