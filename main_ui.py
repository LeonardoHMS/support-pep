# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import img_rc as img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(886, 758)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	background-color: rgb(33,45,51);\n"
"	border:none\n"
"\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 6, 0, 6)
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(0, 16777215))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fm_title = QFrame(self.left_menu)
        self.fm_title.setObjectName(u"fm_title")
        self.fm_title.setFrameShape(QFrame.StyledPanel)
        self.fm_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fm_title)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.fm_title)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.fm_title)

        self.fm_menu = QFrame(self.left_menu)
        self.fm_menu.setObjectName(u"fm_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fm_menu.sizePolicy().hasHeightForWidth())
        self.fm_menu.setSizePolicy(sizePolicy)
        self.fm_menu.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	background-color: rgb(229,249,255);\n"
"	border-top-left-radius: 15px;\n"
"	color: rgb(92,115,134);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"	color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"	\n"
"	background-color: rgba(61,80,95,100);\n"
"	\n"
"}")
        self.fm_menu.setFrameShape(QFrame.StyledPanel)
        self.fm_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.fm_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_home = QPushButton(self.fm_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 28))
        font = QFont()
        font.setPointSize(12)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_ente = QPushButton(self.fm_menu)
        self.btn_ente.setObjectName(u"btn_ente")
        self.btn_ente.setMinimumSize(QSize(0, 28))
        self.btn_ente.setFont(font)
        self.btn_ente.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_ente)

        self.btn_contatos = QPushButton(self.fm_menu)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(0, 28))
        self.btn_contatos.setFont(font)
        self.btn_contatos.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_contatos)

        self.btn_config = QPushButton(self.fm_menu)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setMinimumSize(QSize(0, 28))
        self.btn_config.setFont(font)
        self.btn_config.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_config)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.fm_menu)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setStyleSheet(u"")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/_img/_img/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(37, 37))

        self.horizontalLayout_3.addWidget(self.btn_toggle, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(33,45,51);\n"
"}")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_17 = QVBoxLayout(self.pg_home)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_11 = QFrame(self.pg_home)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 16))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_15 = QLabel(self.frame_11)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_15.addWidget(self.label_15)


        self.verticalLayout_17.addWidget(self.frame_11)

        self.frame_3 = QFrame(self.pg_home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_5.addWidget(self.label_11)

        self.txt_dia_inicial = QLineEdit(self.frame_4)
        self.txt_dia_inicial.setObjectName(u"txt_dia_inicial")
        self.txt_dia_inicial.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setPointSize(20)
        self.txt_dia_inicial.setFont(font1)
        self.txt_dia_inicial.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_dia_inicial.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.txt_dia_inicial, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_11.addWidget(self.label_12)

        self.txt_dia_final = QLineEdit(self.frame_5)
        self.txt_dia_final.setObjectName(u"txt_dia_final")
        self.txt_dia_final.setMinimumSize(QSize(0, 25))
        self.txt_dia_final.setFont(font1)
        self.txt_dia_final.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_dia_final.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.txt_dia_final, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.frame_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_17.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.pg_home)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_12.addWidget(self.label_13)

        self.txt_hora_inicial = QLineEdit(self.frame_7)
        self.txt_hora_inicial.setObjectName(u"txt_hora_inicial")
        self.txt_hora_inicial.setMinimumSize(QSize(0, 25))
        self.txt_hora_inicial.setFont(font1)
        self.txt_hora_inicial.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_hora_inicial.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.txt_hora_inicial)


        self.horizontalLayout_8.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_13.addWidget(self.label_14)

        self.txt_hora_final = QLineEdit(self.frame_8)
        self.txt_hora_final.setObjectName(u"txt_hora_final")
        self.txt_hora_final.setMinimumSize(QSize(0, 25))
        self.txt_hora_final.setFont(font1)
        self.txt_hora_final.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_hora_final.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.txt_hora_final)


        self.horizontalLayout_8.addWidget(self.frame_8)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.verticalLayout_17.addWidget(self.frame_6)

        self.frame_12 = QFrame(self.pg_home)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_13)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_16 = QLabel(self.frame_13)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_16.addWidget(self.label_16)

        self.txt_operadores = QLineEdit(self.frame_13)
        self.txt_operadores.setObjectName(u"txt_operadores")
        self.txt_operadores.setMinimumSize(QSize(0, 25))
        self.txt_operadores.setFont(font1)
        self.txt_operadores.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_operadores.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.txt_operadores, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_14)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_14.addWidget(self.label_17)

        self.txt_tempo_stop = QLineEdit(self.frame_14)
        self.txt_tempo_stop.setObjectName(u"txt_tempo_stop")
        self.txt_tempo_stop.setMinimumSize(QSize(0, 25))
        self.txt_tempo_stop.setFont(font1)
        self.txt_tempo_stop.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_tempo_stop.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.txt_tempo_stop, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.frame_14)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_17.addWidget(self.frame_12)

        self.frame_9 = QFrame(self.pg_home)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_5 = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.btn_confirmar = QPushButton(self.frame_9)
        self.btn_confirmar.setObjectName(u"btn_confirmar")
        self.btn_confirmar.setMinimumSize(QSize(100, 30))
        self.btn_confirmar.setFont(font)
        self.btn_confirmar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confirmar.setStyleSheet(u"QPushButton{\n"
"\n"
"	color: rgb(229,249,255);\n"
"	background-color:rgb(121, 160, 196);\n"
"	border-radius: 15px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_confirmar)

        self.btn_limpar = QPushButton(self.frame_9)
        self.btn_limpar.setObjectName(u"btn_limpar")
        self.btn_limpar.setMinimumSize(QSize(100, 30))
        self.btn_limpar.setFont(font)
        self.btn_limpar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_limpar.setStyleSheet(u"QPushButton{\n"
"\n"
"	color: rgb(229,249,255);\n"
"	background-color:rgb(121, 160, 196);\n"
"	border-radius: 15px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_limpar)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)


        self.verticalLayout_17.addWidget(self.frame_9)

        self.label_resultado = QLabel(self.pg_home)
        self.label_resultado.setObjectName(u"label_resultado")
        sizePolicy.setHeightForWidth(self.label_resultado.sizePolicy().hasHeightForWidth())
        self.label_resultado.setSizePolicy(sizePolicy)
        self.label_resultado.setStyleSheet(u"background-color: rgba(61,80,95,100);")

        self.verticalLayout_17.addWidget(self.label_resultado)

        self.Pages.addWidget(self.pg_home)
        self.pg_sap = QWidget()
        self.pg_sap.setObjectName(u"pg_sap")
        self.verticalLayout_7 = QVBoxLayout(self.pg_sap)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.pg_sap)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.label_3)

        self.frame = QFrame(self.pg_sap)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.txt_file = QLineEdit(self.frame)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setMinimumSize(QSize(0, 28))
        font2 = QFont()
        font2.setPointSize(11)
        self.txt_file.setFont(font2)
        self.txt_file.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.frame)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(120, 27))
        font3 = QFont()
        font3.setFamilies([u"MS UI Gothic"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.btn_open.setFont(font3)
        self.btn_open.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"\n"
"	color: rgb(229,249,255);\n"
"	background-color:rgb(121, 160, 196);\n"
"	border-top-right-radius: 15px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(47,47,47);\n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.btn_open)


        self.verticalLayout_7.addWidget(self.frame)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tb_ente = QTableWidget(self.pg_sap)
        if (self.tb_ente.columnCount() < 15):
            self.tb_ente.setColumnCount(15)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_ente.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        self.tb_ente.setObjectName(u"tb_ente")
        self.tb_ente.setStyleSheet(u"QHeaderView::section{\n"
"\n"
"	background-color: rgb(121,160,196);\n"
"	color: rgb(255,255,255);	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"QTableWidget{\n"
"\n"
"	background-color: rgb(252, 252, 252);\n"
"\n"
"}\n"
"")
        self.tb_ente.horizontalHeader().setDefaultSectionSize(110)

        self.horizontalLayout_6.addWidget(self.tb_ente)

        self.fm_comandos = QFrame(self.pg_sap)
        self.fm_comandos.setObjectName(u"fm_comandos")
        self.fm_comandos.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	background-color: rgb(229,249,255);\n"
"	border-radius: 15px;\n"
"	color: rgb(92,115,134);\n"
"\n"
"}\n"
"QPushButton{\n"
"\n"
"	color: rgb(255,255,255);\n"
"	background-color: none;\n"
"\n"
"}\n"
"QFrame{\n"
"\n"
"	background-color: rgb(121,160,196);\n"
"	border-radius: 10px;\n"
"\n"
"}")
        self.fm_comandos.setFrameShape(QFrame.StyledPanel)
        self.fm_comandos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.fm_comandos)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_ini_ent = QPushButton(self.fm_comandos)
        self.btn_ini_ent.setObjectName(u"btn_ini_ent")
        self.btn_ini_ent.setMinimumSize(QSize(100, 30))
        self.btn_ini_ent.setFont(font)
        self.btn_ini_ent.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ini_ent.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_ini_ent)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.btn_clipboard = QPushButton(self.fm_comandos)
        self.btn_clipboard.setObjectName(u"btn_clipboard")
        self.btn_clipboard.setMinimumSize(QSize(0, 30))
        self.btn_clipboard.setFont(font)

        self.verticalLayout_6.addWidget(self.btn_clipboard)

        self.btn_excel = QPushButton(self.fm_comandos)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(0, 30))
        self.btn_excel.setFont(font)
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btn_excel)


        self.horizontalLayout_6.addWidget(self.fm_comandos)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.Pages.addWidget(self.pg_sap)
        self.pg_config = QWidget()
        self.pg_config.setObjectName(u"pg_config")
        self.verticalLayout_8 = QVBoxLayout(self.pg_config)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.pg_config)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4)

        self.frame_10 = QFrame(self.pg_config)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	background-color: rgb(229,249,255);\n"
"	border-radius: 15px;\n"
"	color: rgb(92,115,134);\n"
"\n"
"}\n"
"QPushButton{\n"
"\n"
"	color: rgb(255,255,255);\n"
"	background-color: none;\n"
"\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_16)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.frame_17)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)


        self.verticalLayout_22.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_18)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy1)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_19)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.txt_user = QLineEdit(self.frame_19)
        self.txt_user.setObjectName(u"txt_user")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_user.sizePolicy().hasHeightForWidth())
        self.txt_user.setSizePolicy(sizePolicy2)
        self.txt_user.setMinimumSize(QSize(150, 25))
        self.txt_user.setFont(font)
        self.txt_user.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.txt_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.txt_user, 0, Qt.AlignHCenter)

        self.txt_password = QLineEdit(self.frame_19)
        self.txt_password.setObjectName(u"txt_password")
        sizePolicy2.setHeightForWidth(self.txt_password.sizePolicy().hasHeightForWidth())
        self.txt_password.setSizePolicy(sizePolicy2)
        self.txt_password.setMinimumSize(QSize(150, 25))
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.txt_password, 0, Qt.AlignHCenter)

        self.txt_acess = QLineEdit(self.frame_19)
        self.txt_acess.setObjectName(u"txt_acess")
        sizePolicy2.setHeightForWidth(self.txt_acess.sizePolicy().hasHeightForWidth())
        self.txt_acess.setSizePolicy(sizePolicy2)
        self.txt_acess.setMinimumSize(QSize(150, 25))
        self.txt_acess.setFont(font)
        self.txt_acess.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_acess.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.txt_acess, 0, Qt.AlignHCenter)

        self.btn_confirm_login = QPushButton(self.frame_19)
        self.btn_confirm_login.setObjectName(u"btn_confirm_login")
        self.btn_confirm_login.setMinimumSize(QSize(100, 30))
        self.btn_confirm_login.setFont(font)
        self.btn_confirm_login.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_20.addWidget(self.btn_confirm_login, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.frame_19)


        self.verticalLayout_22.addWidget(self.frame_18)


        self.verticalLayout_18.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame_10)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_15)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.txt_folder = QLineEdit(self.frame_20)
        self.txt_folder.setObjectName(u"txt_folder")
        self.txt_folder.setMinimumSize(QSize(0, 28))
        self.txt_folder.setFont(font2)
        self.txt_folder.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_folder.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.txt_folder)

        self.btn_folder = QPushButton(self.frame_20)
        self.btn_folder.setObjectName(u"btn_folder")
        self.btn_folder.setMinimumSize(QSize(120, 30))
        self.btn_folder.setFont(font)
        self.btn_folder.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.btn_folder)


        self.verticalLayout_19.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_15)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_21)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.btn_confirm_folder = QPushButton(self.frame_21)
        self.btn_confirm_folder.setObjectName(u"btn_confirm_folder")
        self.btn_confirm_folder.setMinimumSize(QSize(100, 30))
        self.btn_confirm_folder.setFont(font)
        self.btn_confirm_folder.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_23.addWidget(self.btn_confirm_folder)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_3)


        self.verticalLayout_19.addWidget(self.frame_21, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_15)


        self.verticalLayout_8.addWidget(self.frame_10)

        self.Pages.addWidget(self.pg_config)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_10 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.pg_contatos)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.frame_2 = QFrame(self.pg_contatos)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_9.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_9.addWidget(self.label_8)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_9.addWidget(self.label_10)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_9.addWidget(self.label_9)


        self.verticalLayout_10.addWidget(self.frame_2)

        self.Pages.addWidget(self.pg_contatos)

        self.verticalLayout_4.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.fm_footer = QFrame(self.main_container)
        self.fm_footer.setObjectName(u"fm_footer")
        self.fm_footer.setFrameShape(QFrame.StyledPanel)
        self.fm_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.fm_footer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.fm_footer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.fm_footer)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">OpCalculator 3.0</span></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_ente.setText(QCoreApplication.translate("MainWindow", u"ENTE - SAP", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_config.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.btn_toggle.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Calculo tempo de produ\u00e7\u00e3o</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Dia Inicial</span></p></body></html>", None))
        self.txt_dia_inicial.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Dia Final</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Hora In\u00edcial</span></p></body></html>", None))
        self.txt_hora_inicial.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Hora Final</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Operadores</span></p></body></html>", None))
        self.txt_operadores.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Tempo Parado</span></p></body></html>", None))
        self.txt_tempo_stop.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Parada", None))
        self.btn_confirmar.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.btn_limpar.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.label_resultado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Resultado aqui</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">ENTE - SAP</span></p></body></html>", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a planilha com os dados -->", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"OPEN FILE", None))
        ___qtablewidgetitem = self.tb_ente.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ordem", None));
        ___qtablewidgetitem1 = self.tb_ente.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        ___qtablewidgetitem2 = self.tb_ente.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Txt.brv.material", None));
        ___qtablewidgetitem3 = self.tb_ente.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Lista comp.item", None));
        ___qtablewidgetitem4 = self.tb_ente.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Requirement date", None));
        ___qtablewidgetitem5 = self.tb_ente.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Qtd.necess\u00e1ria(EINHEIT)", None));
        ___qtablewidgetitem6 = self.tb_ente.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Qtd.retirada(EINHEIT)", None));
        ___qtablewidgetitem7 = self.tb_ente.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Qtd.Falta", None));
        ___qtablewidgetitem8 = self.tb_ente.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Unid.medida b\u00e1sica(=EINHEIT)", None));
        ___qtablewidgetitem9 = self.tb_ente.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Dep\u00f3sito", None));
        ___qtablewidgetitem10 = self.tb_ente.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Centro de trabalho", None));
        ___qtablewidgetitem11 = self.tb_ente.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do centro de trabalho", None));
        ___qtablewidgetitem12 = self.tb_ente.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Refugo da opera\u00e7\u00e3o %", None));
        ___qtablewidgetitem13 = self.tb_ente.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Status do sistema", None));
        ___qtablewidgetitem14 = self.tb_ente.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Texto", None));
        self.btn_ini_ent.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.btn_clipboard.setText(QCoreApplication.translate("MainWindow", u"ClipBoard", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">CONFIGURA\u00c7\u00d5ES</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">DEFINIR LOGIN SAP</span></p></body></html>", None))
        self.txt_user.setText("")
        self.txt_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"usu\u00e1rio", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"senha", None))
        self.txt_acess.setPlaceholderText(QCoreApplication.translate("MainWindow", u"acesso", None))
        self.btn_confirm_login.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.txt_folder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione o Local para salvar Arquivos -->", None))
        self.btn_folder.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.btn_confirm_folder.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">CONTATOS</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/_img/_img/githublogo.png\"/><span style=\" font-size:18pt; color:#ffffff; vertical-align:super;\">LeonardoHMS</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Linkedin</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/_img/_img/instagram.png\"/><span style=\" color:#ffffff;\">\u200e \u200e \u200e </span><span style=\" font-size:18pt; color:#ffffff; vertical-align:super;\">@cleandark</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Discord", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Manrope,sans-serif'; font-size:12pt; font-weight:600; color:#ffffff;\">\u00a9 LeonardoHMS</span></p></body></html>", None))
    # retranslateUi

