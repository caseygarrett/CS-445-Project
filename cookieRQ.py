from requests import session

f = open("header.txt", "a")


payload = {
    'action': 'login',
    'username': '7753504700',
    'password': 'Caseytheman1!'
}

with session() as c:
    c.post('https://twitter.com/login', data=payload)
    response = c.get('https://twitter.com/login')
    f.write(repr(response.headers))    
    f = open("response.txt", "a")    
    f.write(repr(response.text))

f.close()

