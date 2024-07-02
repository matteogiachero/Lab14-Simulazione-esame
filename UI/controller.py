import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.build_graph()
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.get_num_of_nodes()} Numero di archi: {self._model.get_num_of_edges()}"))
        self._view.txt_result.controls.append(ft.Text(f"Valore minimo archi: {self._model.get_min_weight()} Valore massimo archi: {self._model.get_max_weight()}"))
        self._view.update_page()

    def handle_countedges(self, e):
        soglia = float(self._view.txt_name.value)
        if soglia < self._model.get_min_weight() or soglia > self._model.get_max_weight():
            self._view.create_alert("Valore non valido")
            return
        count_bigger, count_smaller = self._model.count_edges(soglia)
        self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso maggiore della soglia: {count_bigger}"))
        self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso minore della soglia: {count_smaller}"))
        self._view.update_page()

    def handle_search(self, e):
        pass