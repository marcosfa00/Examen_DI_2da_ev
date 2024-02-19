from PyQt6.QtGui import QColor, QIcon
# importamos del pyqt6 los elementos que nos importa -> ventana principal, boton
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout,
    QLineEdit, QHBoxLayout, QTableView, QWidget, QComboBox, QCheckBox
)

from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex

"""

       self.datosTabla = [
    # aquí dentro se definen los datos a poner en una tabla

    # la primera fila siempre van a ser los campos de las columnas
    ['Nombre', 'Apellidos', 'Edad', 'Sexo', 'Trabajando'],
    
    
    ['Juan', 'Perez', 30, 'Hombre', True],
    ['María', 'Gómez', 25, 'Mujer', False],
    ['Carlos', 'López', 35, 'Hombre', True],
    ['Carlos', 'Perez', 35, 'Hombre', True],
    # ... Puedes agregar más filas según sea necesario
]
        
        
"""
class ModeloTabla(QAbstractTableModel):
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla


    def rowCount(self, index):
        return len(self.tabla)

    def columnCount(self, index):
        return len(self.tabla[0])


    def data(self, index, rol):
        if index.isValid():

            if rol == Qt.ItemDataRole.EditRole or rol == Qt.ItemDataRole.DisplayRole:
                valor = self.tabla[index.row()][index.column()]
                return valor

            if rol == Qt.ItemDataRole.ForegroundRole:

                if self.tabla[index.row()][4] == True:
                    return QColor("red")

            if rol == Qt.ItemDataRole.BackgroundRole:

                if self.tabla[index.row()][1] == "Perez":
                    return QColor("yellow")

            if rol == Qt.ItemDataRole.DecorationRole:
                # ahora preguntamos, si el primer condicional (En este caso solo hay uno, pero podría haber varios) es Verdadero
                if isinstance(self.tabla[index.row()][index.column()], bool):
                    if self.tabla[index.row()][4] == True:
                        return QIcon("check.png")
                    else:
                        return QIcon("uncheck.png")





    def setData(self, index, valor,rol):
        if  rol == Qt.ItemDataRole.EditRole:
            self.tabla[index.row()][index.column()] = valor
            return True
        return False


    def flags(self, index):
        if index.row() == 0:
            return Qt.ItemFlag.ItemIsEnabled
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable

