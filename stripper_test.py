import glob, random

human = []
inhuman = []
for path in glob.glob('cache/*.html'):
  with open(path) as f:
    text = f.read()
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

print 'inhuman'
print '-----'
random.shuffle(inhuman)
for line in inhuman[:5]:
  print line

print

print 'human'
print '-----'
random.shuffle(human)
for line in human[:5]:
  print line
