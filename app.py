From flask import Flask

app = Flask(_name_)

@app.route('/')
def hello_world():
    return 'Hello,Jenkins!'
if_name_ == '_main_':
    app.run(host='0.0.0',port=5000)
