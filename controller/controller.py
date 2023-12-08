from view.view import StudentGroupView
from model.model import StudentGroupModel

class StudentGroupController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.button_add.config(command=self.add_relationship)
        self.view.button_color.config(command=self.perform_graph_coloring)

    def add_relationship(self):
        try:
            relationship = [int(x) for x in self.view.entry.get().split()]
            if len(relationship) != 2:
                raise ValueError("Please enter two valid student IDs.")
            self.model.add_relationship(*relationship)
            self.view.entry.delete(0, "end")  # Clear the entry field
        except ValueError as e:
            self.view.display_error(str(e))

    def perform_graph_coloring(self):
        try:
            self.model.perform_graph_coloring()
            subgroup_colors = self.model.get_subgroup_colors()
            self.view.display_results(subgroup_colors)
        except Exception as e:
            self.view.display_error(str(e))
