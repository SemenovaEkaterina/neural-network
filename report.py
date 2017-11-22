import dominate
from dominate.tags import *

doc = dominate.document(title='Report')


stat = list()

for i in range(10):
    file = open('report/stat/{}'.format(i))
    stat.append(file.read().split(';'))

with doc.head:
    link(rel='stylesheet', href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css')
    link(rel='stylesheet', href='../style.css')

with doc:
    with div(id='header'):
        with div(cls='row'):
            for i in range(10):
                with div(cls='col-md-3'):
                    with div(cls='panel panel-{}'.format('success' if (float(stat[i][0]) > 0.65) else 'danger')):
                        div('', cls='panel-heading')
                        with div(cls='panel-body'):
                            with div(cls='col-md-7'):
                                img('', src='imgs/%s.png' % i, width='200px', height='170px')
                            with div(cls='col-md-5'):
                                with div(cls='panel panel-default'):
                                    with ul(cls='list-group'):
                                        li('{}%'.format(round(float(stat[i][0]),2) * 100), cls='list-group-item')
                                        li('Total: {}'.format(stat[i][1]), cls='list-group-item')


file = open('report/report.html', 'w')
file.write(doc.__str__())
file.close()