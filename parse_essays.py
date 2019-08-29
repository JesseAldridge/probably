import glob, re

class Essay:
  pass

essays = []
for path in glob.glob('cache/*.html'):
  with open(path) as f:
    text = f.read()
  essay = Essay()
  essays.append(essay)
  essay.word_to_count = word_to_count = {}
  essay.word_to_ratio = word_to_ratio = {}
  essay.slug = path.split('cache/')[-1].rsplit('.html')[0]
  print 'slug:', essay.slug
  essay.year = re.search(r'\b([0-9]{4})\b', text).group()
  print 'year:', essay.year
  essay.total_word_count = len(text.split())
  for word in 'probably', 'often':
    word_to_count.setdefault(word, 0)
    word_to_ratio.setdefault(word, 0)
    word_to_count[word] += text.lower().count(word)
    word_to_ratio[word] += round(float(word_to_count[word]) / essay.total_word_count, 4)

out_lines = ['slug,year,count,ratio']
for essay in essays:
  out_lines.append('{},{},{},{}'.format(
    essay.slug,
    essay.year,
    essay.word_to_count['probably'],
    essay.word_to_ratio['probably'],
  ))
with open('out.csv', 'w') as f:
  f.write('\n'.join(out_lines))
