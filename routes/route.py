from main import app

from controllers.category_controller import category
from controllers.cinema_controller import cinema
from controllers.city_controller import city
from controllers.client_controller import client
from controllers.country_controller import country
from controllers.detail_sell_food_controller import detail_sell_food 
from controllers.detail_sell_ticket_controller import  detail_sell_ticket
from controllers.employee_controller import employee 
from controllers.food_controller import food 
from controllers.function_controller import function 
from controllers.movie_controller import movie 
from controllers.quality_controller import quality 
from controllers.room_seat_controller import room_seat 
from controllers.room_controller import room  
from controllers.seat_controller import seat  
from controllers.sell_food_controller import sell_food  
from controllers.sell_ticket_controller import sell_ticket  
from controllers.ticket_controller import ticket
from controllers.user_type_controller import user_type 
from controllers.user_controller import user

app.include_router(category)
app.include_router(cinema)
app.include_router(city)
app.include_router(client)
app.include_router(country)
app.include_router(detail_sell_food)
app.include_router(detail_sell_ticket)
app.include_router(employee)
app.include_router(food)
app.include_router(function)
app.include_router(movie)
app.include_router(quality)
app.include_router(room_seat)
app.include_router(room)
app.include_router(seat)
app.include_router(sell_food)
app.include_router(sell_ticket)
app.include_router(ticket)
app.include_router(user)
app.include_router(user_type)