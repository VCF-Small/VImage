# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Himanshu\Desktop\Files\Projects\VImage\VImage\src\Designs\VImage_Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageQt
import numpy

class Ui_VImage_Main(object):
    def setupUi(self, VImage_Main):
        VImage_Main.setObjectName("VImage_Main")
        VImage_Main.resize(1358, 904)
        VImage_Main.setMinimumSize(QtCore.QSize(640, 480))
        VImage_Main.setStyleSheet("QSlider::groove:horizontal {height: 10px; margin: 0 0;}\n"
                                  "QSlider::handle:horizontal {background-color: rgb(0,150,250); border: 1px; border-radius:3px; height: \n"
                                  "40px; width: 40px; margin: 0 0;}\n"
                                  "QSlider::handle:horizontal:hover {background-color: rgb(0,200,150); border: 1px; border-radius:3px; height: \n"
                                  "    40px; width: 40px; margin: 0 0;}\n"
                                  "*{\n"
                                  "    \n"
                                  "    font: 8pt \"MS Shell Dlg 2\";\n"
                                  "}\n"
                                  "#Tool_Box QLabel{\n"
                                  "\n"
                                  "    font: 10pt \"MS Shell Dlg 2\";\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton{\n"
                                  "    background-color:rgb(230,240,240);\n"
                                  "border:none;\n"
                                  "border-radius: 5px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "    background-color:rgb(230,255,255);\n"
                                  "    border:none;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed{\n"
                                  "    background-color:rgb(200,255,255);\n"
                                  "    border:none;\n"
                                  "}\n"
                                  "\n"
                                  "#VImage_Main{\n"
                                  "    background-color:rgb(255,255,255);\n"
                                  "}\n"
                                  "\n"
                                  "")
        self.centralwidget = QtWidgets.QWidget(VImage_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Filter_Box = QtWidgets.QGroupBox(self.centralwidget)
        self.Filter_Box.setMaximumSize(QtCore.QSize(16777215, 120))
        self.Filter_Box.setObjectName("Filter_Box")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Filter_Box)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Template_Label_1 = QtWidgets.QLabel(self.Filter_Box)
        self.Template_Label_1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Template_Label_1.setText("")
        self.Template_Label_1.setObjectName("Template_Label_1")
        self.gridLayout_3.addWidget(self.Template_Label_1, 0, 0, 1, 1)
        self.Template_Label_2 = QtWidgets.QLabel(self.Filter_Box)
        self.Template_Label_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Template_Label_2.setText("")
        self.Template_Label_2.setObjectName("Template_Label_2")
        self.gridLayout_3.addWidget(self.Template_Label_2, 0, 1, 1, 1)
        self.Template_Label_7 = QtWidgets.QLabel(self.Filter_Box)
        self.Template_Label_7.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Template_Label_7.setText("")
        self.Template_Label_7.setObjectName("Template_Label_7")
        self.gridLayout_3.addWidget(self.Template_Label_7, 0, 6, 1, 1)
        self.Template_Label_4 = QtWidgets.QLabel(self.Filter_Box)
        self.Template_Label_4.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Template_Label_4.setText("")
        self.Template_Label_4.setObjectName("Template_Label_4")
        self.gridLayout_3.addWidget(self.Template_Label_4, 0, 3, 1, 1)
        self.Template_Label_8 = QtWidgets.QLabel(self.Filter_Box)
        self.Template_Label_8.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Template_Label_8.setText("")
        self.Template_Label_8.setObjectName("Template_Label_8")
        self.gridLayout_3.addWidget(self.Template_Label_8, 0, 7, 1, 1)
        self.Template_Label_3 = QtWidgets.QLabel(self.Filter_Box)
        self.Template_Label_3.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Template_Label_3.setText("")
        self.Template_Label_3.setObjectName("Template_Label_3")
        self.gridLayout_3.addWidget(self.Template_Label_3, 0, 2, 1, 1)
        self.Template_Label_6 = QtWidgets.QLabel(self.Filter_Box)
        self.Template_Label_6.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Template_Label_6.setText("")
        self.Template_Label_6.setObjectName("Template_Label_6")
        self.gridLayout_3.addWidget(self.Template_Label_6, 0, 5, 1, 1)
        self.Template_Label_5 = QtWidgets.QLabel(self.Filter_Box)
        self.Template_Label_5.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Template_Label_5.setText("")
        self.Template_Label_5.setObjectName("Template_Label_5")
        self.gridLayout_3.addWidget(self.Template_Label_5, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.Filter_Box, 0, 1, 1, 1)
        self.Image_Box = QtWidgets.QGroupBox(self.centralwidget)
        self.Image_Box.setObjectName("Image_Box")
        self.Image_Label = QtWidgets.QLabel(self.Image_Box)
        self.Image_Label.setGeometry(QtCore.QRect(10, 20, 1161, 701))
        self.Image_Label.setMouseTracking(True)
        self.Image_Label.setText("")
        self.Image_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Image_Label.setObjectName("Image_Label")
        self.gridLayout.addWidget(self.Image_Box, 1, 1, 1, 1)
        self.Tool_Box = QtWidgets.QGroupBox(self.centralwidget)
        self.Tool_Box.setMaximumSize(QtCore.QSize(230, 16777215))
        self.Tool_Box.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.Tool_Box.setObjectName("Tool_Box")
        self.formLayout = QtWidgets.QFormLayout(self.Tool_Box)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.Tool_Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label)
        self.Brightness_Slider = QtWidgets.QSlider(self.Tool_Box)
        self.Brightness_Slider.setMinimum(-100)
        self.Brightness_Slider.setMaximum(100)
        self.Brightness_Slider.setRange(-100, 100)
        self.Brightness_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Brightness_Slider.setObjectName("Brightness_Slider")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.SpanningRole, self.Brightness_Slider)
        self.label_2 = QtWidgets.QLabel(self.Tool_Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.Tool_Box)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.SpanningRole, self.label_3)
        self.Sharpness_Slider = QtWidgets.QSlider(self.Tool_Box)
        self.Sharpness_Slider.setMinimum(-100)
        self.Sharpness_Slider.setMaximum(100)
        self.Sharpness_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Sharpness_Slider.setObjectName("Sharpness_Slider")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.SpanningRole, self.Sharpness_Slider)
        self.label_4 = QtWidgets.QLabel(self.Tool_Box)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.SpanningRole, self.label_4)
        self.Saturation_Slider = QtWidgets.QSlider(self.Tool_Box)
        self.Saturation_Slider.setMinimum(-100)
        self.Saturation_Slider.setMaximum(100)
        self.Saturation_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Saturation_Slider.setObjectName("Saturation_Slider")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.SpanningRole, self.Saturation_Slider)
        self.label_5 = QtWidgets.QLabel(self.Tool_Box)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.SpanningRole, self.label_5)
        self.Hue_Slider = QtWidgets.QSlider(self.Tool_Box)
        self.Hue_Slider.setMinimum(-100)
        self.Hue_Slider.setMaximum(100)
        self.Hue_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Hue_Slider.setObjectName("Hue_Slider")
        self.formLayout.setWidget(
            10, QtWidgets.QFormLayout.SpanningRole, self.Hue_Slider)
        self.Rotate_Box = QtWidgets.QGroupBox(self.Tool_Box)
        self.Rotate_Box.setMinimumSize(QtCore.QSize(0, 100))
        self.Rotate_Box.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.Rotate_Box.setObjectName("Rotate_Box")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Rotate_Box)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Rotate_Right_Button = QtWidgets.QPushButton(self.Rotate_Box)
        self.Rotate_Right_Button.setText("")
        icon = QtGui.QIcon()
<<<<<<< Updated upstream
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Himanshu\\Desktop\\Files\\Projects\\VImage\\VImage-1\\src\\Source\\icons\\rotate_right_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
=======
        icon.addPixmap(QtGui.QPixmap(
            "C:\\Users\\Ankit\\Desktop\\VImage\\src\\Source\\icons\\rotate_right_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
>>>>>>> Stashed changes
        self.Rotate_Right_Button.setIcon(icon)
        self.Rotate_Right_Button.setIconSize(QtCore.QSize(48, 48))
        self.Rotate_Right_Button.setObjectName("Rotate_Right_Button")
        self.gridLayout_4.addWidget(self.Rotate_Right_Button, 0, 2, 1, 1)
        self.Rotate_Flip_Button = QtWidgets.QPushButton(self.Rotate_Box)
        self.Rotate_Flip_Button.setMinimumSize(QtCore.QSize(0, 50))
        self.Rotate_Flip_Button.setText("")
        icon1 = QtGui.QIcon()
<<<<<<< Updated upstream
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Himanshu\\Desktop\\Files\\Projects\\VImage\\VImage-1\\src\\Source\\icons\\rotate_flip_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
=======
        icon1.addPixmap(QtGui.QPixmap(
            "C:\\Users\\Ankit\\Desktop\\VImage\\src\\Source\\icons\\rotate_flip_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
>>>>>>> Stashed changes
        self.Rotate_Flip_Button.setIcon(icon1)
        self.Rotate_Flip_Button.setIconSize(QtCore.QSize(48, 48))
        self.Rotate_Flip_Button.setObjectName("Rotate_Flip_Button")
        self.gridLayout_4.addWidget(self.Rotate_Flip_Button, 0, 1, 1, 1)
        self.Rotate_Left_Button = QtWidgets.QPushButton(self.Rotate_Box)
        self.Rotate_Left_Button.setAutoFillBackground(False)
        self.Rotate_Left_Button.setText("")
        icon2 = QtGui.QIcon()
<<<<<<< Updated upstream
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\Himanshu\\Desktop\\Files\\Projects\\VImage\\VImage-1\\src\\Source\\icons\\rotate_left_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
=======
        icon2.addPixmap(QtGui.QPixmap(
            "C:\\Users\\Ankit\\Desktop\\VImage\\src\\Source\\icons\\rotate_left_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
>>>>>>> Stashed changes
        self.Rotate_Left_Button.setIcon(icon2)
        self.Rotate_Left_Button.setIconSize(QtCore.QSize(48, 48))
        self.Rotate_Left_Button.setObjectName("Rotate_Left_Button")
        self.gridLayout_4.addWidget(self.Rotate_Left_Button, 0, 0, 1, 1)
        self.formLayout.setWidget(
            11, QtWidgets.QFormLayout.SpanningRole, self.Rotate_Box)
        self.Contrast_Slider = QtWidgets.QSlider(self.Tool_Box)
        self.Contrast_Slider.setMinimum(-100)
        self.Contrast_Slider.setMaximum(100)
        self.Contrast_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Contrast_Slider.setObjectName("Contrast_Slider")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.SpanningRole, self.Contrast_Slider)
        self.gridLayout.addWidget(self.Tool_Box, 0, 0, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        VImage_Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VImage_Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1358, 16))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport = QtWidgets.QMenu(self.menuFile)
        self.menuExport.setObjectName("menuExport")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuTheme = QtWidgets.QMenu(self.menubar)
        self.menuTheme.setObjectName("menuTheme")
        VImage_Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VImage_Main)
        self.statusbar.setObjectName("statusbar")
        VImage_Main.setStatusBar(self.statusbar)
        self.actionVImage = QtWidgets.QAction(VImage_Main)
        self.actionVImage.setObjectName("actionVImage")
        self.actionVCF = QtWidgets.QAction(VImage_Main)
        self.actionVCF.setObjectName("actionVCF")
        self.actionOpen = QtWidgets.QAction(VImage_Main)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(VImage_Main)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(VImage_Main)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(VImage_Main)
        self.actionExit.setObjectName("actionExit")
        self.actionPNG = QtWidgets.QAction(VImage_Main)
        self.actionPNG.setObjectName("actionPNG")
        self.actionJPG = QtWidgets.QAction(VImage_Main)
        self.actionJPG.setObjectName("actionJPG")
        self.actionPDF = QtWidgets.QAction(VImage_Main)
        self.actionPDF.setObjectName("actionPDF")
        self.actionLight = QtWidgets.QAction(VImage_Main)
        self.actionLight.setObjectName("actionLight")
        self.actionDark = QtWidgets.QAction(VImage_Main)
        self.actionDark.setObjectName("actionDark")
        self.menuExport.addAction(self.actionPNG)
        self.menuExport.addAction(self.actionJPG)
        self.menuExport.addAction(self.actionPDF)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionVImage)
        self.menuAbout.addAction(self.actionVCF)
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addAction(self.actionDark)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuTheme.menuAction())
        #setupControl called here 
        self.setupControls()
        #*************************************

        ########## Menu Action ##################
        self._connectActions()
        #*****************************************#

        ########## Image processing ##################
        self.Image_Modifier()
        #*****************************************#

        self.retranslateUi(VImage_Main)
        QtCore.QMetaObject.connectSlotsByName(VImage_Main)

    def setupControls(self):
        
        pass

    def retranslateUi(self, VImage_Main):
        _translate = QtCore.QCoreApplication.translate
        VImage_Main.setWindowTitle(_translate(
            "VImage_Main", "VImage - Simple Image Manipulation"))
        self.Filter_Box.setTitle(_translate("VImage_Main", "Filters"))
        self.Image_Box.setTitle(_translate("VImage_Main", "Image"))
        self.Tool_Box.setTitle(_translate("VImage_Main", "Tool Box"))
        self.label.setText(_translate("VImage_Main", "Brightness"))
        self.label_2.setText(_translate("VImage_Main", "Contrast"))
        self.label_3.setText(_translate("VImage_Main", "Sharpness"))
        self.label_4.setText(_translate("VImage_Main", "Saturation"))
        self.label_5.setText(_translate("VImage_Main", "Hue"))
        self.Rotate_Box.setTitle(_translate("VImage_Main", "Rotate"))
        self.menuFile.setTitle(_translate("VImage_Main", "File"))
        self.menuExport.setTitle(_translate("VImage_Main", "Export"))
        self.menuAbout.setTitle(_translate("VImage_Main", "About"))
        self.menuTheme.setTitle(_translate("VImage_Main", "Theme"))
        self.actionVImage.setText(_translate("VImage_Main", "VImage"))
        self.actionVCF.setText(_translate("VImage_Main", "VCF"))
        self.actionOpen.setText(_translate("VImage_Main", "Open"))
        self.actionSave.setText(_translate("VImage_Main", "Save"))
        self.actionSave_As.setText(_translate("VImage_Main", "Save As"))
        self.actionExit.setText(_translate("VImage_Main", "Exit"))
        self.actionPNG.setText(_translate("VImage_Main", "PNG"))
        self.actionJPG.setText(_translate("VImage_Main", "JPG"))
        self.actionPDF.setText(_translate("VImage_Main", "PDF"))
        self.actionLight.setText(_translate("VImage_Main", "Light"))
        self.actionDark.setText(_translate("VImage_Main", "Dark"))

    ############## Menu Action function connecter #############################

    def _connectActions(self):
        self.actionOpen.triggered.connect(self.openImage)

    #*************************************************************#
    
    ############## Oen Image menu action #############################

    def openImage(self):
        self.file = QtWidgets.QFileDialog.getOpenFileName(self.Image_Label,'Single File','C:\'','*.png, *.jpg')
        self.loadImage()

    #*************************************************************#
    
    ############## initial load of image #############################

    def loadImage(self):
        self.Image_Label.setAutoFillBackground(False)
        self.Image_Label.setText("")
        image = QtGui.QPixmap(self.file[0])

        image = image.scaled(self.Image_Label.width(), self.Image_Label.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.Image_Label.setPixmap(image)
        self.Image_filters()

    #*************************************************************#
    
    ############## Image Modifier function connecter #############################

    def Image_Modifier(self):
        self.Brightness_Slider.valueChanged.connect(self.on_Brightness_slider_released)
        self.Contrast_Slider.valueChanged.connect(self.On_Contrast_slider_released)
        self.Sharpness_Slider.valueChanged.connect(self.on_sharpness_slider_released)
        self.Saturation_Slider.valueChanged.connect(self.on_Saturation_slider_released)
        self.Hue_Slider.valueChanged.connect(self.on_hue_slider_released)
        self.Rotate_Left_Button.clicked.connect(self.left_rotation)
        self.Rotate_Right_Button.clicked.connect(self.right_rotation)
        self.Rotate_Flip_Button.clicked.connect(self.flip_image)
    
    #*************************************************************#

    ############## Brightness slider #############################
    
    def on_Brightness_slider_released(self):
        factor = self.Brightness_Slider.value()

        #read image
        im = Image.open(self.file[0])

        #image brightness enhancer
        enhancer = ImageEnhance.Brightness(im)
        output_Image = enhancer.enhance(factor)
        output_Image.save("demo.jpg")
        self.loadImageOut()
    #*************************************************************#

    ############## Contrast slider #############################

    def On_Contrast_slider_released(self):
        factor = self.Contrast_Slider.value()
        factor /= 100


        #read image
        im = Image.open(self.file[0])

        #image contrast enhancer
        enhancer = ImageEnhance.Contrast(im)
        output_Image = enhancer.enhance(factor)
        output_Image.save("demo.jpg")
        self.loadImageOut()

    #*************************************************************#
    
    ############## Sharpness slider #############################
    
    def on_sharpness_slider_released(self):
        factor = self.Sharpness_Slider.value()

        #read image
        im = Image.open(self.file[0])

        #image sharpness enhancer
        enhancer = ImageEnhance.Sharpness(im)
        output_Image = enhancer.enhance(factor)
        output_Image.save("demo.jpg")
        self.loadImageOut()

    #*************************************************************#
    
    ############## Sharpness slider #############################

    def on_Saturation_slider_released(self):
        factor = self.Saturation_Slider.value()

        #read image
        im = Image.open(self.file[0])

        #image saturation enhancer
        enhancer = ImageEnhance.Color(im)
        output_Image = enhancer.enhance(factor)
        output_Image.save("demo.jpg")
        self.loadImageOut()
    
    #*************************************************************#

    ############## Hue slider #############################
    
    def on_hue_slider_released(self):
        factor = self.Hue_Slider.value()

        #read image
        im = Image.open(self.file[0])

        #image hue enhancer
        if(factor <= -34):
            layer = Image.new('RGB', im.size, 'red') # "hue" selection is done by choosing a color...
            output_Image = Image.blend(im, layer, (factor+66)/100)
            output_Image.save("demo.jpg")
        elif( 66< factor <= 32):
            layer = Image.new('RGB', im.size, 'green') # "hue" selection is done by choosing a color...
            if(factor < 0):
                output_Image = Image.blend(im, layer, (factor+66)/100)
                output_Image.save("demo.jpg")
            else:
                output_Image = Image.blend(im, layer, (66-factor)/100)
                output_Image.save("demo.jpg")
        else:
            layer = Image.new('RGB', im.size, 'blue') # "hue" selection is done by choosing a color...
            output_Image = Image.blend(im, layer, (66-factor)/100)
            output_Image.save("demo.jpg")
        self.loadImageOut()

    #*************************************************************#
    
    ############## load Image after Modification #############################

    def loadImageOut(self):
        self.Image_Label.setAutoFillBackground(False)
        self.Image_Label.setText("")
        image = QtGui.QPixmap("demo.jpg")

        image = image.scaled(self.Image_Label.width(), self.Image_Label.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.Image_Label.setPixmap(image)

    #*************************************************************#
    
    ############## Left Rotation #############################

    def left_rotation(self):
        #read image
        im = Image.open(self.file[0])

        #rotation
        output_Image = im.transpose(Image.ROTATE_90)
        output_Image.save("demo.jpg")
        self.loadImageOut()
    
    #*************************************************************#

    ############## Right Rotation #############################

    def right_rotation(self):
        #read image
        im = Image.open(self.file[0])

        #rotation
        output_Image = im.transpose(Image.ROTATE_270)
        output_Image.save("demo.jpg")
        self.loadImageOut()
    
    #*************************************************************#

    ############## flip image #############################

    def flip_image(self):
        #read image
        im = Image.open(self.file[0])

        #flip
        output_Image = ImageOps.mirror(im)
        output_Image.save("demo.jpg")
        self.loadImageOut()
    
    #*************************************************************#

    ############## Image Filters #############################

    def Image_filters(self):
        im = Image.open(self.file[0])

        filter1 = im.filter(ImageFilter.BLUR)
        filter2 = im.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 9, -1, -1, -1, -1), 1, 0))
        filter3 = im.filter(ImageFilter.EMBOSS)
        filter4 = im.filter(ImageFilter.MaxFilter(size=3))
        filter5 = im.filter(ImageFilter.CONTOUR)
        filter6 = im.filter(ImageFilter.EDGE_ENHANCE)
        filter7 = im.filter(ImageFilter.Smooth)
        filter8 = im.filter(ImageFilter.Sharpen)

        filter_img1 = self.PILimageToQImage(filter1)
        filter_img2 = self.PILimageToQImage(filter2)
        filter_img3 = self.PILimageToQImage(filter3)
        filter_img4 = self.PILimageToQImage(filter4)
        
        filter_img5 = self.PILimageToQImage(filter1)
        filter_img6 = self.PILimageToQImage(filter2)
        filter_img7 = self.PILimageToQImage(filter3)
        filter_img8 = self.PILimageToQImage(filter4)


        ###################### Filter 1 #################################

        self.Template_Label_1.setAutoFillBackground(False)
        self.Template_Label_1.setText("")
        image = QtGui.QPixmap(filter_img1)

        image = image.scaled(self.Template_Label_1.width(), self.Template_Label_1.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.Template_Label_1.setPixmap(image)

        #*************************************************************#

        ###################### Filter 2 #################################

        self.Template_Label_2.setAutoFillBackground(False)
        self.Template_Label_2.setText("")
        image = QtGui.QPixmap(filter_img2)

        image = image.scaled(self.Template_Label_2.width(), self.Template_Label_2.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.Template_Label_2.setPixmap(image)

        #*************************************************************#

        ###################### Filter 3 #################################

        self.Template_Label_3.setAutoFillBackground(False)
        self.Template_Label_3.setText("")
        image = QtGui.QPixmap(filter_img3)

        image = image.scaled(self.Template_Label_3.width(), self.Template_Label_3.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.Template_Label_3.setPixmap(image)

        #*************************************************************#

        ###################### Filter 4 #################################

        self.Template_Label_4.setAutoFillBackground(False)
        self.Template_Label_4.setText("")
        image = QtGui.QPixmap(filter_img4)

        image = image.scaled(self.Template_Label_4.width(), self.Template_Label_4.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.Template_Label_4.setPixmap(image)

        #*************************************************************#

        ###################### Filter 6 #################################

        self.Template_Label_6.setAutoFillBackground(False)
        self.Template_Label_6.setText("")
        image = QtGui.QPixmap(filter_img5)

        image = image.scaled(self.Template_Label_6.width(), self.Template_Label_6.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.Template_Label_6.setPixmap(image)

        #*************************************************************#

        ###################### Filter 6 #################################

        self.Template_Label_6.setAutoFillBackground(False)
        self.Template_Label_6.setText("")
        image = QtGui.QPixmap(filter_img6)

        image = image.scaled(self.Template_Label_6.width(), self.Template_Label_6.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.Template_Label_6.setPixmap(image)

        #*************************************************************#

        ###################### Filter 7 #################################

        self.Template_Label_7.setAutoFillBackground(False)
        self.Template_Label_7.setText("")
        image = QtGui.QPixmap(filter_img7)

        image = image.scaled(self.Template_Label_7.width(), self.Template_Label_7.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.Template_Label_7.setPixmap(image)

        #*************************************************************#

        ###################### Filter 8 #################################

        self.Template_Label_8.setAutoFillBackground(False)
        self.Template_Label_8.setText("")
        image = QtGui.QPixmap(filter_img8)

        image = image.scaled(self.Template_Label_8.width(), self.Template_Label_8.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.Template_Label_8.setPixmap(image)

        #*************************************************************#

    #*************************************************************#

    ###################### PTL image to QImage converter #################################

    def PILimageToQImage(self, pilimage):
        """converts a PIL image to QImage"""
        #convert PIL image to a PIL.ImageQt object
        imageq = numpy.array(pilimage.getdata()).reshape(pilimage.size[0], pilimage.size[1], 3)
        qimage = QtGui.QImage(imageq, imageq.shape[1], imageq.shape[0], QtGui.QImage.Format_RGB888) #cast PIL.ImageQt object to QImage object -that´s the trick!!!
        return qimage

    #*************************************************************#

    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VImage_Main = QtWidgets.QMainWindow()
    ui = Ui_VImage_Main()
    ui.setupUi(VImage_Main)
    VImage_Main.show()
    sys.exit(app.exec_())
