from flask import Flask, render_template, request, url_for
import Spotify


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
	if request.method == "POST":
		if request.form.get('filter') == 'most_popular':

			text = request.form.get("genre")
			result = Spotify.get_popular_song(text)
			return render_template("index.html",result = result, text = text)
		elif request.form.get('filter') == 'least_popular':
			text = request.form.get('genre')
			result = Spotify.get_least_popular_song(text)
			return render_template("index.html",result = result, text=text)
	return render_template("index.html",result=None, text=None )

@app.route("/contact_us")
def contact():
	return render_template("contact_us.html")





""""
@app.route("/recommendation_result/", methods = ["GET", "POST"])
def genre_recommendation_result():
	if request.method == "POST":
		if request.form.get('filter') == 'most_popular':
			text = request.form.get("genre")
			result = Spotify.get_popular_song(text)
			return render_template("genre_recommendation_result.html",result = result)
		elif request.form.get('filter') == 'least_popular':
			text = request.form.get('genre')
			result = Spotify.get_least_popular_song(text)
			return render_template("genre_recommendation_result.html",result = result)

	"""



if __name__ == "__main__":
	app.run(debug=True) #debug = true so we do not need to re run the server anytime we make changes