import re
import datetime
from .utility import Utility

class Booking(Utility):

  def __init__(self):
    self.data_warning = "\nPLEASE ENSURE THAT THE ENTERED DATA IS CORRECT"
    self.proceed_prompt = "WOULD YOU LIKE TO PROCEED? (Y/N)"

  def get_username(self):
    while True:
      print(self.data_warning)
      username = input('\nADD A USERNAME: ').strip().capitalize()

      if self.check_len(username, 3, 20): continue
      else: 
        if self.proceed(self.proceed_prompt): return username
        else: continue

  def get_phone(self):
    while True:
      print(self.data_warning)
      print('THE APPLICATION ONLY ACCEPTS NIGERIAN NUMBER')
      phone = input('\nADD A PHONE NUMBER: ').strip()

      if not re.fullmatch(r'(070|080|081|090|091)\d{8}', phone):
        print('INVALID PHONE NUMBER')
      else: 
        if self.proceed(self.proceed_prompt): return phone
        else: continue

  def get_event_name(self):
    while True:
      print(self.data_warning)
      event_name = input('\nADD AN EVENT NAME: ').strip().capitalize()

      if self.check_len(event_name, 3, 20): continue
      else: 
        if self.proceed(self.proceed_prompt): return event_name
        else: continue

  def get_date(self):
    date_warning = "\nPLEASE ENSURE THE DATE AND TIME ON YOUR SYSTEM IS CORRECT.\nTHE APPLICATION USES YOUR SYSTEM TIME."
    system_date = datetime.date.today()
    system_year = system_date.year
    system_month = datetime.date(system_year, system_date.month, 1)

    while True:
      # YEAR
      while True:
        print(date_warning)

        year = input('\nADD A VALID YEAR: ').strip()
        if year.isdigit():
          year = int(year)
          if system_year > year: print('THE SELECTED YEAR HAS PASSED')
          elif year - system_year > 5: print('YOU CAN`T BOOK AN EVENT FURTHER THAN FIVE YEARS')
          else: break
        else: print('INVALID DATE TYPE')

      # MONTH
      while True:
        print(date_warning)

        month = input('\nADD A VALID MONTH: ').strip()
        if month.isdigit():
          month = int(month)
          try:
            if system_month > datetime.date(year, month, 1): print('THE SELECTED MONTH HAS PASSED')
            else: break
          except ValueError: print('INVALID DATE TYPE')
        else: print('INVALID DATE TYPE')

      # DAY
      while True:
        print(date_warning)

        day = input('\nADD A VALID DAY: ').strip()
        if day.isdigit():
          day = int(day)
          try:
            if system_date >= datetime.date(year, month, day): print('THE SELECTED DAY HAS PASSED')
            else: break
          except ValueError: print('INVALID DATE TYPE')
        else: print('INVALID DATE TYPE')

      date = f'{year}-{int(month):02}-{int(day):02}'
      print(f'CHOSEN DATE: {date}\n')
      if self.proceed(self.proceed_prompt): return f'{year}-{int(month):02}-{int(day):02}'
      else: continue

  def get_time_slot(self):
    prompt_1 = '''
      1. MORNING 9.00am - 12.00pm
      2. AFTERNOON 2.00pm - 5.00pm
      3. EVENING 7.00pm - 10.00pm
      4. ALL-DAY
    '''
    prompt_2 = 'ADD A TIME SLOT'
    options = [str(i) for i in range(1, 5)]

    while True:
      time_slot = self.option_menu(options, prompt_1, prompt_2)

      if time_slot == '1': time_slot = 'Morning'
      elif time_slot == '2': time_slot = 'Afternoon'
      elif time_slot == '3': time_slot = 'Evening'
      else: time_slot = 'All-day'

      if self.proceed(self.proceed_prompt): return time_slot
      else: continue

  def get_hall_number(self):
    prompt_1 = 'WE HAVE ONLY 10 AVAILABLE HALL'
    prompt_2 = 'ADD A HALL NUMBER'
    options = [str(i) for i in range(1, 11)]

    while True:
      hall_no = self.option_menu(options, prompt_1, prompt_2)

      if self.proceed(self.proceed_prompt): return hall_no
      else: continue
