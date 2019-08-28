import glob, re

class Essay:
  pass

essays = []
for path in glob.glob('cache/*.html'):
  with open(path) as f:
    text = f.read()
  essay = Essay()
  essay.word_to_count = word_to_count = {}
  essay.slug = path.split('cache/')[-1].rsplit('.html')[0]
  print 'slug:', essay.slug
  essay.year = re.search(r'\b([0-9]{4})\b', text, re.DOTALL).group(1)
  print 'year:', essay.year
  essays.append(essay)
  for word in 'probably', 'often':
    word_to_count.setdefault(word, 0)
    word_to_count[word] += text.count(word)

out_lines = ['slug,year,probably,often']
for essay in essays:
  out_lines.append('{},{},{},{}'.format(
    essay.slug, essay.year, essay.word_to_count['probably'], essay.word_to_count['often'],
  ))
with open('out.csv', 'w') as f:
  f.write('\n'.join(out_lines))
