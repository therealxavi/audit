import sys
from pkgs import *

def ask_again():
  if Utility.proceed('\nWOULD YOU LIKE TO RE-ENTER DATA (Y/N)'): return True
  else: 
      print('CANCELLING PROCESSES...')
      return False

shuffle_edit = lambda details: (details[3], details[4], details[5], details[0], details[1], details[2], details[6])

# ADD BOOKING TO TABLE
def Add_booking():
  while True:
    # PERSONAL INFORMATION SECTION
    while True:
      username = Booking.get_username()
      phone = Booking.get_phone()
      event_name = Booking.get_event_name()
      
      data = (username, phone, event_name, 'Pending')
      entry = Event.if_data_exists(data)
      if entry: 
        print('\nSPAM EVENT PREVENTION. THE APPLICATION DOES NOT ALLOW SIMILAR EVENT NAME WITH THE SAME PERSONAL DATA')
        print(Utility.gen_manifest(entry))
        if ask_again(): continue
        else: return        
      else: break
        
    # DATE-TIME SECTION
    while True:
      date = Booking.get_date()
      time_slot = Booking.get_time_slot()
      hall_no = Booking.get_hall_number()
      
      data = ((date, time_slot, hall_no, 'Pending'), (date,'All-day', hall_no, 'Pending'))
      if Event.if_date_exists(data):
        print('\nTHE SELECTED HALL HAS ALREADY BEEN BOOKED ON THE SELECTED DATE. TRY ANOTHER')
        if ask_again(): continue
        else: return
      else: break

    data = (username, phone, event_name, date, time_slot, hall_no, 'Pending')
    print(Utility.gen_manifest(data))
    if Utility.proceed('\nPLEASE ENSURE THAT THE ENTERED DATA IS CORRECT\nWOULD YOU LIKE TO PROCEED (Y/N)'): 
      Event.add_event(data)
      break
    elif ask_again(): continue
    else: break

# EDIT BOOKING IN TABLE
def Edit_booking():
  while True:
    # PERSONAL INFORMATION SECTION
    while True:
      username = Booking.get_username()
      phone = Booking.get_phone()
      event_name = Booking.get_event_name()

      data = (username, phone, event_name, 'Pending')
      entry = Event.if_data_exists(data)
      if entry: 
        print(Utility.gen_manifest(entry))
        break
      else:
        print('NO EVENT UNDER SUCH ALIAS')
        if ask_again(): continue
        else: return

    # DATE-TIME SECTION
    while True:
      date = Booking.get_date()
      time_slot = Booking.get_time_slot()
      hall_no = Booking.get_hall_number()
      
      data = ((date, time_slot, hall_no, 'Pending'), (date,'All-day', hall_no, 'Pending'))
      if Event.if_date_exists(data):
        print('\nTHE SELECTED HALL HAS ALREADY BEEN BOOKED ON THE SELECTED DATE. TRY ANOTHER')
        if ask_again(): continue
        else: return
      else: break

    data = (username, phone, event_name, date, time_slot, hall_no, 'Pending')
    print('\nOLD-BOOKING')
    print(Utility.gen_manifest(entry))
    print('\nNEW-BOOKING')
    print(Utility.gen_manifest(data))

    if Utility.proceed('PLEASE ENSURE THAT THE ENTERED DATA IS CORRECT\nWOULD YOU LIKE TO PROCEED (Y/N)'):
      Event.edit_event(shuffle_edit(data))
      break
    elif ask_again(): continue
    else: break

def Close_app():
  prompt = "\nALL CHANGES MADE HAS BEEN BACKED UP\nDO YOU WANT TO CLOSE APP? (Y/N)"
  if Utility.proceed(prompt): 
    print('CLOSING ALL OPERATIONS...')
    sys.exit()
  else: return

def Cancel_booking():
  while True:
    username = Booking.get_username()
    phone = Booking.get_phone()
    event_name = Booking.get_event_name()

    data = (username, phone, event_name, 'Pending')
    entry = Event.if_data_exists(data)
    if entry: 
      print(Utility.gen_manifest(entry))
      break
    else:
      print('NO EVENT UNDER SUCH ALIAS')
      if ask_again(): continue
      else: return
  
  while True:
    prompt = "DO YOU WANT TO CANCEL THIS EVENTS"
    if Utility.proceed(prompt):
      Event.cancel_event(data)
      return
    else:
      print('CANCELLING PROCESSES...')
      return
  