from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def hello():
    return f"""
        <a href={url_for('index')}>Сайт</a>
    """

@app.route('/index')
def index():
    return render_template('index.html')    #отрисовывает шаблон, лежащий в папке темплейтс


@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')    #отрисовывает шаблон, лежащий в папке темплейтс


@app.route('/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html')



if __name__ == '__main__':
    app.run(debug=True)
