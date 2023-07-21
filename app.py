from flask import Flask,  render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/testing'


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=True)


@app.route('/')
@app.route('/<int:page>', methods=['GET'])
def index(page=1):
    per_page = 5
    users_pagination = Users.query.order_by(Users.id).paginate(
        page=page, per_page=per_page, error_out=False)
    title = 'Flask App with Jinja2'
    name = 'Admin Panel'
    return render_template('app.html', title=title, name=name, users_pagination=users_pagination)


@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    last_name = request.form.get('last_name')
    city = request.form.get('city')

    if not name or not last_name or not city:
        return redirect(url_for('index'))

    new_user = Users(name=name, last_name=last_name, city=city)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = Users.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()

    return redirect(url_for('index'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(port=8000, debug=True)
