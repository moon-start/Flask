#  pip install flask-script

# from flask import Flask
# app = Flask(name)
# app.config.from_object(DevConfig)

from flask import Flask

from DD import *

# app.config.from_object(ProductionConfig)
# app.config['DEBUG'] = False
# app.config['PORT'] = 80
# app.config.from_pyfile('CC.py')




# print(app.config.get('DATABASE_URI'))  # mysql://user@localhost/foo

if __name__ == '__main__':
    # app.run(port=80)
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7" \xe6px@\xc3#\\'
    app.config.from_object(ProductionConfig) ## 使用DD..ProductionConfig類別
    print(app.config.get('DATABASE_URI')) 
    app.run()