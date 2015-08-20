import sys
import tkinter as tk
import tkinter.messagebox

class Hanoi:
    def __init__(self, num):
        self.num = num
        self.peg_a = []
        self.peg_b = []
        self.peg_c = []
        for i in range(0, num):
            self.peg_a.append(num-i)
        print("A:", end=' ')
        for i in range(0, len(self.peg_a)):
            print(self.peg_a[i], end=' ')
        print("\nB:")
        print("C:")

    def display(self, peg_a, peg_b, peg_c):
        print("\nA:", end=' ')
        for i in range(0, len(self.peg_a)):
            print(self.peg_a[i], end=' ')
        print("\nB:", end=' ')
        for i in range(0, len(self.peg_b)):
            print(self.peg_b[i], end=' ')
        print("\nC:", end=' ')
        for i in range(0, len(self.peg_c)):
            print(self.peg_c[i], end=' ')
        print()
                
    def move(self, giver, taker):
        taker.insert(len(taker), giver[len(giver)-1])
        giver.remove(giver[len(giver)-1])
        self.display(self.peg_a, self.peg_b, self.peg_c)

    def solve(self, num, source, target, helper):
        if num == 1:
            self.move(source, target)
        else:
            self.solve(num-1, source, helper, target)
            self.move(source, target)
            self.solve(num-1, helper, target, source)

def check_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

submitted = input()

if check_int(submitted) == True:
    disk_num = int(submitted)
    hanoi = Hanoi(disk_num)
    hanoi.solve(disk_num, hanoi.peg_a, hanoi.peg_b, hanoi.peg_c)
else:
    tkinter.messagebox.showinfo("Error", "Wrong Input")
    root = tk.Tk()
    root.withdraw()
    exit()
