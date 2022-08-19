import os

w = open('config.json', 'w+')
w.write('{')
w.write('\n')
w.write('    "authToken": "'+os.getenv('5679036074:AAFYjlgDItAxiFiLQ6HnK5q9EBwpnCBWJH8')+'",')
w.write('\n')
w.write('    "owner": '+os.getenv('5455166957'))
w.write('\n')
w.write('}')
