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
        botonAdd.clicked.connect(lambda: self.addToTable(txtName,txtApellidos,txtEdad,txtSexo,checkBoxWork,tabla))
        botonEdit = QPushButton('Editar')
        botonDelete = QPushButton('Borrar')
        botonDelete.clicked.connect(lambda: self.borrarFila(tabla))

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
        tabla.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)

        parte2.addWidget(cuadradoTabla)

        self.seleccion = tabla.selectionModel()  # Selección de la fila
        self.seleccion.selectionChanged.connect(lambda: self.rellenarCampos(tabla,txtName,txtApellidos,txtEdad,txtSexo,checkBoxWork)) # Conexión de la señal de selección de fila con el método 'on_filaSeleccionada'

        container = QWidget()
        container.setLayout(main_layout)

        # Establecemos el contenedor como el widget central
        self.setCentralWidget(container)

        # Mostramos la ventana
        self.show()

    def addToTable(self, nombre, apellidos, edad, sexo,trabajando, tabla):
        fila =[]
        fila.append(nombre.text())
        fila.append(apellidos.text())
        fila.append(edad.text())
        fila.append(sexo.text())
        if  trabajando.checkState():
            fila.append(True)
        else:
            fila.append(False)
            print(fila)
        tabla.model().tabla.append(fila)
        tabla.model().layoutChanged.emit()

    def borrarFila(self, tabla):
        indice = tabla.currentIndex()
        print(f"Fila a eliminar: {indice.row()}")
        if indice.isValid():
            tabla.model().removeRow(indice.row())  # Se elimina la fila seleccionada
            print("Eliminada con exito!")
            tabla
    def rellenarCampos(self, tabla,nombre, apellidos, edad, sexo,trabajando ):

        indice =  tabla.selectedIndexes()
        if indice != []: # si el indice actual no es igual a una fila vacía
                nombre.setText(indice[0].data())
                apellidos.setText(indice[1].data())
                edad.setText(str(indice[2].data()))
                sexo.setText(indice[3].data())
                if trabajando.checkState():
                    trabajando.setChecked(True)
                else:
                    trabajando.setChecked(False)

               # self.borrarFila(tabla)



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaTabla()
    sys.exit(aplicacion.exec())
