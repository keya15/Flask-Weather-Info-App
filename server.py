from flask import Flask, render_template, request
from weather import get_weather_condition

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather')
def weather_condition():
    city = request.args.get('city')
    if not bool(city.strip()):
        return render_template("city-not-found.html")

    weather_info = get_weather_condition(city)

    if weather_info == "none":
        return render_template("city-not-found.html")

    return render_template('weather.html', 
    title = city.capitalize(),
    status =  weather_info['weather'][0]['description'].capitalize(),
    temp = weather_info['main']['temp'],
    feels_like = weather_info['main']['feels_like'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')