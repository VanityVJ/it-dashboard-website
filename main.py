from website import create_app
from flask import Flask

app = create_app()

if __name__ == '__main__':
    #app.secret_key = os.getenv('SECRET_KEY')
    #app.run(debug=True,host="127.0.0.1",port="8001")
    #app.secret_key = 'loginnitialworkimaingroupsaintintglobalkarnatakadash'
    app.run(debug=True,host='0.0.0.0', port=8090)
    #context = ('/home/psmri/ssl-test/wildcard.crt', '/home/psmri/ssl-test/wildcard_key.key')
    #app.run(debug=False,host="0.0.0.0",port="443",ssl_context=context)
