import glob, re

class Essay:
  pass

def strip_markup(text): # see stripper_test.py
  human = []
  inhuman = []
  for line in text.splitlines():
    if (
      'DOCTYPE HTML' in line or
      "text/javascript" in line or
      "</script>" in line or
      "Begin Yahoo Store Generated Code" in line or
      'csell' in line or
      "<area shape=rect" in line
    ):
      inhuman.append(line)
    else:
      human.append(line)
  return '\n'.join(human)

essays = []
for path in glob.glob('cache/*.html'):
  with open(path) as f:
    raw_text = f.read()
  stripped_text = strip_markup(raw_text)
  essay = Essay()
  essays.append(essay)
  essay.word_to_count = word_to_count = {}
  essay.word_to_ratio = word_to_ratio = {}
  essay.slug = path.split('cache/')[-1].rsplit('.html')[0]
  print 'slug:', essay.slug
  essay.year = re.search(r'\b([0-9]{4})\b', raw_text).group()
  print 'year:', essay.year
  essay.total_word_count = len(stripped_text.split())
  for word in 'probably', 'often':
    word_to_count.setdefault(word, 0)
    word_to_ratio.setdefault(word, 0)
    word_to_count[word] += stripped_text.lower().count(word)
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
