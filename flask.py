from flask import Flask

app=Flask(__name__)

# 创建了网址 /show/info 和函数index的映射
@app.route('/show/info')
def show_info():
    return 'This is a Flask app'