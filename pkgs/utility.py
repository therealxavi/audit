
class Utility:

  def check_len(self, arg, min, max):
    if len(arg) < min: 
      print(f'ENTRY MUST CONTAIN MORE THAN {min} CHARACTERS')
      return True
    elif len(arg) > max:
      print(f'ENTRY MUST CONTAIN LESS THAN {max} CHARACTERS')
      return True
    else: return False

  def proceed(self, prompt):
    options = ['Y', 'N']
    while True:
      choice = input(f'{prompt}: ').strip().upper()
      if choice not in options:
        print('INVALID ENTRY. ENTER Y OR N')
      elif choice == 'Y': return True
      else: return False
  
  def option_menu(self, options, prompt_1, prompt_2):
    print(prompt_1)
    while True:
      choice = input(f'\n{prompt_2}: ').strip()
      if choice in options: return choice
      else: print('INVALID OPTION. TRY AGAIN')
  
  def gen_manifest(self, details, index=0):
    label = ['USERNAME', 'PHONE NUMBER', 'EVENT NAME', 'DATE', 'TIME SLOT', 'HALL NUMBER', 'EVENT STATUS'][index:]
    temp_details = list(details)[index:]
    output = '\n'
    for key,value in zip(label, temp_details):
      output += f"{key}: {value}\n"
    return output
  
  def gen_mainifest_list(self, data_list):
    output = '\n'
    for data in data_list:
      count = data_list.index(data) + 1
      output += f'{count}>\n{self.gen_manifest(data, 2)}'
    return output
