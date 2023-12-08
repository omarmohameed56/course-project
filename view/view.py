import tkinter as tk
from tkinter import messagebox

class StudentGroupView:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grouping Tool")

        # Model initialization (for example purposes)
        self.model = None

        # GUI components
        self.label = tk.Label(root, text="Enter relationships (e.g., 0 1 for student 0 and student 1):")
        self.entry = tk.Entry(root)
        self.button_add = tk.Button(root, text="Add Relationship", command=self.add_relationship)
        self.button_color = tk.Button(root, text="Perform Graph Coloring", command=self.perform_graph_coloring)
        self.result_label = tk.Label(root, text="Subgroup Colors:")
        self.result_text = tk.Text(root, height=5, width=30, state=tk.DISABLED)

        # Layout
        self.label.pack(pady=10)
        self.entry.pack(pady=5)
        self.button_add.pack(pady=5)
        self.button_color.pack(pady=10)
        self.result_label.pack(pady=5)
        self.result_text.pack(pady=5)


    def add_relationship(self):
        try:
            relationship = [int(x) for x in self.entry.get().split()]
            if len(relationship) != 2:
                raise ValueError("Please enter two valid student IDs.")
            self.model.add_relationship(*relationship)
            self.entry.delete(0, tk.END)  # Clear the entry field
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def perform_graph_coloring(self):
        try:
            self.model.perform_graph_coloring()
            subgroup_colors = self.model.get_subgroup_colors()
            self.display_results(subgroup_colors)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_results(self, subgroup_colors):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        for student, color in enumerate(subgroup_colors):
            self.result_text.insert(tk.END, f"Student {student}: Subgroup {color}\n")
        self.result_text.config(state=tk.DISABLED)
        
    def display_error(self, message):
        tk.messagebox.showerror("Error", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentGroupView(root)
    root.mainloop()




