from database import Database
from colors import Color
from ui import UI

w = Database()
w.load_data()
x = w.get("N5", "reading")
# print(x[0])
u = UI()

print(u.welcome_msg)
