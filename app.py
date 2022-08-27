from flask import Flask, render_template, request, url_for,flash,jsonify
import Spotify
import json
from pprint import pprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'spotify'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://wpzofaarahpesm:484bbff9823132b5f22578dfffa95bce4452dde87b30b5aef2375c45a615e5e5@ec2-54-85-56-210.compute-1.amazonaws.com:5432/deofkbvcf6h3pd' #table name is song_recommentations 
app.permanent_session_life = timedelta(minutes=10)




db = SQLAlchemy(app)
migrate = Migrate(app,db)

class recommendations(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(40),  nullable=True)
	song_name = db.Column(db.String(40), nullable=True)
	artist_name = db.Column(db.String(40), nullable=True)
	image = db.Column(db.String(140), nullable=True)
	preview = db.Column(db.String(140), nullable=True)
	url = db.Column(db.String(140), nullable=True)

	def __init__(self,user_name,song_name,artist_name):
		self.user_name = user_name
		self.song_name = song_name
		self.artist_name = artist_name

	def __repr__(self):
		return f'<user_name: {self.user_name} song_name: {self.song_name} artist_name: {self.artist_name} image: {self.image} preview: {self.preview} url: {self.url}'

@app.route("/", methods = ["GET", "POST"])
def home():
	if request.method == "POST":
		if request.form.get('filter') == 'most_popular':

			text = request.form.get("genre")
			result = Spotify.get_popular_song(text)
			pprint(result)
		
			
			return render_template("index.html",result = result, text = text)
		elif request.form.get('filter') == 'least_popular':
			text = request.form.get('genre')
			result = Spotify.get_least_popular_song(text)
			return render_template("index.html",result = result, text=text)

	return render_template("index.html",result=None, text=None )

@app.route("/contact_us")
def contact():
	

	return render_template("contact_us.html")



@app.route("/friends", methods=["POST","GET"])
def friends():
	result = None
	
	if request.method =="POST":
		song_namee = request.form['song_name']
		artist_namee = request.form['artist_name']
		user_namee = request.form['user_name']
		result = None
		if song_namee == '':
			flash('Please enter a song name')
			result = None
		elif artist_namee == '':
			flash('please enter an artist name')
			result = None
		elif user_namee == '':
			flash('please enter your name')
			result = None
		elif user_namee != '' and song_namee!='' and artist_namee!='':
			recomendation = recommendations(user_namee,song_namee,artist_namee)
			text = song_namee + ' ' + artist_namee
			result = Spotify.get_popular_song(text)
			#pprint(result)
			#db.session.add(recomendation)
			#db.session.commit()

		return render_template('modals.html', modal_recommendations=result)



	
	return render_template("friends.html", recommendations=recommendations.query.all(), recommendation_result=result)


@app.route('/modal', methods=['POST'])
def modal():
	#output = request.get_json()
	
	return render_template('modals.html')

@app.route('/test', methods=['POST'])
def test():
	output = request.get_json()
	print('output here')
	pprint(output)
	return render_template('test.html')
if __name__ == "__main__":

	app.run(debug=True) #debug = true so we do not need to re run the server anytime we make changes