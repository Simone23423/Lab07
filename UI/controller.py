import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        biblioteche = self._model.get_biblioteche()
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(b.nome))

        generi = self._model.get_generi()
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(g))

        self._view.update()

    # CALLBACKS DROPDOWN
    def seleziona_biblioteca(self, e):
        self.biblioteca_selezionata = e.control.value

    def seleziona_genere(self, e):
        self.genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        biblio = self.biblioteca_selezionata
        if biblio == "Nessun filtro" or biblio is None:
            biblio = None

        gen = self.genere_selezionato
        if gen == "Nessun filtro" or gen is None:
            gen = None

        libri = self._model.get_libri_filtrati(biblio, gen)

        self._view.list_view.controls.clear()
        if not libri:
            self._view.show_alert("Nessun libro soddisfa i criteri di filtraggio indicati.")
        else:
            for l in libri:
                self._view.list_view.controls.append(ft.Text(str(l)))
        self._view.update()
