class AdjacencyMatrix():

    # O(V^2) for space
    def __init__(self):
        raise NotImplementedError  # no tests
        self.__mat = []
        self.__vertex_index_mapping = {}

    # O(V)
    def add_vertex(self, vertex_id):
        if vertex_id in self.__vertex_index_mapping.keys():
            return
        self.__mat.append([])
        for index in range(0, len(self.__mat)):
            while len(self.__mat[index]) < len(self.__mat):
                self.__mat[index].append(False)
        latest_index = len(self.__mat) - 1
        self.__vertex_index_mapping[vertex_id] = latest_index

    # O(V)
    def remove_vertex(self, vertex_id):
        index = self.__vertex_index_mapping[vertex_id]
        for i in range(0, len(self.__mat)):
            if i != index:
                del self.__mat[i][index]
        del self.__mat[index]
        self.__vertex_index_mapping.pop(vertex_id)

    # O(1)
    def add_edge(self, vertex_id_1, vertex_id_2):
        index_1 = self.__vertex_index_mapping[vertex_id_1]
        index_2 = self.__vertex_index_mapping[vertex_id_2]
        self.__mat[index_1][index_2] = True

    # O(1)
    def remove_edge(self, vertex_id_1, vertex_id_2):
        index_1 = self.__vertex_index_mapping[vertex_id_1]
        index_2 = self.__vertex_index_mapping[vertex_id_2]
        self.__mat[index_1][index_2] = False

    # O(V)
    def is_vertex_exists(self, vertex_id):
        return vertex_id in self.__vertex_index_mapping.keys()

    # O(1)
    def is_edge_exists(self, vertex_id_1, vertex_id_2):
        index_1 = self.__vertex_index_mapping[vertex_id_1]
        index_2 = self.__vertex_index_mapping[vertex_id_2]
        return self.__mat[index_1][index_2]

    def __str__(self):
        s = ""
        for row in self.__mat:
            for col in row:
                s += " "
                s += "T" if col else "F"
            s += "\n"
        return s
