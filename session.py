from flask import Flask, session, redirect, url_for, escape, request
from flask import make_response
from flask import render_template

app = Flask(__name__)
app.secret_key = 'fkdjsafjdkfdlkjfadskjfadskljdsfklj'
app.config.from_pyfile('config.py')


@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        return '登录用户名是:' + username + '<br>' + \
               "<b><a href = '/logout'>点击这里注销</a></b>"
    return "您暂未登录，<br><a href = 'login'></b>" + \
           "点击这里登录</b></a>"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
    <form action = "" method = "post">
        <p><input type = "text" name="username"/><p>
        <p><input type = "submit" value = "登录"/><p>
    </form>
    '''


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
