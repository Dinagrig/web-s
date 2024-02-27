from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


users = [
    {'username': 'kirpich', 'password': 1234}
]


@app.route('/')
def hello():
    return f"""
    <p>сайт начиающего верстальщика. Есть ссылки: </p>
        <a href={url_for('index')}>Сайт</a>
        <a href={url_for('start')}>Стартовая стр</a>
        <a href={url_for('base')}>База</a>
        <a href={url_for('form')}>Форма чрт</a>
        <a href={url_for('login')}>Регистрация</a>
    """


@app.route('/index')
def index():
    return render_template('index.html')    # отрисовывает шаблон, лежащий в папке темплейтс


@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        for item in request.form:
            print(request.form[item])
    return render_template('form.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        for user in users:
            if request.form['login'] == user['username']:
                if request.form['password'] == user['password']:
                    return redirect(url_for('profile', username=user['username']))
        print('Неправильный пароль')
    return render_template('login.html')


@app.route('/profile/<username>')
def profile(username):
    return render_template('start.html', username=username)


@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')


@app.route('/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html')


if __name__ == '__main__':
    app.run(debug=True)
