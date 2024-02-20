import sys
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QVBoxLayout, QHBoxLayout, QTableView, QLabel, QLineEdit, QCheckBox)

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
        # self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        # self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnRowChange)
        modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        tabla.setModel(modelo)

        # Añadimos por ser SQL
        modelo.setTable("usuarios")
        modelo.select()

        parte1.addWidget(tabla)

        self.seleccion = tabla.selectionModel()
        self.seleccion.selectionChanged.connect(lambda:self.editarElemento(tabla,modelo))
        tabla.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)# para seleccionar la tabla entera



        # botonera
        botonera = QWidget()
        layoutBotones = QHBoxLayout()

        botonAdd = QPushButton('Añadir')
        botonAdd.clicked.connect(lambda: self.botonAdd(modelo))

        botonEliminar = QPushButton("Eliminar")
        botonEliminar.clicked.connect(lambda: self.eliminarElemento(modelo, tabla))

        botonUpdate = QPushButton('Update')
        botonUpdate.clicked.connect(lambda: self.botonSave(modelo))



        layoutBotones.addWidget(botonAdd)
        layoutBotones.addWidget(botonEliminar)  # Corregido el nombre del botón
        layoutBotones.addWidget(botonUpdate)
        botonera.setLayout(layoutBotones)

        parte2.addWidget(botonera)

        # creamos los Line edit para editar Elementos de la tabla

        textos = QWidget()
        layouttextos  = QVBoxLayout()

        lblDNI = QLabel("dni:")
        self.textDNI = QLineEdit()
        lblName = QLabel("nombre:")
        self.textName = QLineEdit()
        lblEdad = QLabel("edad:")
        self.textEdad = QLineEdit()
        lblGenero = QLabel("genero:")
        self.textGenero = QLineEdit()
        self.checkTrabajando = QCheckBox("Trabajando")

        # añadimos todo al Layout

        layouttextos.addWidget(lblDNI)
        layouttextos.addWidget(self.textDNI)
        layouttextos.addWidget(lblName)
        layouttextos.addWidget(self.textName)
        layouttextos.addWidget(lblEdad)
        layouttextos.addWidget(self.textEdad)
        layouttextos.addWidget(lblGenero)
        layouttextos.addWidget(self.textGenero)
        layouttextos.addWidget(self.checkTrabajando)

        textos.setLayout(layouttextos)

        parte2.addWidget(textos)






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
        numRows = modelo.rowCount()

        # Obtener los valores de los QLineEdit y QCheckBox
        dni_valor = self.textDNI.text()
        name_valor = self.textName.text()
        edad_valor = self.textEdad.text()
        genero_valor = self.textGenero.text()
        trabajando_valor = self.checkTrabajando.isChecked()


        # Insertar una nueva fila al final
        modelo.insertRow(numRows)

        # Establecer valores para la nueva fila usando los datos proporcionados
        modelo.setData(modelo.index(numRows, 0), dni_valor)
        modelo.setData(modelo.index(numRows, 1), name_valor)
        modelo.setData(modelo.index(numRows, 2), edad_valor)
        modelo.setData(modelo.index(numRows, 3), genero_valor)
        modelo.setData(modelo.index(numRows, 4), trabajando_valor)

        # Confirmar los cambios en la base de datos
        modelo.submitAll()

        # Limpiar los QLineEdit y desmarcar el QCheckBox después de guardar
        self.textDNI.clear()
        self.textName.clear()
        self.textEdad.clear()
        self.textGenero.clear()
        self.checkTrabajando.setChecked(False)

    def editarElemento(self, tabla, modelo):
        indice = tabla.selectedIndexes()

        if indice != []:
            print(indice)
            self.textDNI.setText(indice[0].data())
            self.textName.setText(indice[1].data())
            self.textEdad.setText(str(indice[2].data()))
            self.textGenero.setText(str(indice[3].data()))
            if indice[4].data():
                self.checkTrabajando.setChecked(True)
            else:
                self.checkTrabajando.setChecked(False)

                self.eliminarElemento(modelo, tabla)












    '''
    
    def on_filaSeleccionada(self):
        indices = self.tvwTabla.selectedIndexes()
        if indices != []:
            print(indices)
            self.txtNombre.setText(self.datos[indices[0].row()][0])
            self.txtDni.setText(self.datos[indices[0].row()][1])
            self.cmbGenero.setCurrentText(self.datos[indices[0].row()][2])
            self.chkFallecido.setChecked(self.datos[indices[0].row()][3])

    '''
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaTabla()
    sys.exit(aplicacion.exec())
