import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self._nodes = []
        self._edges = []

        self.idMap = {}

        self._listChromosome = []
        self._listGenes = []
        self._listConnectedGenes = []

        self.loadGenes()
        self.loadChromosome()
        self.loadConnectedGenes()

    def loadChromosome(self):
        self._listChromosome = DAO.getAllChromosomes()

    def loadGenes(self):
        self._listGenes = DAO.getAllGenes()
        self.idMap = {}
        for g in self._listGenes:
            self.idMap[g.GeneID] = g.Chromosome

    def loadConnectedGenes(self):
        self._listConnectedGenes = DAO.getAllConnectedGenes()

    def build_graph(self):
        self._grafo.clear()

        for c in self._listChromosome:
            self._nodes.append(c)
        self._grafo.add_nodes_from(self._nodes)

        edges = {}
        for g1, g2, corr in self._listConnectedGenes:
            if(self.idMap[g1], self.idMap[g2]) not in edges:
                edges[(self.idMap[g1], self.idMap[g2])] = float(corr)
            else:
                edges[(self.idMap[g1], self.idMap[g2])] += float(corr)
        for k,v in edges.items():
            self._edges.append((k[0], k[1], v))
        self._grafo.add_weighted_edges_from(self._edges)



    def get_nodes(self):
        return self._grafo.nodes()
    def get_edges(self):
        return list(self._grafo.edges(data=True))

    def get_num_of_nodes(self):
        return self._grafo.number_of_nodes()
    def get_num_of_edges(self):
        return self._grafo.number_of_edges()

    def get_min_weight(self):
        return min([x[2]['weight'] for x in self.get_edges()])

    def get_max_weight(self):
        return max([x[2]['weight'] for x in self.get_edges()])

    def count_edges(self, s):
        bigger = 0
        smaller = 0
        for x in self.get_edges():
            if x[2]['weight'] > s:
                bigger +=1
            elif x[2]['weight'] < s:
                smaller +=1
        return bigger, smaller
