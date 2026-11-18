"""Build map/artifact.html (fragment for the Claude preview) and map/index.html (standalone page)."""
import json
src = open('artifact.src.html').read()
rooms = json.dumps(json.load(open('regions.json')), separators=(',', ':'))
frag = src.replace('__ROOMS__', rooms)
open('artifact.html', 'w').write(frag)
i = frag.index('</style>') + len('</style>')
head, body = frag[:i], frag[i:]
open('index.html', 'w').write('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    + head + '\n</head>\n<body>' + body.rstrip() + '\n</body>\n</html>\n')
print('built', len(frag), 'bytes')
