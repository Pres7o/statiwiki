from browser import  document
from browser import window

page = str(window.location.search[1:])
metadata = window.jsyaml.load(open(str('/content/' + page + ".yaml")).read())
content = window.markdownit().render(open(str('/content/' + page + ".md")).read())

if page == 'Main_Page':
    document['title'].text = metadata["title"]
    document['slogan'].text = metadata["slogan"]
    document['content'].html = content
    
else:
    document['title'].text = metadata["title"]
    document['content'].html = content
