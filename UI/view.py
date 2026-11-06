import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        self.dd_biblioteca = ft.Dropdown(
            label="Biblioteca",
            hint_text="Seleziona biblioteca",
            options=[ft.dropdown.Option("Nessun filtro")],
            on_select=self.controller.seleziona_biblioteca,
            width=300
        )
        self.dd_genere = ft.Dropdown(
            label="Genere",
            hint_text="Seleziona genere",
            options=[ft.dropdown.Option("Nessun filtro")],
            on_select=self.controller.seleziona_genere,
            width=300
        )

        # Sezione 3: Libri
        self.btn_mostra_libri = ft.Button(
            content="Mostra Libri",
            on_click=self.controller.mostra_libri
        )
        self.list_view = ft.ListView(expand=1, spacing=10, padding=10)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row([self.dd_biblioteca, self.dd_genere], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Libri
            ft.Row([self.btn_mostra_libri], alignment=ft.MainAxisAlignment.CENTER),
            self.list_view
        )

        self.page.scroll = "adaptive"
        self.page.update()
        self.controller.popola_dropdown()
    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
