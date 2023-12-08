from utils.algorithm import graph_coloring

class StudentGroupModel:
    def __init__(self, num_students):
        self.num_students = num_students
        self.adjacency_matrix = [[0] * num_students for _ in range(num_students)]
        self.subgroup_colors = [-1] * num_students

    def add_relationship(self, student1, student2):
        """
        Add a relationship between two students to the adjacency matrix.
        """
        self.adjacency_matrix[student1][student2] = 1
        self.adjacency_matrix[student2][student1] = 1

    def get_relationships(self, student):
        """
        Get the relationships of a given student.
        """
        return [i for i, is_connected in enumerate(self.adjacency_matrix[student]) if is_connected]

    def perform_graph_coloring(self):
        """
        Perform graph coloring using the adjacency matrix.
        """
        self.subgroup_colors = graph_coloring(self.adjacency_matrix)

    def set_subgroup_color(self, student, color):
        """
        Set the subgroup color of a student.
        """
        self.subgroup_colors[student] = color

    def get_subgroup_colors(self):
        """
        Get the subgroup colors assigned to each student.
        """
        return self.subgroup_colors
