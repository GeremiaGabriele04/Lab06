import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillddAnno(self):
        for b in self._model.getAllAnno():
            self._view.ddAnno.options.append(ft.dropdown.Option(key=b, data=b, on_click=self._choiceDDAnno))
            pass

    def fillddBrand(self):
        for b in self._model.getAllBrand():
            self._view.ddBrand.options.append(ft.dropdown.Option(key=b, data=b, on_click=self._choiceDDBrand))
            pass
    def fillddRetailer(self):
        for b in self._model.getAllRetailer():
            self._view.ddRetailer.options.append(ft.dropdown.Option(key=b, data=b, on_click=self._choiceDDRetailer))
            pass

    def handleTopVendite(self):
        pass

    def handleAnalizzaVendite(self):
        pass

    def _choiceDDBrand(self, e):
        self._ddBrandValue = e.control.data
        print(self._ddBrandValue)

    def _choiceDDRetailer(self, e):
        self._ddRetailerValue = e.control.data
        print(self._ddRetailerValue)

    def _choiceDDAnno(self, e):
        self._ddAnnoValue = e.control.data
        print(self._ddAnnoValue)

