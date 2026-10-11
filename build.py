# Builds the deployable index.html at the repo root from src/index.html (adds the document head that the preview adds automatically).
import os
here=os.path.dirname(os.path.abspath(__file__))
dist=here
src=open(os.path.join(here,'src','index.html'),encoding='utf-8').read()
# move everything up to the first <style> into head, the rest into body
i=src.index('<style>')
page=('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
      '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
      + src[:i] + '\n' + src[i:src.index('</style>')+8] + '\n</head>\n<body>\n' + src[src.index('</style>')+8:] + '\n</body>\n</html>\n')
open(os.path.join(dist,'index.html'),'w',encoding='utf-8').write(page)
print('built', os.path.join(dist,'index.html'))
