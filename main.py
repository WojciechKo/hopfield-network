import tkinter as tk
import numpy as np

class PatternGrid(tk.Frame):
    def __init__(self, master=None, size=8):
        super().__init__(master)
        self.grid = np.zeros((size,size), dtype=object)
        [self._init_cell(row, column) for row in range(size) for column in range(size)]

    def state(self):
        return np.vectorize(lambda v: v.get())(self.grid)

    def clear(self):
        [value.set(0) for value in self.grid.flat]

    def _init_cell(self, row, column):
        var = tk.IntVar()
        self.grid[row][column] = var

        label = tk.Checkbutton(self, bg="green", width=1, height=1, variable=var)
        label.grid(row=row, column=column)

class NewPattern(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pattern_grid = PatternGrid(self)
        self.pattern_grid.pack()

        self.save_pattern = tk.Button(self, text="Save pattern", command=self._save_pattern)
        self.save_pattern.pack()

    def _save_pattern(self):
        print(self.pattern_grid.state())
        # save_pattern_here
        self.pattern_grid.clear()

class PatternList(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

class Memory(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.label = tk.Label(self)
        self.label["text"] = "Memory"
        self.label.pack(side="top")

        self.new_pattern = NewPattern(master=self)
        self.new_pattern.pack()

        self.pattern_list = PatternList(master=self)
        self.pattern_list.pack()

class Recall(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.hi_there = tk.Button(self, text="Hello World\n(click me)")
        self.hi_there.pack(side="top", expand=1, fill="both")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="top")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title('Hopfield network')
        self.pack(fill="both", expand=1)

        self.memory = Memory(master=self)
        self.memory.pack(side="left", expand=1, fill="both")

        self.recall = Recall(master=self)
        self.recall.pack(side="right")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
