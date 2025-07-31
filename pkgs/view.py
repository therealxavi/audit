from .utility import Utility
from .event import Event


class View(Utility, Event):
  
  def View_all_entries(self):
    prompt = "PLEASE CONFIRM YOU WOULD LIKE TO VIEW ALL ENTRIES (Y/N)"
    if self.proceed(prompt):
      print('\nTHE PERSONAL INFORMATION OF THE BOOKER HAS BEEN HIDDEN IN ACCORDANCE TO PRIVACY TERMS')
      entries = self.view_all()
      print(self.gen_mainifest_list(entries))