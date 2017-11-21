import dominate
from dominate.tags import *

doc = dominate.document(title='Dominate your HTML')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div():
        attr(cls='body')
        p('Lorem ipsum..')


    with div(id='header').add(ol()):
        for i in range(10):
            img('', src='%s.png' % i, width='300px', height='200px')

file = open('report.html', 'w')
file.write(doc.__str__())
file.close()