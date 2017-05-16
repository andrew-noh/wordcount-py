**Wordcount**

Word Frequency count comparison of the Apple iOS HIG and Android Material Design documents

***Text sources***:
1. [Apple iOS Human Interface Guidelines](https://developer.apple.com/ios/human-interface-guidelines/overview/design-principles/)
2. [Android Material Design](https://material.io/guidelines/material-design/introduction.html)

***File list***:
1. Source Text(.docx)
 - iOS Human Interface Guidelines.docx
 - Material design.docx
2. TXT file for processing(.txt)
 - ios_hig _text.txt
 - android_design _text.txt
3. Output Files
 - ios_word _count.txt
 - android_word _count.txt
 - ios_word _count.xlsx (modified from .csv file)
 - android_word _count.xlsx (modified from .csv file)
4. Python Source code
 - word counter.py
5. [Wordclouds](http://wordclouds.com) project file
 - wordcloud_ios.wcld
 - wordcloud_android.wcld

 
 
 **Font weight is determined by word frequency:**

 IF (>500),19,
 
 IF (<500, >300),14,
 
 IF (<300, >150),10,
 
 IF (<150, D4>60),6,
 
 IF (<60, >30),3,
 
 ELSE 2
 
 ***=IF(D4>500,19,IF(AND(D4<500,D4>300),14,IF(AND(D4<300,D4>150),10,IF(AND(D4<150,D4>60),6,IF(AND(D4<60,D4>30),3,2)))))***
 
Less meaningful grammatical parts of words like articles(the, a) and prepositions(for, with, when) are manually reduced.

