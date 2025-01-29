from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/Superhelden'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    try:
        squads = Squad.query.all()
        print(f"Found {len(squads)} squads")  # Debug output
        for squad in squads:
            print(f"Squad: {squad.SquadName}")  # Debug output
        return render_template('index.html', squads=squads)
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug output
        return f"Database error: {str(e)}"

@app.route('/squad/add', methods=['GET', 'POST'])
def add_squad():
    if request.method == 'POST':
        try:
            new_squad = Squad(
                SquadName=request.form['squadname'],
                HomeTown=request.form['hometown'],
                formed=int(request.form['formed']),
                position=request.form['position'],
                SecretBase=request.form['secretbase'],
                active=bool(request.form.get('active'))
            )
            new_squad.insert()
            return redirect(url_for('index'))
        except Exception as e:
            return f"Error adding squad: {str(e)}"
    return render_template('add_squad.html')

@app.route('/squad/<int:sid>')
def view_squad(sid):
    squad = Squad.query.get_or_404(sid)
    members = Member.query.filter_by(sid=sid).all()
    for member in members:
        member.powers = Power.query.filter_by(mid=member.mid).all()
    return render_template('view_squad.html', squad=squad, members=members)

# @app.route('/squad/<int:sid>')
# def view_squad(sid):
#     squad = Squad.query.get_or_404(sid)
#     members = Member.query.filter_by(sid=sid).all()
#     return render_template('view_squad.html', squad=squad, members=members)

@app.route('/squad/edit/<int:sid>', methods=['GET', 'POST'])
def edit_squad(sid):
    squad = Squad.query.get_or_404(sid)
    if request.method == 'POST':
        try:
            squad.SquadName = request.form['squadname']
            squad.HomeTown = request.form['hometown']
            squad.formed = int(request.form['formed'])
            squad.position = request.form['position']
            squad.SecretBase = request.form['secretbase']
            squad.active = bool(request.form.get('active'))
            squad.update()
            return redirect(url_for('index'))
        except Exception as e:
            return f"Error updating squad: {str(e)}"
    return render_template('edit_squad.html', squad=squad)

@app.route('/squad/delete/<int:sid>')
def delete_squad(sid):
    squad = Squad.query.get_or_404(sid)
    try:
        squad.delete()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Error deleting squad: {str(e)}"

# Tabellenstruktur definieren (entsprechend deiner Datenbank)
class Squad(db.Model):
    __tablename__ = 'squad'
    sid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    SquadName = db.Column('SquadName', db.String(255))
    HomeTown = db.Column('HomeTown', db.String(255))
    formed = db.Column('formed', db.Integer)
    position = db.Column('position', db.String(255))
    SecretBase = db.Column('SecretBase', db.String(255))
    active = db.Column('active', db.Boolean, default=True)

    def format(self):
        return {
            'sid': self.sid,
            'SquadName': self.SquadName,
            'HomeTown': self.HomeTown,
            'formed': self.formed,
            'position': self.position,
            'SecretBase': self.SecretBase,
            'active': self.active
        }

    # Relationship
    member = db.relationship('Member', backref='squad', lazy=True, foreign_keys='Member.sid')

class Power(db.Model):
    __tablename__ = 'powers'
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mid = db.Column(db.Integer, db.ForeignKey('member.mid'))
    power = db.Column('power', db.String(255))

class Member(db.Model):
    __tablename__ = 'member'
    mid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sid = db.Column(db.Integer, db.ForeignKey('squad.sid'))
    name = db.Column('name', db.String(255))
    age = db.Column('age', db.Integer)
    SecretIdentity = db.Column('SecretIdentity', db.String(255))

    # Relationship
    powers = db.relationship('Power', backref='member', lazy=True, foreign_keys='Power.mid')


def init_db():
    with app.app_context():
        try:
            db.create_all()
            # Test database connection
            squad = Squad.query.first()
            if squad:
                print(f"Database connection successful. Found squad: {squad.SquadName}")
            else:
                print("Database connected but no squads found")
        except Exception as e:
            print(f"Database connection error: {str(e)}")

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)