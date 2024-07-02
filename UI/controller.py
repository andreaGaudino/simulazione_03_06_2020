import warnings

import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model



    def handleCreaGrafo(self, e):
        media = self._view.txtGoalFatti.value
        if media == "":
            self._view.create_alert("Media gol non inserita")
            return
        try:
            mediaFloat = float(media)
        except ValueError:
            self._view.create_alert("Media gol inserita non numerica")
            return
        self._model.buildGraph(mediaFloat)
        n,e = self._model.graphDetails()
        self._view.txtGrafo.clean()
        self._view.txtGrafo.controls.append(ft.Text(f"Grafo creato con {n} nodi e {e} archi"))
        self._view.btnTopPlayer.disabled = False
        self._view.btnDreamTeam.disabled = False
        self._view.update_page()


    def handleTopPlayer(self, e):
        nodo, lista = self._model.getTopPlayer()
        final = []
        for l in lista:
            final.append((l[1], int(l[2]["weight"])))
        self._view.txtTopPlayer.clean()
        self._view.txtTopPlayer.controls.append(ft.Text(f"Top player: {nodo}"))
        self._view.txtTopPlayer.controls.append(ft.Text(f"Avversari battuti:"))
        final.sort(key=lambda x: x[1], reverse=True)
        for i in final:
            self._view.txtTopPlayer.controls.append(ft.Text(f"{i[0]} | {i[1]}"))
        self._view.update_page()



    def handleDreamTeam(self, e):
        nGiocatori = self._view.numeroGiocatori.value
        if nGiocatori == "":
            self._view.create_alert("Numero giocatori non inserito")
            return
        try:
            nGiocatoriInt = float(nGiocatori)
        except ValueError:
            self._view.create_alert("Numero giocatori inserito non numerico")
            return

        gradoTitolarita, solBest = self._model.getDreaTeam(nGiocatoriInt)
        self._view.txtDreamTeam.clean()
        self._view.txtDreamTeam.controls.append(ft.Text(f"Il Dream Team creato ha grado di titolarità {gradoTitolarita}"))
        for n in solBest:
            self._view.txtDreamTeam.controls.append(
                ft.Text(f"{n} - {self._model.getTitolarita(n)}"))
        self._view.update_page()


    def fillDD(self):
        pass


           