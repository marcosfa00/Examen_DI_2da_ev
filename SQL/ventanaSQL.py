import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QListWidget,
                             QComboBox, QFrame, QSlider, QGroupBox, QTableWidget, QTableView, QLineEdit)


class VentanaTabla(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tabla normal')
        self.setFixedSize(550, 500)

        main_layout = QVBoxLayout()

        parte1 = QHBoxLayout()
        parte2 = QHBoxLayout()

        main_layout.addLayout(parte1)
        main_layout.addLayout(parte2)

        # establecemos que tipo de base de datos es
        miBaseDeDatos = QSqlDatabase("QSQLITE")
        miBaseDeDatos.setDatabaseName("database.dat")
        miBaseDeDatos.open()

        # creamos la tabla
        cuadradoTabla = QWidget()
        layoutTabla = QHBoxLayout()

        # creamso elemento tabla
        tabla = QTableView()
        modelo = QSqlTableModel(db =miBaseDeDatos)
        tabla.setModel(modelo)

        # a mayores por ser SQL
        modelo.setTable("usuarios")
        modelo.select()

        layoutTabla.addWidget(tabla)
        cuadradoTabla.setLayout(layoutTabla)

        parte1.addWidget(cuadradoTabla)


        botonera = QWidget()
        layoutBotones = QHBoxLayout()
        nuevoElemento =  ['1234E', 'Perez', 30, 'Hombre', True]

        botonAdd= QPushButton('añadir')
        botonAdd.clicked.connect(lambda: self.botonAdd(modelo, nuevoElemento))

        layoutBotones.addWidget(botonAdd)
        botonera.setLayout(layoutBotones)

        parte2.addWidget(botonera)













        container = QWidget()
        container.setLayout(main_layout)

        # Establecemos el contenedor como el widget central
        self.setCentralWidget(container)

        # Mostramos la ventana
        self.show()



    def botonAdd(self, modelo, nuevoElemento):
        # Obtener el número de filas actual
        numRows = modelo.rowCount()

        # Insertar una nueva fila al final
        modelo.insertRow(numRows)

        # Establecer valores para la nueva fila usando el array proporcionado
        for col, valor in enumerate(nuevoElemento):
            modelo.setData(modelo.index(numRows, col), valor)

        # Confirmar los cambios en la base de datos
        modelo.submitAll()


if __name__ == "__main__":
        aplicacion = QApplication(sys.argv)
        ventana = VentanaTabla()
        sys.exit(aplicacion.exec())







