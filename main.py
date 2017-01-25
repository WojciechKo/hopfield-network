import sys

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

        self.clear_grid = tk.Button(self, text="Clear grid", command=self._clear_grid)
        self.clear_grid.pack()

        self.indicator = tk.Label(self, text=self._indicator_text(False, ''), justify="left", anchor="w")
        self.indicator.pack(expand=1, fill="both")

    def _recall_pattern(self):
        state = hopfield.recall(self.pattern_grid.state())
        self.pattern_grid.set_state(state["pattern"])
        self.indicator.configure(text = self._indicator_text(state["stable"], state["name"]))

    def _clear_grid(self):
        self.pattern_grid.clear()
        self.indicator.configure(text = self._indicator_text(False, ''))

    def _indicator_text(self, stable, name):
        return "Stable: " + str(stable) + "\nPattern: " + name

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

file_name = 'patterns' if not sys.argv[1] else sys.argv[1]
print(file_name)
print(sys.argv)
patterns = Reader(file_name).patterns()
hopfield = Hopfield(patterns['patterns'])

root = tk.Tk()
app = Application(size=patterns['pattern_size'], master=root)
app.mainloop()
