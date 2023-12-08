def graph_coloring(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    color_assigned = [-1] * num_vertices
    available_colors = set(range(num_vertices))

    def is_safe(vertex, color):
        for neighbor in range(num_vertices):
            if adjacency_matrix[vertex][neighbor] and color_assigned[neighbor] == color:
                return False
        return True

    def color_graph_util(vertex):
        nonlocal available_colors

        if vertex == num_vertices:
            return True  # All vertices are colored

        for color in available_colors.copy():
            if is_safe(vertex, color):
                color_assigned[vertex] = color
                available_colors.discard(color)

                if color_graph_util(vertex + 1):
                    return True  # If coloring is successful

                # Backtrack if coloring is not successful
                color_assigned[vertex] = -1
                available_colors.add(color)

        return False  # If no color can be assigned to the vertex

    color_graph_util(0)  # Start coloring from the first vertex
    return color_assigned