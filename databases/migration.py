from models import country, city, room, cinema, room_seat, seat

from databases.database import engine

country.Base.metadata.create_all(bind=engine)
city.Base.metadata.create_all(bind=engine)
cinema.Base.metadata.create_all(bind=engine)
room.Base.metadata.create_all(bind=engine)
seat.Base.metadata.create_all(bind=engine)
room_seat.Base.metadata.create_all(bind=engine)
