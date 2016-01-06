# random-lyrics

This is an experiment trying to rewrite the lyrics of a Cantonese song based on a [Word2Vec](https://github.com/piskvorky/gensim/) model and the segmentation by [Jieba](https://github.com/fxsjy/jieba).

In Cantonese, a character is like a syllable in an English word. Combinations of characters form words; words form phrases. <sub>(To linguists: Just pretend this is how Cantonese works)</sub> The biggest difference between Cantonese and English is that each character in Cantonese also has a tone. A sentence would only make sense (formally) if the characters are pronounced in specific tones. As a result, lyricists cannot simply pick _any_ 2-character Cantonese
words to fill 2 notes in a melody. Therefore, to write lyrics for a song, the actual notes in the melody need to be taken into account. Luckily, this experiment is simply to _rewrite_ the lyrics. The tones of the original lyrics could be used as reference.

Ideally, I want to replace the words in the original lyrics with some other words with the same tones. And this is why Word2Vec can be helpful. Based on articles from Wikipedia, Word2Vec can suggest similar words. Unlike English, words in a Chinese phrase are not separated by spaces. It is just a contagious chunk of characters. Hence, it is only meaningful if we could segment the sentences/phrases into words _correctly_. Jieba does a fantastic job in segmentation although there
are cases where it may struggle, e.g. unknown words, play of words in lyrics. Besides, English words, and other non-Chinese characters can be found in Chinese Wikipedia articles, though there is not enough of them to affect the model significantly.

Let's see some results:
`python random_lyrics.py < test.txt`

```
Building prefix dict from the default dictionary ...
Loading model from cache /tmp/jieba.cache
Loading model cost 0.336 seconds.
Prefix dict has been built succesfully.
頭被雨偏似雪花 打胎該我抹啊 
這風褸我該我曇到有襟花 
連掉也職也不要 好多可惜心碎 
採青選中一天想車我晴天 

明白你一再素恩 身體決對氣促 
花萼鋪滿心裡扶林纔懼怕 
從命我非你都妾 彼此偷生海葬 
心心相印等今天足夠面對 

呢不只得裏單手 要擁抱但難任我保有 
去保有之知好驚覺啥證實 
他延著雪路浪遊 從來爲可別定能 
呢能慿泰攝去愛宕山專有 

何足把心中可怕 拱角另然在我龜兔 
試管裡想花去它五識眼瞳 
纏綿硬化着木頭 離情地丟下就逃跑 
我實都少有 往街裡火向三週 你軸對遭網 

無炎綫相信看腰 只敢兗我褲端 
某種盔甲可會令我多孤單 
留下汽車裡採暖 應當好多推說 
好多鈕以則手指反悔劃損 

人活到很帥夠稍 失戀僅有多稍 
哭喪足夠幾里路呢能外債 
明白你她我宿怨 邊哭邊也幾轉 
中京即旅清早很三世迷惘 

呢不只得裏單手 要擁抱但難任我保有 
去保有之知好驚覺啥證實 
他延著雪路浪遊 從來爲可別定能 
呢能慿泰攝去愛宕山專有 

何足把心中可怕 拱角另然在我龜兔 
試管裡想花去它五識眼瞳 
纏綿硬化着木頭 離情地丟下就逃跑 
我實都少有 往街裡火向三週 你軸對遭網 

呢不只得裏單手 要擁抱但難任我保有 
去保有之知好驚覺啥證實 
他延著雪路浪遊 從來爲可別定能 
呢能慿泰攝去愛宕山專有 

何足把心中可怕 拱角另然在我龜兔 
試管裡想花去它五識眼瞳 
纏綿硬化着木頭 離情地丟下就逃跑 
我實都少有 往街裡火向三週 你軸對遭網 

我還蠻不算 你把這陳年尖領 卻害我抓過 
```

#### Other problems

As you can see, assuming you read Chinese, it mades no sense at all. Most of them don't even work grammatically. This is because _similar_ (based on Word2Vec) words may not have the same part of speech. Secondly, some of the tones do not sound right. Reason for that is Cantonese tones may depend on the context; a character can sound differently in different contexts, and the way I retrieve tones is not aware of the context.


#### References

The training of the Word2Vec model (`wiki.zh.text.trad.seg.model`) is inspired by 52nlp's article, [中英文维基百科语料上的Word2Vec实验](http://www.52nlp.cn/%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91%E8%AF%AD%E6%96%99%E4%B8%8A%E7%9A%84word2vec%E5%AE%9E%E9%AA%8C). The Wikipedia articles are converted to traditional Chinese and are segmented using Jieba instead of MeCab.

The tones (`tones.pickle`) are obtained from the Jyutping romanization [http://faculty-staff.ou.edu/C/Szeming.Cheng-1/cantonese.html](http://faculty-staff.ou.edu/C/Szeming.Cheng-1/cantonese.html).
