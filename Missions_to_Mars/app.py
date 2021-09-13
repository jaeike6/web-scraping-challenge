from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars"
mongo = PyMongo(app)


news_title = "Q&A with the Student Who Named Ingenuity, NASA's Mars Helicopter"
news_p ="As a longtime fan of space exploration, Vaneeza Rupani appreciates the creativity and collaboration involved with trying to fly on another planet."
hemisphere_image_urls = [
    {"title_1": "Valles Marineris Hemisphere", "img_url_1": "https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
    {"title_2": "Cerberus Hemisphere", "img_url_2": "https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title_3": "Schiaparelli Hemisphere", "img_url_3": "https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    {"title_4": "Syrtis Major Hemisphere", "img_url_4": "https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
]

@app.route("/")
def echo():

    return render_template("index.html", title=news_title, subtitle=news_p, image = hemisphere_image_urls)

@app.route("/scrape")
def scraper():
    listings = mongo.db.listings
    listings_data = scrape_mars.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)