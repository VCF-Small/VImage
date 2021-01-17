from PyQt5.QtWidgets import QFileDialog
import webbrowser
from numpy import load, array
from os.path import splitext
from PIL import Image, ImageQt, ImageEnhance
from numpy.lib.npyio import save
DarkStyleSheet = '''QSlider::groove:horizontal{height:10px;margin:0 0}QSlider::handle:horizontal{background-color:#0096fa;border:1px;border-radius:3px;height:40px;width:40px;margin:0 0}QSlider::handle:horizontal:hover{background-color:#00c896;border:1px;border-radius:3px;height:40px;width:40px;margin:0 0}*{font:8pt "MS Shell Dlg 2"}#Tool_Box QLabel{font:10pt "MS Shell Dlg 2"}QGroupBox{color:#fff}QPushButton{background-color:#282828;border:none;border-radius:5px}QPushButton:hover{background-color:#323232;border:none}QPushButton:pressed{background-color:#0a0a0a;border:none}#VImage_Main{background-color:#1e1e1e}QLabel{color:#fff}QMenuBar{background:#282828;color:#fff}QMenu{background:#282828;color:#fff}'''
LightStyleSheet = '''QSlider::groove:horizontal{height:10px;margin:0 0}QSlider::handle:horizontal{background-color:#0096fa;border:1px;border-radius:3px;height:40px;width:40px;margin:0 0}QSlider::handle:horizontal:hover{background-color:#00c896;border:1px;border-radius:3px;height:40px;width:40px;margin:0 0}*{font:8pt "MS Shell Dlg 2"}#Tool_Box QLabel{font:10pt "MS Shell Dlg 2"}QPushButton{background-color:#e6f0f0;border:none;border-radius:5px}QPushButton:hover{background-color:#e6ffff;border:none}QPushButton:pressed{background-color:#c8ffff;border:none}#VImage_Main{background-color:#fff}'''

def Open():
    src_path, _ = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg *.npy)")
    if(src_path != "" or src_path != None):
        name, exten = splitext(src_path)
        image = None
        if(exten == ".npy"):
            data = load(src_path)
            image = Image.fromarray(data)
        else:
            image = Image.open(src_path)
        return(src_path, ImageQt.ImageQt(image), image)
    else:
        return
def Save(image, dst_path):
    data = array(image)
    save(dst_path, data)

def SaveAs(image):
    dst_path, _ = QFileDialog.getSaveFileName(filter="VImage (*.npy)")
    if(dst_path == ""):
        return
    elif(dst_path != None):
        data = array(image)
        save(dst_path, data)
        return dst_path
    else:
        return

def DarkMode(window):
    window.setStyleSheet(DarkStyleSheet)
    
def LightMode(window):
    window.setStyleSheet(LightStyleSheet)
    
def AboutVCF():
    webbrowser.open("http://vcfstudio.in/about")

def AboutVImage():
    pass

def ExportPNG(image):
    dst_path, _ = QFileDialog.getSaveFileName(filter="PNG (*.png)")
    if(dst_path == ""):
        return
    image.save(dst_path)

def ExportJPG(image):
    dst_path, _ = QFileDialog.getSaveFileName(filter="JPG (*.jpg *.jpeg)")
    if(dst_path == ""):
        return
    jpg_image = image.convert("RGB")
    jpg_image.save(dst_path)

def ExportPDF(image):
    dst_path, _ = QFileDialog.getSaveFileName(filter="PDF (*.pdf)")
    if(dst_path == ""):
        return
    pdf_image = image.convert("RGB")
    pdf_image.save(dst_path)

