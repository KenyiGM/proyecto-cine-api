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

aap.include_router(category)
aap.include_router(cinema)
aap.include_router(city)
aap.include_router(client)
aap.include_router(country)
aap.include_router(detail_sell_food)
aap.include_router(detail_sell_ticket)
aap.include_router(employee)
aap.include_router(food)
aap.include_router(function)
aap.include_router(movie)
aap.include_router(quality)
aap.include_router(room_seat)
aap.include_router(room)
aap.include_router(seat)
aap.include_router(sell_food)
aap.include_router(sell_ticket)
aap.include_router(ticket)
aap.include_router(user_type)
aap.include_router(user)