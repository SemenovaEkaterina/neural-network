import dominate
from dominate.tags import *

doc = dominate.document(title='Report')


a = 80

with doc.head:
    link(rel='stylesheet', href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css')
    link(rel='stylesheet', href='../style.css')

with doc:
    h1('Report',cls='page-header')

    with div(id='header'):
        with div(cls='row'):
            for i in range(10):
                with div(cls='col-md-6'):
                    with div(cls='panel panel-success'):
                        div('Header', cls='panel-heading')
                        with div(cls='panel-body'):
                            with div(cls='col-md-5'):
                                img('', src='imgs/%s.png' % i, width='200px', height='200px')
                            with div(cls='col-md-7'):
                                with div(cls='panel panel-default'):
                                    with ul(cls='list-group'):
                                        li('200', cls='list-group-item')
                                        li('80%', cls='list-group-item')


file = open('report/report.html', 'w')
file.write(doc.__str__())
file.close()