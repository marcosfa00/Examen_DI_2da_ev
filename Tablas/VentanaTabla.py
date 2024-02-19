import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QListWidget,
                             QComboBox, QFrame, QSlider, QGroupBox, QTableWidget, QTableView, QLineEdit)

from ModeloTabla import ModeloTabla

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

        # botonera
        botonera = QWidget()
        layoutBotones = QVBoxLayout()

        # ceamos los botones
        botonAdd = QPushButton('Añadir')
        botonEdit = QPushButton('Editar')
        botonDelete = QPushButton('Borrar')

        layoutBotones.addWidget(botonAdd)
        layoutBotones.addWidget(botonEdit)
        layoutBotones.addWidget(botonDelete)

        botonera.setLayout(layoutBotones)

        parte1.addWidget(botonera)

        # textos
        textos = QWidget()
        layoutTextos = QVBoxLayout()

        # añadimos los textos
        '''  ['Nombre', 'Apellidos', 'Edad', 'Sexo', 'Trabajando'],'''
        lblName = QLabel('Nombre')
        txtName = QLineEdit()
        lblApellido = QLabel('Apellidos')
        txtApellidos = QLineEdit()
        lblEdad = QLabel('Edad')
        txtEdad = QLineEdit()
        lblSexo = QLabel('Sexo')
        txtSexo = QLineEdit()

        checkBoxWork = QCheckBox('Trabajando')

        layoutTextos.addWidget(lblName)
        layoutTextos.addWidget(txtName)

        layoutTextos.addWidget(lblApellido)
        layoutTextos.addWidget(txtApellidos)

        layoutTextos.addWidget(lblEdad)
        layoutTextos.addWidget(txtEdad)

        layoutTextos.addWidget(lblSexo)
        layoutTextos.addWidget(txtSexo)


        layoutTextos.addWidget(checkBoxWork)

        textos.setLayout(layoutTextos)

        parte1.addWidget(textos)


    # creamos los datos de la tabla
        self.datosTabla =[
            # titulo -> Header
            ['Nombre', 'Apellidos', 'Edad', 'Sexo', 'Trabajando'],
            # datos de la tabla
            ['Juan', 'Perez', 30, 'Hombre', True],
            ['María', 'Gómez', 25, 'Mujer', False],
            ['Carlos', 'López', 35, 'Hombre', True],
            ['Carlos', 'Perez', 35, 'Hombre', True],



        ]

# parte dos creamos la tabla
        cuadradoTabla = QWidget()
        layoutTabla = QHBoxLayout()



# elementos
        tabla = QTableView()
        modelo = ModeloTabla(self.datosTabla)
        tabla.setModel(modelo)

        layoutTabla.addWidget(tabla)

        cuadradoTabla.setLayout(layoutTabla)

        parte2.addWidget(cuadradoTabla)
















        container = QWidget()
        container.setLayout(main_layout)

        # Establecemos el contenedor como el widget central
        self.setCentralWidget(container)

        # Mostramos la ventana
        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaTabla()
    sys.exit(aplicacion.exec())
