import tkinter as tk
from turtle import color

class Calculator:
  def __init__(self, root):
    self.root = root
    self.root.title("Calculator")
    self.root.geometry("400x380")
    self.root.resizable(False, False)
    self.root.configure(bg="black")

    # current expression
    self.current_expression = ""

    # create the display field
    self.display = tk.Entry(
      root,
      font=('Arial', 24),
      relief=tk.RIDGE,
      justify='right'
    )
    self.display.grid(
      row=0,
      column=0,
      columnspan=4,
      padx=10,
      pady=10,
      ipadx=10,
      ipady=10
    )

    # Create calculator buttons layout
    self.create_buttons()

  def create_buttons(self):
    buttons = [
      { 'label': '7', 'position': [1, 0], 'command': lambda: self.button_click('7')},
      { 'label': '8', 'position': [1, 1], 'command': lambda: self.button_click('8')},
      { 'label': '9', 'position': [1, 2], 'command': lambda: self.button_click('9')},
      { 'label': '/', 'position': [1, 3], 'command': lambda: self.button_click('/')},
      { 'label': '4', 'position': [2, 0], 'command': lambda: self.button_click('4')},
      { 'label': '5', 'position': [2, 1], 'command': lambda: self.button_click('5')},
      { 'label': '6', 'position': [2, 2], 'command': lambda: self.button_click('6')},
      { 'label': '*', 'position': [2, 3], 'command': lambda: self.button_click('*')},
      { 'label': '1', 'position': [3, 0], 'command': lambda: self.button_click('1')},
      { 'label': '2', 'position': [3, 1], 'command': lambda: self.button_click('2')},
      { 'label': '3', 'position': [3, 2], 'command': lambda: self.button_click('3')},
      { 'label': '-', 'position': [3, 3], 'command': lambda: self.button_click('-')},
      { 'label': 'C', 'position': [4, 0], 'command': lambda: self.button_click('C')},
      { 'label': '0', 'position': [4, 1], 'command': lambda: self.button_click('0')},
      { 'label': '=', 'position': [4, 2], 'command': lambda: self.button_click('=')},
      { 'label': '+', 'position': [4, 3], 'command': lambda: self.button_click('+')},
    ]

    for button_info in buttons:
        button = tk.Button(
          self.root,
          text = button_info['label'],
          font = ['Arial', 18],
          width=5,
          height=2,
          bg='black',
          fg='#707070',
          activebackground='#707070',
          relief=tk.RAISED,
          command=button_info['command']
        )
        button.grid(row=button_info['position'][0], column=button_info['position'][1], padx=5, pady=5)
  
  def button_click(self, button_text):
    if button_text == 'C':
      self.clear()
    elif button_text == '=':
      self.calculate()
    else:
      self.append_to_expression(button_text)
  
  def append_to_expression(self, value):
    self.current_expression += str(value)
    self.update_display(self.current_expression)
  
  def clear(self):
    self.current_expression = ""
    self.update_display("")

  def calculate(self):
    try:
      result = eval(self.current_expression)
      self.update_display(str(result))
      self.current_expression = str(result)
    except Exception as e:
      self.update_display("Error")
      self.current_expression = ""

  def update_display(self, value):
    self.display.delete(0, tk.END)
    self.display.insert(0, value)

# Start Calculator
if __name__ == "__main__":
  root = tk.Tk()
  calculator = Calculator(root)
  root.mainloop()