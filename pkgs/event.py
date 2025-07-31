import sqlite3
# from utility import Utility

class Event:
  
  def __init__(self):
    self.database = sqlite3.connect('pkgs\My_event.db')

  # CREATE BOOKING TABLE
  def create_table(self):
    with self.database as db:
      db.execute('''CREATE TABLE IF NOT EXISTS bookings 
        (User_name TEXT, Phone_no TEXT, Event_name TEXT, Date TEXT, Time_slot TEXT, Hall_no TEXT, Event_status TEXT)''')
    print('TABLE CREATED SUCCESSFULLY')
  
  # ADD EVENT BOOKING
  def add_event(self, details):
    with self.database as db:
      db.execute('''INSERT INTO bookings 
        (User_name, Phone_no, Event_name, Date, Time_slot, Hall_no, Event_status)
        VALUES (?, ?, ?, ?, ?, ?, ?)''', details)
    print('BOOKING ADDED SUCCESSFULLY')

  # CHECK IF DATA ALREADY EXIST
  def if_data_exists(self, details): 
    with self.database as db:
      entry = db.execute('SELECT * FROM bookings WHERE (User_name = ? AND Phone_no = ? AND Event_name = ? AND Event_status = ?)', details).fetchone()
    return entry

  # CHECK IF DATE IS ALREADY BOOKED
  def if_date_exists(self, details):
    with self.database as db:
      entry_1 = db.execute('SELECT * FROM bookings WHERE (Date = ? AND Time_slot = ? AND Hall_no = ? AND Event_status = ?)', details[0]).fetchone()
      entry_2 = db.execute('SELECT * FROM bookings WHERE (Date = ? AND Time_slot = ? AND Hall_no = ? AND Event_status = ?)', details[1]).fetchone()

    if entry_1: return entry_1
    elif entry_2: return entry_2
    else: return None
  
  # EDIT EVENT BOOKING
  def edit_event(self, details):
    with self.database as db:
      db.execute('''UPDATE bookings SET Date = ?, Time_slot = ?, Hall_no = ?
        WHERE (User_name = ? AND Phone_no = ? AND Event_name = ? AND Event_status = ?)''', details)
    print('BOOKING EDITED SUCCESSFULLY')
  
  # CANCEL EVENT BOOKING
  def cancel_event(self, details):
    with self.database as db:
      db.execute('''UPDATE bookings SET Event_status = Cancelled
        WHERE WHERE (User_name = ? AND Phone_no = ? AND Event_name = ? AND Event_status = ?)''', details)
    print('EVENT CANCELLED SUCCESSFULLY')

  # VIEW ALL BOOKINGS IN TABLE
  def view_all(self):
    with self.database as db:
      entries = db.execute('SELECT * FROM bookings').fetchall()
    return entries