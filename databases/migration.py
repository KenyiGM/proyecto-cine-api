from models import category, cinema, city, client, country, detail_sell_food, detail_sell_ticket, employee, food, function, movie, quality, room_seat, room, seat, sell_food, sell_ticket, ticket, user_type, user

from databases.database import engine

category.Base.metadata.create_all(bind=engine)
cinema.Base.metadata.create_all(bind=engine)
city.Base.metadata.create_all(bind=engine)
client.Base.metadata.create_all(bind=engine)
country.Base.metadata.create_all(bind=engine)
detail_sell_food.Base.metadata.create_all(bind=engine)
detail_sell_ticket.Base.metadata.create_all(bind=engine)
employee.Base.metadata.create_all(bind=engine)
food.Base.metadata.create_all(bind=engine)
function.Base.metadata.create_all(bind=engine)
movie.Base.metadata.create_all(bind=engine)
quality.Base.metadata.create_all(bind=engine)
room_seat.Base.metadata.create_all(bind=engine)
room.Base.metadata.create_all(bind=engine)
seat.Base.metadata.create_all(bind=engine)
sell_food.Base.metadata.create_all(bind=engine)
sell_ticket.Base.metadata.create_all(bind=engine)
ticket.Base.metadata.create_all(bind=engine)
user_type.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)
