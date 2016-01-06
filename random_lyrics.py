import jieba, pickle, sys, os.path, shutil
from gensim.models import Word2Vec
from glob import glob

model_file = 'wiki.zh.text.trad.seg.model'
tones_file = 'tones.pickle'

# concat the part model files
if not os.path.isfile(model_file):
  with open(model_file,'wb') as fout:
    for part in sorted(glob(model_file + '.*')):
      with open(part, 'rb') as fin:
        shutil.copyfileobj(fin, fout)

model = Word2Vec.load_word2vec_format(model_file, binary=True)

with open(tones_file, 'rb') as f:
  tones_dict = pickle.load(f)

for line in sys.stdin:
  for phrase in line.split():
    for word in jieba.cut(phrase):
      num_char = len(word)
      tones = [tones_dict[c][0] for c in word] # only use the first tone
      choice = word
      try:
        for cand, _ in model.most_similar(word, topn=100):
          if len(cand) != num_char:
            continue
          elif [tones_dict.get(c, [0])[0] for c in cand] == tones:
            choice = cand
            break
      except KeyError:
        pass
      sys.stdout.write(choice.encode('utf-8'))
    sys.stdout.write(' ')
  print
