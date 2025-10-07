import tkinter as tk

class Calculator:
  def __init__(self, root):
    self.root = root
    self.root.title("Calculator")
    self.root.geometry("300x400")
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

  def update_display(self, value):
    self.display.delete(0, tk.END)
    self.display.insert(0, value)

# Start Calculator
if __name__ == "__main__":
  root = tk.Tk()
  calculator = Calculator(root)
  root.mainloop()