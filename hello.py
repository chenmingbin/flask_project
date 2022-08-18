from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route("/")
def index():
    return "hello,flask"


books = [
    {"book_id": 1, "book_name": "三国演义"},
    {"book_id": 2, "book_name": "水浒传"},
    {"book_id": 3, "book_name": "红楼梦"},
    {"book_id": 4, "book_name": "西游记"}
]


@app.route("/book/list")
def book_list():
    return books


@app.route("/book/<int:book_id>")
def book_details(book_id):
    for book in books:
        if book_id == book["book_id"]:
            return book
    return "该图书ID不存在"


@app.route('/html_demo')
def html_demo():
    # 声明要渲染的数据
    my_str = "hahaha"
    my_int = 15
    my_float = 15.5
    my_tuples = ("hahahaha")
    my_lists = [1, 2, 3, 4, 5, 6]
    my_dists = {"姓名": "陈明彬", "年龄": 24, "体重": "75KG", "身高": "174CM"}

    # 使用render_template方法进行渲染；
    # 第一个参数是需要渲染的文件名(文件都需要保存在templates文件夹内)，后续才是需要传入的数据
    return render_template(
        'hello.html',
        my_int=my_int,
        my_str=my_str,
        my_float=my_float,
        my_tuples=my_tuples,
        my_lists=my_lists,
        my_dists=my_dists
    )


@app.route('/index')
def index_demo():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
