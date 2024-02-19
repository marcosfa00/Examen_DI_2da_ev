import sys
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QVBoxLayout, QHBoxLayout, QTableView)

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

        # Establecemos qué tipo de base de datos es
        miBaseDeDatos = QSqlDatabase("QSQLITE")
        miBaseDeDatos.setDatabaseName("database.dat")
        miBaseDeDatos.open()

        # Creamos la tabla
        tabla = QTableView()
        modelo = QSqlTableModel(db=miBaseDeDatos)
        tabla.setModel(modelo)

        # Añadimos por ser SQL
        modelo.setTable("usuarios")
        modelo.select()

        parte1.addWidget(tabla)

        botonera = QWidget()
        layoutBotones = QHBoxLayout()

        botonAdd = QPushButton('Añadir')
        botonAdd.clicked.connect(lambda: self.botonAdd(modelo))

        botonEliminar = QPushButton("Eliminar")
        botonEliminar.clicked.connect(lambda: self.eliminarElemento(modelo, tabla))

        botonGuardar = QPushButton('Guardar')
        botonGuardar.clicked.connect(lambda: self.botonSave(modelo))

        layoutBotones.addWidget(botonAdd)
        layoutBotones.addWidget(botonEliminar)  # Corregido el nombre del botón
        layoutBotones.addWidget(botonGuardar)
        botonera.setLayout(layoutBotones)

        parte2.addWidget(botonera)

        container = QWidget()
        container.setLayout(main_layout)

        # Establecemos el contenedor como el widget central
        self.setCentralWidget(container)

        # Mostramos la ventana
        self.show()

    def eliminarElemento(self, modelo, tabla):
        # Obtener el índice de la fila seleccionada
        indice_fila_seleccionada = tabla.currentIndex().row()
        # Verificar si hay una fila seleccionada
        if indice_fila_seleccionada >= 0:
            # Eliminar la fila seleccionada
            modelo.removeRow(indice_fila_seleccionada)
            # Confirmar los cambios en la base de datos
            modelo.submitAll()

    def botonAdd(self, modelo):
        nuevoElemento = ['Juan', 'Perez', 30, 'Hombre', True]
        # Obtener el número de filas actual
        numRows = modelo.rowCount()

        # Insertar una nueva fila al final
        modelo.insertRow(numRows)

        # Establecer valores para la nueva fila usando el array proporcionado
        for col, valor in enumerate(nuevoElemento):
            modelo.setData(modelo.index(numRows, col), valor)

        # Confirmar los cambios en la base de datos
        modelo.submitAll()

    def botonSave(self, modelo):
        modelo.submitAll()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaTabla()
    sys.exit(aplicacion.exec())
