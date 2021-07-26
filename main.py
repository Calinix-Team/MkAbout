import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def mask_image(imgdata, imgtype ='jpg', size = 270):
  
    # Load image
    image = QImage.fromData(imgdata, imgtype)
  
    # convert image to 32-bit ARGB (adds an alpha
    # channel ie transparency factor):
    image.convertToFormat(QImage.Format_ARGB32)
  
    # Crop image to a square:
    imgsize = min(image.width(), image.height())
    rect = QRect(
        (image.width() - imgsize) / 2,
        (image.height() - imgsize) / 2,
        imgsize,
        imgsize,
     )
       
    image = image.copy(rect)
  
    # Create the output image with the same dimensions 
    # and an alpha channel and make it completely transparent:
    out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
    out_img.fill(Qt.transparent)
  
    # Create a texture brush and paint a circle 
    # with the original image onto the output image:
    brush = QBrush(image)
  
    # Paint the output image
    painter = QPainter(out_img)
    painter.setBrush(brush)
  
    # Don't draw an outline
    painter.setPen(Qt.NoPen)
  
    # drawing circle
    painter.drawEllipse(0, 0, imgsize, imgsize)
  
    # closing painter event
    painter.end()
  
    # Convert the image to a pixmap and rescale it. 
    pr = QWindow().devicePixelRatio()
    pm = QPixmap.fromImage(out_img)
    pm.setDevicePixelRatio(pr)
    size *= pr
    pm = pm.scaled(size, size, Qt.KeepAspectRatio, 
                               Qt.SmoothTransformation)
  
    # return back the pixmap data
    return pm
   
class window(QWidget):
   def __init__(self, parent = None):
      super(window, self).__init__(parent)
      self.setStyleSheet("background-image: linear-gradient(right, antiquewhite, grey);; filter: blur(50);");
      self.resize(900,500)
      self.setWindowTitle("About This Mac")
      self.label = QLabel(self)
      self.label.setText("MkOsh Monterey 12.0")
      font = QFont()
      font.setFamily("Arial")
      font.setBold(True)
      font.setPointSize(27)
      self.label.setFont(font)
      self.label.move(400,100)
      self.label = QLabel(self)
      self.label.setText("Version 12.0.1")
      font = QFont()
      font.setFamily("Arial")
      font.setPointSize(14)
      self.label.setFont(font)
      self.label.move(400,137)

      self.label = QLabel(self)
      self.label.setText("ASUS Vivobook 14, 14-inch 2020")
      font = QFont()
      font.setFamily("Helvetica")
      font.setPointSize(14)
      font.setBold(True)
      self.label.setFont(font)
      self.label.move(400, 197)

      self.label = QLabel(self)
      self.label.setText("Processor ")
      font = QFont()
      font.setFamily("Helvetica")
      font.setPointSize(14)
      font.setBold(True)
      self.label.setFont(font)
      self.label.move(400, 224)

      self.label = QLabel(self)
      self.label.setText("2.3 GHz AMD Athlon Silver 3050U ")
      font = QFont()
      font.setFamily("Helvetica")
      font.setPointSize(14)
      self.label.setFont(font)
      self.label.move(500, 224)

      self.label = QLabel(self)
      self.label.setText("Memory ")
      font = QFont()
      font.setFamily("Helvetica")
      font.setPointSize(14)
      font.setBold(True)
      self.label.setFont(font)
      self.label.move(400, 251)

      self.label = QLabel(self)
      self.label.setText("4 GB 2666 MHz SO-DIMM DDR4")
      font = QFont()
      font.setFamily("Helvetica")
      font.setPointSize(14)
      self.label.setFont(font)
      self.label.move(500, 251)

    
      self.label = QLabel(self)
      self.label.setText("Graphics ")
      font = QFont()
      font.setFamily("Helvetica")
      font.setPointSize(14)
      font.setBold(True)
      self.label.setFont(font)
      self.label.move(400, 277)

      self.label = QLabel(self)
      self.label.setText("Radeon R2 Graphics")
      font = QFont()
      font.setFamily("Helvetica")
      font.setPointSize(14)
      self.label.setFont(font)
      self.label.move(500, 277)

      self.label = QLabel(self)
      self.label.setText("0XX34DX3DH1U28H-MC")
      font = QFont()
      font.setFamily("Helvetica")
      font.setPointSize(14)
      self.label.setFont(font)
      self.label.move(500, 302)

      self.label = QLabel(self)
      self.label.setText("Serial No.")
      font = QFont()
      font.setBold(True)
      font.setFamily("Helvetica")
      font.setPointSize(14)
      self.label.setFont(font)
      self.label.move(400, 302)

      button = QPushButton('Overview', self)
      button.setToolTip('Your Mk Device')
      button.move(200,20)
      button.resize(80, 30)

      button = QPushButton('Displays', self)
      button.setToolTip('View and Manage Displays')
      button.move(290,20)
      button.resize(80, 30)

      button = QPushButton('Storage', self)
      button.setToolTip('View Storage Capacity')
      button.move(380,20)
      button.resize(80, 30)

      button = QPushButton('Support', self)
      button.setToolTip('Mapple Support')
      button.move(470,20)
      button.resize(80, 30)

      button = QPushButton('Service', self)
      button.setToolTip('Mapple Services')
      button.move(560,20)
      button.resize(80, 30)

      button = QPushButton('System Report...', self)
      button.setToolTip('Report Problems of your system to Mapple')
      button.move(400,360)
      button.resize(150, 30)

      button = QPushButton('Software Update...', self)
      button.setToolTip('Update your system')
      button.move(560,360)
      button.resize(150, 30)

      # image path
      imgpath = "morn.jpg"

      # loading image
      imgdata = open(imgpath, 'rb').read()

      # calling the function
      pixmap = mask_image(imgdata)

      # creating label
      self.ilabel = QLabel(self)

      # putting image on label
      self.ilabel.setPixmap(pixmap)

      # moving the label
      self.ilabel.move(50, 100)

      
def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   main()