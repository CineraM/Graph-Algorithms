import pandas as pd

class TitleDictionary:

    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.title_dict = self._create_title_dict()
        self.profession_dict = self._create_profession_dict()

    def _create_title_dict(self):
        title_dict = {}
        data = self.df.values.tolist()

        for entry in data:
            title = entry[2]
            if entry[1] in title_dict:
                title_dict[entry[1]].append(title)
            else:
                title_dict[entry[1]] = [title]

        # print(title_dict['nm6081065']) # debug
        return title_dict 

    def _create_profession_dict(self):
        profession_dict = {}
        data = self.df.values.tolist()

        for entry in data:
            if entry[1] not in profession_dict:
                profession = entry[3]
                if entry[4] == 'actor':
                    profession+='_a'
                else:
                    profession+='_d'

                profession_dict[entry[1]] = profession

        # print(profession_dict['nm6446679']) # debug
        return profession_dict

#Graph Network Creation
class MovieNetwork:
    def __init__(self, name_movie_dict, nconst_ar_dr):
        self.graph = {} 
        self.name_movie_dict = name_movie_dict 
        self.nconst_ar_dr = nconst_ar_dr 
        
    def add_node(self, node):
        self.graph[node] = {}

    def edge_bi(self, node1, node2, weigh):
        if node1 not in self.graph: self.add_node(node1)
        if node2 not in self.graph: self.add_node(node2)

        if node2 not in self.graph[node1]:
            self.graph[node1][node2] = weigh

        if node1 not in self.graph[node2]:
            self.graph[node2][node1] = weigh

    def edge_single(self, node1, node2, weigh):
        if node1 not in self.graph: self.add_node(node1)
        if node2 not in self.graph: self.add_node(node2)
        
        if node2 not in self.graph[node1]:
            self.graph[node1][node2] = weigh

    # nconst_ar_dr, weight=1
    # old parameters, not needed
    def add_edge(self, node1, node2):
        node1_movies = self.name_movie_dict[node1]
        node2_movies = self.name_movie_dict[node2]

        empty_set = set()
        # checking movies in common
        for movie in node1_movies:
            if movie in node2_movies:
                # weight+=1
                empty_set.add(movie)
        
        weight = len(empty_set)
                
        # only proceed if weights are more than 2
        if weight > 2:
            node1_ar_dr = self.nconst_ar_dr[node1]
            node1_profession = node1_ar_dr[len(node1_ar_dr)-1:]

            node2_ar_dr = self.nconst_ar_dr[node2]
            node2_profession = node2_ar_dr[len(node2_ar_dr)-1:]

            if node1_profession == node2_profession:
                self.edge_bi(node1, node2, weight)
            if node1_profession == "a" and node2_profession == "d":
                self.edge_single(node2, node1, weight)
            if node1_profession == "d" and node2_profession == "a":
                self.edge_single(node1, node2, weight)

    def get_graph(self):
        for node1 in self.nconst_ar_dr:
            for node2 in self.nconst_ar_dr:
                if node1 == node2:
                    continue
                if node1 not in self.graph: self.add_node(node1)
                if node2 not in self.graph: self.add_node(node2)
                self.add_edge(node1, node2)
        
        return self.graph