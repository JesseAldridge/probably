import os, shutil

import requests

slugs = [
  'sun',
  'pow',
  'disc',
  'prop62',
  'pgh',
  'vb',
  're',
  'bias',
  'talk',
  'aord',
  'name',
  'ronco',
  'work',
  'corpdev',
  'ecw',
  'know',
  'fr',
  'speak',
  'property',
  'ambitious',
  'word',
  'patentpledge',
  'top',
  'organic',
  'discover',
  'kate',
  'revolution',
  'convergence',
  'hackernews',
  '13sentences',
  'highres',
  'artistsship',
  'badeconomy',
  'fundraising',
  'prcmc',
  'cities',
  'distraction',
  'lies',
  'good',
  'boss',
  'ycombinator',
  'startuphubs',
  'webstartups',
  'unions',
  'guidetoinvestors',
  'judgement',
  'mit',
  'investors',
  'copy',
  'island',
  'marginal',
  'america',
  'siliconvalley',
  'startuplessons',
  'randomness',
  'softwarepatents',
  '6631327',
  'procrastination',
  'web20',
  'sfp',
  'inequality',
  'hiring',
  'mac',
  'start',
  'essay',
  'pypar',
  'gh',
  'gba',
  'hp',
  'hundred',
  'nerds',
  'better',
  'spam',
  'power',
  'diff',
  'road',
  'rootsoflisp',
  'popular',
  'lwba',
  'progbot',
]


if os.path.exists('cache'):
  shutil.rmtree('cache')
os.mkdir('cache')

for i, slug in enumerate(slugs):
  print '{}/{}'.format(i + 1, len(slugs))
  req = requests.get('http://www.paulgraham.com/{}.html'.format(slug))
  with open(os.path.join('cache', slug) + '.html', 'w') as f:
    f.write(req.content)
