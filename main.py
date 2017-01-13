import tkinter as tk
import numpy as np
from hopfield import Hopfield
from reader import Reader

class PatternGrid(tk.Frame):
    def __init__(self, master, size):
        super().__init__(master)
        self.grid = np.zeros((size,size), dtype=object)
        [self._init_cell(row, column) for row in range(size) for column in range(size)]

    def state(self):
        s = np.vectorize(lambda v: -1 if v.get() == 0 else 1)(self.grid)
        print("get_state:")
        print(s)
        return s

    def set_state(self, state):
        # raise Exception("invalid value")
        print("set_state:")
        print(state)
        def mapper(val):
            if val == -1:
                return 0
            elif val == 1:
                return 1
            raise Exception()
        [cell.set(mapper(value)) for value, cell in zip(state.flatten(), self.grid.flat)]

    def clear(self):
        [value.set(0) for value in self.grid.flat]

    def _init_cell(self, row, column):
        var = tk.IntVar()
        self.grid[row][column] = var

        label = tk.Checkbutton(self, bg="green", width=1, height=1, variable=var)
        label.grid(row=row, column=column)

class NewPattern(tk.Frame):
    def __init__(self, master, size):
        super().__init__(master)

        self.pattern_grid = PatternGrid(self, size)
        self.pattern_grid.pack()

        self.recall_pattern = tk.Button(self, text="Recall pattern", command=self._recall_pattern)
        self.recall_pattern.pack()

    def _recall_pattern(self):
        new_pattern = hopfield.recall(self.pattern_grid.state())
        self.pattern_grid.set_state(new_pattern)

    def _clean_pattern(self):
        self.pattern_grid.clear()

class Memory(tk.Frame):
    def __init__(self, master, size):
        super().__init__(master)

        self.label = tk.Label(self)
        self.label["text"] = "Memory"
        self.label.pack(side="top")

        self.new_pattern = NewPattern(self, size)
        self.new_pattern.pack()

# class Recall(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#
#         self.hi_there = tk.Button(self, text="Hello World\n(click me)")
#         self.hi_there.pack(side="top", expand=1, fill="both")
#
#         self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
#         self.quit.pack(side="top")

class Application(tk.Frame):
    def __init__(self, master, size):
        super().__init__(master)
        master.title('Hopfield network')
        self.pack(fill="both", expand=1)

        self.memory = Memory(self, size)
        self.memory.pack(side="left", expand=1, fill="both")

        # self.recall = Recall(master=self)
        # self.recall.pack(side="right")

patterns = Reader('patterns').patterns()
hopfield = Hopfield(patterns['patterns'])

root = tk.Tk()
app = Application(size=patterns['pattern_size'], master=root)
app.mainloop()
