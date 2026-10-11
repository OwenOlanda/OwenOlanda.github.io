# Builds a standalone, deployable copy of the site in dist/ (adds the document head that the preview adds automatically).
import os, shutil, sys
here=os.path.dirname(os.path.abspath(__file__))
dist=os.path.join(here,'dist')
shutil.rmtree(dist,ignore_errors=True); os.makedirs(dist)
src=open(os.path.join(here,'index.html'),encoding='utf-8').read()
page=('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
      '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
      + src.replace('<style>','</head>\n<body>\n<style>',0) )
# move everything up to the first <style> into head, the rest into body
i=src.index('<style>')
page=('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
      '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
      + src[:i] + '\n' + src[i:src.index('</style>')+8] + '\n</head>\n<body>\n' + src[src.index('</style>')+8:] + '\n</body>\n</html>\n')
open(os.path.join(dist,'index.html'),'w',encoding='utf-8').write(page)
shutil.copytree(os.path.join(here,'assets'),os.path.join(dist,'assets'))
print('built', os.path.join(dist,'index.html'))
