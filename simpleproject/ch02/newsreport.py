"""
1. 뉴스 기사 (base64파일) 디코딩
2. 문서 요약/키워드 추출
3. 요약 리포트 작성
4. html 파일로 Export
"""

# 뉴스 기사 디코딩
import base64
import collections
import textwrap
import re
from gensim.summarization.summarizer import summarize
from gensim.summarization.textcleaner import split_sentences

#기사 이미지
f = open("simpleproject/ch02/news/image",'rb')
image = f.readlines()
f.close()

#기사 본문
f = open("simpleproject/ch02/news/article",'rb')
article = f.readlines()
f.close()

#사진 디코딩 후 jpg로 저장
file_base64 = image[0]
path = "simpleproject/ch02/news/image.jpg"
with open(path, 'wb') as f:
    decoded_data = base64.decodebytes(file_base64)
    f.write(decoded_data)

#문서 디코딩
file_base64 = article[0]
decoded_data = base64.decodebytes(file_base64)
article = decoded_data.decode('utf-8')

article_summarized = summarize(article, word_count=50)   #ratio = 비율, word_count = 단어수

#키워드 추출 후 상위 5개만 사용 (태그를 다는 용도)
article_align = textwrap.fill(article, width=50)
words = re.findall(r'\w+', article_align)
counter = collections.Counter(words)
keywords = counter.most_common(5)[1:]

#요약 리포트 작성
keys = ['#' + elem[0] for elem in keywords]
keys = ' '.join(keys)
#html 파일로 저장
htmlfile = open("simpleproject/ch02/news/summary.html", "w")
htmlfile.write("<html>\n")
htmlfile.write("<h1>"+'카운트다운 들어간 아르테미스 계획..."달의 여신"은 미소지을까'+"<h1>\n")
htmlfile.write("<img src='image.jpg'/>\n")
htmlfile.write("<h2>"+ article_summarized +"<h2>\n")
htmlfile.write("<h2 style='background-color:powderblue;'>"+ keys +"<h2>\n")
htmlfile.write("</html>\n")
htmlfile.close()