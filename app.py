
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_PyMongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def echo():
    final_mars_data = mongo.db.final_mars_data.find_one()
    return render_template("index.html", final_mars_data=final_mars_data)

@app.route("/scrape")
def scrape():
    
    final_mars_data = scrape_mars.scrape()
    mongo.db.final_mars_data.update_one({},{"$set":final_mars_data}, upsert=True)
    return redirect('/', code=302)
    
if __name__ == "__main__":
    app.run(debug=True)