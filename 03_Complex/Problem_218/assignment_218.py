'''
Write A Python Program To Find Keyword Density In A Article. 
And Display A Message If Density Increase Up To 3%
'''

def keyword_density(article, keyword):
    article_words = article.split()
    keyword_count = article_words.count(keyword)
    
    density = (keyword_count / len(article_words)) * 100
    return density

article = input("Enter the article: ")
keyword = input("Enter the keyword: ")

density = keyword_density(article, keyword)
print(f"The keyword density of '{keyword}' is: {density:.2f}%")

if density > 3:
    print("Warning: Keyword density exceeds 3%!")


