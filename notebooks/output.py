# coding: utf-8
for i, article in enumerate(data): 
#     clear_output()
    print('\r', 'Matching article %s of %s' % (i, len(data)), end='')
    if 'numMatches' not in article: 
        articleText = Text(article['text'], article['record_title'], nlp)
        article['numMatches'], article['Locations in A'], article['Locations in B'] =         Matcher(mm, articleText).match()
