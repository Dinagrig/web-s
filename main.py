from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def hello():
    return f"""
    <p>сайт начиающего верстальщика. Есть ссылки: </p>
        <a href={url_for('index')}>Сайт</a>
        <a href={url_for('start')}>Стартовая стр</a>
        <a href={url_for('base')}>База</a>
    """

@app.route('/index')
def index():
    return render_template('index.html')    #отрисовывает шаблон, лежащий в папке темплейтс


@app.route('/start')
def start():
    return render_template('start.html')    #отрисовывает шаблон, лежащий в папке темплейтс



@app.route('/base')
def base():
    return render_template('base.html')    #отрисовывает шаблон, лежащий в папке темплейтс



@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')    #отрисовывает шаблон, лежащий в папке темплейтс


@app.route('/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html')



if __name__ == '__main__':
    app.run(debug=True)
