---
title: Why scholars quote: a study of 2,000 articles on *Middlemarch*
author: 
 - Milan Terlunen
 - Sierra Eckert
 - Jonathan Reeve
bibliography: Middlemarch.bib
figureTitle: Figure
figPrefix: Figure
---

# 1. Introduction

Scholars across all [or "all humanistic" disciplines––since some scientific disciplines rely entirely on citation, rather than quotation] disciplines routinely quote other writings, but the quotation has a particularly fundamental status for literary scholars. Quoting from literary works is how we present our evidence, comparable to an image for an art historian, an archival reference for a historian or the numbers, tables and graphs by which scientists in many disciplines report their results. If literary works themselves are our raw materials, a quotation is the minimally processed form [Or "most basic unit"? So we can avoid the inevitable Reader #2 who says that "all quotations are 'cooked' not 'raw'"] in which those materials appear in our studies. Quotations are a sliced tomato salad, while paraphrases, generalizations, abstractions and plot summaries are various kinds of tomato soups, salsas and sauces.

Learning to quote appropriately is part of the apprenticeship to enter the discipline, even if it's rarely taught explicitly. Norms around quotation function unobtrusively for the most part, often only becoming palpable when giving feedback to undergraduates. Nonetheless, even if we might struggle to put it into words, we might reasonably believe that we know why we quote what we quote, and how we quote. Like that famous non-definition of obscenity, we know an (in)appropriate quotation when we see it.

This article, and the empirical research it presents, investigates why and how literary scholars quote from a literary text. Do we actually know what, why, and how we quote? Even an agnostic attitude to this question might seem provocative when we're talking about one of the basic building blocks of our discipline and its writing.

Decades of research in linguistics have shown that when a large enough collection of texts (a corpus) is analyzed, patterns emerge which aren't detectable at a smaller scale. In some cases these patterns confirm our intuitions and expectations, in other cases they are entirely unexpected or counter-intuitive. This study began with a simple question: what might we learn about quoting practices by studying a large corpus of literary scholarship? Would it provide empirical confirmation of our intuitions, or would it reveal dynamics shaping the field and its practices of which scholars aren't consciously aware?

We began this project curious to see what quotation practices would look like at a scale beyond that which mere mortals can perceive, and approached the results not with hypotheses but with questions. Which parts of a given literary text have been quoted most frequently? Which parts haven't? Have these patterns changed over time? Can we detect a life-cycle for certain passages which rise and fall in popularity over time? Can this be connected to major movements within the field (e.g. feminist criticism, deconstruction) or even to a specific critic? How do large-scale patterns relate to an individual scholar's freedom, choices and disciplinary pressures?

George Eliot's novel *Middlemarch* struck us as a rich test case for these questions. Its first chapter compares the heroine's outstanding qualities to the way a Bible quotation stands out within a piece of journalism, and the novel itself repeatedly thematizes more abstract questions of how a whole can be made up of heterogeneous parts, including elements drawn in from elsewhere (the newcomer Lydgate's struggle to find a place within the local community, for instance). [find pithier quotation]. Moreover, as Leah Price's work has shown, *Middlemarch* was quoted with exceptional intensity from the moment of publication, starting with anthologizers of the time who extracted the novel's eminently quotable aphorisms into books such as *Wise, Witty and Tender Sayings of George Eliot* (even including, ironically enough, a plea against decontextualized wisdom such as: "........."). 

*Middlemarch* is also ideal for our purposes on practical grounds. Firstly, its canonical status within studies of English literature ensured the availability of a large sample of articles. Secondly, its length: unlike short hyper-canonical works such as a Shakespeare sonnet, where every word is likely to have been quoted many times, novels in general, and long novels in particular, pose more acute problems for quotation, where a small part has to stand for a much larger whole. We were curious to examine how scholars allocate their attention when they can only quote a small fraction of the work they're discussing. Quotation here demands, to use a phrase of Eliot's, an "eminently discriminating selection" ["Historic Guidance", that notebook essay on Comte, @EliotMoreLeavesGeorge1966, 373]. Finally, on a practical level, *Middlemarch* occupies a sweet spot of being out of copyright, which facilitates acquiring a digital text, and yet not so old as to raise linguistic problems such as variant spellings. It also has a relatively straightforward editorial history, so that we haven't had to keep track of multiple versions. [Include more reflection on Middlemarch as a work that is both canonically quoted and also frequently referenced as its own unit]

[Maybe frame this last paragraph with a few introductory sentences describing the arc of our argument before jumping into a description of the various parts of the article?]
The first section of this article offers an account of the dataset and tool we constructed to detect quotations. The next two sections present our results and discuss possible explanations for some of the most striking patterns we found. First, we examine the uneven attention given to the novel's parts, moving from the largest scales (the novel as a whole; its eight "Books") down through chapters and paragraphs to end up on the smallest scale of individual sentences. In addition, we examine the shifts in quotation distribution over the last 50 years. Second, we examine the most frequently-quoted words across the whole novel, and break the results down into specialist and generalist journals, to gain insights into the dynamics of literary studies as a field. Finally, the article concludes by reflecting on the implications of this research for literary studies more broadly, in particular the contribution it makes to the sociology of scholarly activity and the implications it has for reception theory.


# 2. Methodology

## Creating the corpora

The foundation of this project is a comparison between two corpora, one relatively small, consisting of the entire novel *Middlemarch*, the other large and potentially endlessly expandable, consisting of as many writings citing the novel as possible. Of these two, the *Middlemarch* corpus posed far fewer problems: we took the digital text from Project Gutenberg, which aside from a minor issue involving British vs. American spellings seemed to be without visible errors.

As for our corpus of articles, **we began by batch-downloading articles from online library JSTOR**[I would cut this section out––in the wake of Aaron Swartz, I think any discussion of batch-downloading before getting JSTOR approval might raise eyebrows] and then approached JSTOR Labs directly, which very helpfully supplied us with all the articles in JSTOR's collection containing the word "Middlemarch". This proved to be a mixed bag. Firstly, of the 6,069 individual items, many were not articles but "Front Matter", "End Matter", tables of contents and other miscellaneous kinds of writing where the word "Middlemarch" appeared. After running the text matcher (see below), 489 items contained at least one quotation from the novel. Of these, we excluded 7 items dating from between 1873 and 1949, since the coverage prior to the 1950s was so patchy as to prevent any meaningful generalizations. This restriction is justified not only quantitatively but also historically: since our object of study is a scholarly tradition, it's by no means clear how far back the field of literary studies and its institutional contexts remain meaningfully "the same". Certainly it would be dubious to conflate late nineteenth-century literary journals with scholarly journals today, but the early twentieth century is a grey area which for now we've chosen to avoid.

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


# 3. How Critics Quote: Parts of the novel

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


“If we had a keen vision and feeling of all ordinary human life, it would be like hearing the grass grow and the squirrel's heartbeat, and we should die of that roar which lies on the other side of silence.” This passage from  *Middlemarch*, Chapter 20, is one of the most frequently quoted passage in the novel. For many What if you wanted to know how other scholars have used this passage? A glance through JSTOR, you might find yourself dying in a roar of literary information:

[Quotations from six critics who introduce the sentence using the words "famous," "key" or "great"]

The passage is famously famous. But we can be more precise: this exact sentence been quoted over 50 times in scholarly articles written in the last six decades.  Contrast this with Chapter 44, which our algorithm did not detect any quotations in. 

Even within Chapter 20, however, it's really only paragraphs, and even sentences and parts of sentences within paragraphs that are being quoted. Most of chapter 20 looks like the rest of the novel, only a few paragraphs that are quoted

[MORE TO WRITE: Read the single paragraph in all 16 or so articles that quote "roar on the other side of silence" paragraph in Chapter 20.]


## 3c and d: Chapter 15

In these visualizations thus far, we displayed our initial findings synchronically: all of the results are viewed at the same time. And this is how a lot of computational data is presented: in aggregate. But our initial questions had to do with the history of these patterns of literary critical attention. This is where JSTORs metadata comes in. What this metadata helps us do is visualize the same results diachronically––that is, viewing patterns in quotation not in aggregate, but separated out in time. If we do so, it looks something like this image [Image of heatmap] In this heatmap, along the bottom of the chart is the different books divisions of Middlemarch (book “0” refers to the prologue). Along the left-hand side is the decade, starting in 1960s and going up to the 2010s, which tells you when a given part of the novel was quoted in our corpus. And on the far righthand side of the chart is the legend. We’re using one of the standard matplotlib colormaps: the color indicates how often a part of the novel has been quoted in our corpus. Yellow is extremely often, dark purple is rarely. Out of 1794 quotations that we were able to identify, 1270 (or about 70%) come from the first half of the novel, while only 524 or (about 30%) come from the second half. And within the first half of the novel, the first few books are quoted more. If you look at the table below the heatmap, you’ll see that Book 1 and the prologue, seems to be the most frequently cited book of the novel, with about 27% of the total citations, followed closely by Book 2, while Book 7 is the least frequently cited with just 49 quotations (or 3%). So, the story of uneven quotation in Middlemarch seems like one in which Books 1 and 2 seem to have had sustained critical attention, with some waxing and waning across this 60-year-period. 

But these this story looks look slightly different when you look at quotation at the level of the chapter, rather than at the level of the book. This is what it looks like if we visualize same data, but at a different scale. [SLIDE] The image above is a heatmap of the chapters of Middlemarch and how frequently they have been quoted across 60 years of literary criticism. The color coding here has the same meaning: yellow means a chapter has been quoted extremely often, while dark purple means it has been quoted rarely. The most frequently and consistently cited chapters are Chapter 20 (the infamous chapter with the squirrel’s heartbeat line) and Chapter 15 (a chapter devoted to the surgeon Lydgate’s research and backstory). 

In other words, the chapter level view shows us that not only has critical attention tended to favor the first half of the novel, it’s been even more focused: on a handful of particular chapters. 

This brings us to our second important takeaway. Even though we can see clear, and consistent patterns in what gets cited that tend towards select part of the first half of the novel, nearly every single chapter gets quoted at least once during this 60-year time span, even if only gets quoted once during this entire time. This is easier to see in a second visualization. [SLIDE] This heatmap represents the same set of data, but with a slightly different color scheme representing how often a chapter has been quoted. Yellow indicates extremely often; black indicates rarely, while red and purple indicate infrequent quotation. Here we can see that there’s only one chapter, chapter 44 that our algorithm didn’t pick up at least one quotation in.  

We can go even more granular. When we zoom in at the level of the paragraph, rather than the chapter, we can see that even here the unevenness in critical quotation. 

[Image of Middlematch browser] 
This a screenshot included a snippet of a browser we built that displays the text in color depending on how frequently it has been quoted in our dataset, with yellow indicating extremely often and black being rarely. What we see here is that it’s just individual chapters that have come in and out of literary critical fashion––it’s individual paragraphs or sentences within chapters.

This brings us to our third takeaway of this project: the stories that we might tell about critical quotation practices depend heavily on the units of analysis we take in representing these quantitative findings  (the book or chapter level, the sentence or paragraph level, synchronic or diachronic analysis) and the techniques of visualization. Each of these visualizations draws on the same data, but the unit of analysis––the book level, the chapter level, or the sentence and paragraph level––show us that it’s an even small portion of the novel critics have consistently quoted. This third finding is one of the most important, because it shows how this kind of method can tell us something not only about a particular novel and its critical history, but about the way that we as literary critics use evidence.

What are quotation patterns evidence of? For one, they are evidence of institutional infrastructures. *JSTOR* articles do not exist in a vacuum: they come from particular journals [SLIDE] each of which we might study further in trying to track patterns in quotation. What had started as a question about quotation We compare what parts of Middlemarch get quoted in genre-specific journals (like Novel or Studies in the Novel, both founded in the 1960s) or period-specific journals (like Victorian Studies or Nineteenth-Century Fiction, founded around the 1950s) or author-specific and more recent journals (like George Eliot - George Henry Lewes Studies, founded in 1992 from an earlier newsletter). This last journal is an interesting example. Its quotations tend to focus more on minor character names: Casaubon, Garth, Ladislaw, Mary, Farebrother, Carp, Brooke. [Table of names from MDWs?]  Does a more specialist journal tend to gravitate more towards minor characters because they can presume reader familiarity? Or, is it a product of the New Historicist moment of the 1990s with its interests in the various professions of these characters? Journals, like the quotations themselves, are an under-examined institutional structure, and studying them––as we discuss below––offers a more concrete means of studying disciplinary history. 

[MORE TO COME]

Before turning to the next steps of the project, we want to turn to one example of what we can glean from this preliminary work. This has to do with particular set of quotations of a particular chapter: Chapter 15. Something interesting happens to this chapter when we look at how it’s been quoted over time. [GRAPH] Early on, the chapter had some critical citations––3 articles quote from it in the 1960s, 7 in the 1970s. This chapter then jumps into prominence in the 1980s and 1990s with 29 different articles quoting from this chapter––even more than the number quoting from chapter 20. By the next decade, we’ve detected only 7 articles citing it. When we look at the text of the quotations from this chapter–– about 1/3 of which quote the narrator’s opening meta reflections about Fielding and historiography while the rest quote mostly from four paragraphs describing Lydgate and his medical research––the articles that cite it, the intense new focus on chapter 15 becomes a clearer. Many articles, focus on the language of scientific discourse, or on a New Historicist approach to medicine, and on poststructural historiography. 

For instance.... [Close read 2 or 3 examples]

What’s most interesting about Chapter 15 is not the unsurprising fact that New Historicist critics and poststructuralist historians would be interested in this chapter, but the fact that critical attention after this intense focus on Chapter 15 shifts elsewhere: to Chapter 1 and Chapter 20 in the 2000s, to chapters 1, 7, 20, and 24 in the 2010s. What we see is a kind of the rise and fall of chapter 15 as a hotspot for critical quotation. 

Like all aspects of this project, this quantitative finding about Chapter 15 is not, in itself and end result, but a means to prompt further inquiry. Within the project, we use these kinds of findings to return back to the text of the articles that make up these quotations, using to more traditional forms of close reading or cultural analysis to ask new questions about what these patterns are evidence of. Moments like this, or other unusual patterns as a starting point to return to the particular critical articles that make up that data, and the journals that feature certain quotations from parts of the novel.
Without extrapolating too much from this example, we want to suggest that Middlemarch’s critical quotations allow us to think about the degree to which scholarly quotation traces patterns in literary history. Scholars don’t quote in a vacuum. They quote––and they return to quote the passages other scholars quote––because this part of the novel has a history in critical discourse. Sometimes the presence of this pre-history can lead us to not quote from that passage––as we saw happen with Chapter 15––and there are ongoing chapters that critics seem to return to and quote again and again. While one might read these findings and come away with a dire warning about all the swaths of the novel that remain relegated to what Margaret Cohen calls “the great unread,” we’re arguing instead, that the passages critics are citing have as much to do with critics’ historical context as it does with the novel’s structure.[@CohenSentimentalEducationNovel1999, 23] 



# OLD - Integrate into section 3 above: *Middlemarch* in parts: the distribution of quotations

As said before, despite the enormous amount of scholarly attention *Middlemarch* has received, its size means that large swathes of it have probably never been quoted. This raised for us two questions: is there a pattern to the distribution of quotations, and how (if at all) can we best explain these? As we will show, the question of patterns also requires reflection on the *scale* of analysis. In this section, we examine distributions in descending order of size, starting with a division into the first and second halves of the novel, then comparison between the eight "Books", then the 88 chapters and finally focusing in on paragraphs within a single chapter. In the final part of this section, we introduce a decade-by-decade breakdown of these patterns at the chapter level, in order to examine trends and changes over time.

But first a few words on our results. Of the ..... articles in the corpus, only ..... yielded a single match. In total there were ....... matches, which gives an average of ...... among the articles that produced any matches. Throughout our discussion, it will be important to distinguish clearly between two measures of quantity: the number of quotations (i.e. matches) and the number of words quoted. While the minimum length of quotation our algorithm detects is five words, the range is from five to .......... . These two measures sometimes produce different distributions, and in these cases we state both, since we don't want to adjudicate on the informative value of each.

At the largest scale, the first half of the novel has received substantially more attention than the second half: ...... quotations are taken from the first half compared to ..... for the second half. In other words, the first half accounts for ...% of all quotations. [Difference for word counts?]. While we don't want to suggest that scholars are failing to make it all the way through, the latter parts of the novel certainly seem to have been less generative of discussion. Partly, such a tendency may simply be self-sustaining: if all other scholars have discussed and continue to discuss sections from earlier in the novel, any given scholar will be biased in that direction if they want to engage in those discussions (a point we treat more extensively in section 5 on the sociology of the discipline). An intriguing possibility, however, is that this privileging of the first half isn't unique to *Middlemarch*, or even just to long texts, but can be detected across scholarly writing on all kinds of texts. A project at Stanford has found this to be the case for articles in journals from the 1870s to 1920s [check?] quoting not only *Middlemarch* but some 150 [check] other texts. Important to note is that these were not *scholarly* journals, and that literary scholarship such as it was looked very different at that time, but the trend is certainly suggestive.

Once we shift to the level of the novel's eight "Books", a more complex though not entirely unexpected picture emerges. Within the first half, we see that






# Random cuts

Whereas Margaret Cohen has referred to the 99% of forgotten non-canonical literature of the past as "the great unread" [The Sentimental Education of
the Novel [@CohenSentimentalEducationNovel1999, 23], we were curious to consider how 

large swathes of even a hyper-canonical novel can remain "unread" as far as literary scholarship is concerned.

