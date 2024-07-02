import copy
import random

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.idMap = {}


    def buildGraph(self, media):
        self.graph.clear()
        nodi = DAO.getNodi(media)
        for n in nodi:
            self.graph.add_node(n)
            self.idMap[n.id] = n
        archi = DAO.getArchi(media)
        for a in archi:
            self.graph.add_edge(self.idMap[a[0]], self.idMap[a[1]], weight = a[2])

    def getTopPlayer(self):
        battuti = {}
        for n in list(self.graph.nodes):
            battuti[n] = list(self.graph.out_edges(nbunch=n, data=True))
        sortato = sorted(battuti, key=lambda x: len(battuti[x]), reverse=True)
        return sortato[0], battuti[sortato[0]]


    def getDreaTeam(self, giocatori):
        self.solBest = []
        self.gradoTitolarita = 0

        for n in list(self.graph.nodes):
            parziale = []
            parziale.append(n)
            self.ricorsione(parziale, giocatori)
        print(self.gradoTitolarita, self.solBest)
        return self.gradoTitolarita, self.solBest

    def ricorsione(self, parziale, nMax):
        if len(parziale) == nMax:
            titolarita = 0
            for p in parziale:
                titolarita += self.getTitolarita(p)
            if titolarita > self.gradoTitolarita:
                self.gradoTitolarita = titolarita
                self.solBest = copy.deepcopy(parziale)
        else:
            nodi = list(self.graph.nodes)
            nodiAmmissibili = self.getAmmissibili(parziale, nodi)
            for n in nodiAmmissibili:
                parziale.append(n)
                self.ricorsione(parziale, nMax)
                parziale.pop()

    def getAmmissibili(self, parziale, nodi):
        ammissibili = []
        players = []
        for p in parziale:
            out = self.graph.out_edges(nbunch=p)
            for o in out:
                players.append(o[1])
        for n in nodi:
            if n not in parziale and n not in players:
                ammissibili.append(n)
        return ammissibili
    def getTitolarita(self, nodo):
        somma = 0
        for u in self.graph.out_edges(nbunch=nodo, data=True):
            somma += int(u[2]["weight"])
        for e in self.graph.in_edges(nbunch=nodo, data=True):
            somma -= int(e[2]["weight"])
        return somma

    def graphDetails(self):
        return len(self.graph.nodes), len(self.graph.edges)