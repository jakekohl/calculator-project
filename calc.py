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
      ['7', '8', '9', '/'],
      ['4', '5', '6', '*'],
      ['1', '2', '3', '-'],
      ['C', '0', '=', '+']
    ]

    for row_idx, row in enumerate(buttons, start = 1):
      for  col_idx, label in enumerate(row):
        button = tk.Button(
          self.root,
          text = label,
          font = ['Arial', 18],
          width=5,
          height=2,
          bg='black',
          fg='white',
          activebackground='#707070',
          relief=tk.RAISED
        )
        button.grid(row=row_idx, column=col_idx, padx=5, pady=5)

  def update_display(self, value):
    self.display.delete(0, tk.END)
    self.display.insert(0, value)

# Start Calculator
if __name__ == "__main__":
  root = tk.Tk()
  calculator = Calculator(root)
  root.mainloop()