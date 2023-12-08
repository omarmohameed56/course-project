from model.model import StudentGroupModel
from view.view import StudentGroupView
from controller.controller import StudentGroupController
import tkinter as tk


def main():
    root = tk.Tk()
    model = StudentGroupModel(num_students=0)
    view = StudentGroupView(root)
    controller = StudentGroupController(model, view)
    root.mainloop()




main()