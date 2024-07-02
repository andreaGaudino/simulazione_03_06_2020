import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None



    def load_interface(self):
        # title
        self._title = ft.Text("simulazione esame 24/01/2024", color="blue", size=24)
        self._page.controls.append(self._title)

        #row1
        self.txtGoalFatti = ft.TextField(label="Goal fatti")
        self.btnCreaGrafo = ft.ElevatedButton(text="Crea grafo", on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([ft.Container(self.txtGoalFatti, width=300),
                       ft.Container(self.btnCreaGrafo, width=300)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)

        #row 2
        self.btnTopPlayer = ft.ElevatedButton(text="Top player", on_click=self._controller.handleTopPlayer, disabled = True)
        row2 = ft.Row([ft.Container(self.btnTopPlayer, width=300)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)

        #row3
        self.numeroGiocatori = ft.TextField(label="Numero giocatori")
        self.btnDreamTeam = ft.ElevatedButton(text="Dream Team", on_click=self._controller.handleDreamTeam, disabled = True)
        row3 = ft.Row([ft.Container(self.numeroGiocatori, width=300),
                       ft.Container(self.btnDreamTeam, width=300)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row3)

        self.txtGrafo = ft.ListView()
        self.txtTopPlayer = ft.ListView(expand=1)
        self.txtDreamTeam = ft.ListView(expand=1)

        self._page.add(self.txtGrafo)
        self._page.add(self.txtTopPlayer)
        self._page.add(self.txtDreamTeam)
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
