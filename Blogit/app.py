# Importing the necessary Libraries
from database import Database
from menu import Menu

# Initializing database and making connection
Database.initialize()

# Making instance of Menu class
menu = Menu()

menu.run_menu()