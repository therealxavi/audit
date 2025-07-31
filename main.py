from pkgs import *
from build import *

print("\033[2J\033[H")
print("D'Atrium CLI Tool. Visit dautium.org for more details.")

def Menu():
  prompt_1 = '''
    1. ADD BOOKING
    2. EDIT BOOKING
    3. CANCEL BOOKING
    4. VIEW TABLE
    5. HELP
    6. QUIT
  '''
  prompt_2 = "ENTER A VALID OPTION"
  options = [str(i) for i in range(1, 7)]

  choice = Utility.option_menu(options, prompt_1, prompt_2)
  if choice == '1': Add_booking()
  elif choice == '2': Edit_booking()
  elif choice == '3': Cancel_booking()
  elif choice == '4': View_booking()
  elif choice == '5': pass
  else: Close_app()

while True:
  Menu()
