from main import app

from controllers.country_controller import country
from controllers.city_controller import city

app.include_router(country)
app.include_router(city)