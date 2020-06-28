from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    first_num = d.get('first_num', [''])[0]
    second_num = d.get('second_num', [''])[0]
    sum, mul = 0, 0
    if '' not in [first_num, second_num]:
        first_num, second_num = int(first_num), int(second_num)
        sum = first_num + second_num
        mul = first_num * second_num
    response_body = html % {'sum':sum, 'mul':mul}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]

