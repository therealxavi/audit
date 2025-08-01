from .utility import Utility
from .event import Event
from .booking import Booking

utility, event, booking  = Utility(), Event(), Booking()


class View():
  
  def __init__(self):
    self.caution_prompt = lambda x: f"PLEASE CONFIRM YOU WOULD LIKE TO {x}(Y/N)"
    self.privacy_warninng = "\nTHE PERSONAL INFORMATION OF THE BOOKER HAS BEEN HIDDEN IN ACCORDANCE TO PRIVACY TERMS"

  def view_all_entries(self):
    if utility.proceed(self.caution_prompt('VIEW ALL ENTRIES')):
      print(self.privacy_warninng)
      entries = event.view_all()
      print(utility.gen_mainifest_list(entries))

      utility.ask_table(entries)
  
  def view_by_hall(self):
    while True:
      hall_no = booking.get_hall_number()

      if utility.proceed(self.caution_prompt(f'FILTER ENTRIES BY HALL NUMBER [{hall_no}]')):
        print(self.privacy_warninng)
        args = "Hall_no = ?"
        entries = event.dynamic_query(args, (hall_no,))
        print(utility.gen_mainifest_list(entries))
        
        utility.ask_table(entries)
        break

      else:
        if utility.ask_again(): continue
        else: return

  def view_by_time(self):
    while True:
      time_slot = booking.get_time_slot()

      if utility.proceed(self.caution_prompt(f'FILTER ENTRIES BY TIME SLOT [{time_slot}]')):
          print(self.privacy_warninng)
          args = "Time_slot = ?"
          entries = event.dynamic_query(args, (time_slot,))
          print(utility.gen_mainifest_list(entries))
          
          utility.ask_table(entries)
          break
        
      else:
        if utility.ask_again(): continue
        else: return

  def view_by_date(self):
    while True:
      date = booking.get_date()

      if utility.proceed(self.caution_prompt(f'FILTER ENTRIES BY DATE [{date}]')):
          print(self.privacy_warninng)
          args = "Date = ?"
          entries = event.dynamic_query(args, (date,))
          print(utility.gen_mainifest_list(entries))
          
          
          utility.ask_table(entries)
          break
        
      else:
        if utility.ask_again(): continue
        else: return