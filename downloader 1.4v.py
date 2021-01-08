from PyQt5.Qt import *
import sys
import pytube
import urllib.request
import os

app = QApplication(sys.argv)
dir_ = QDir("Cairo")
_id = QFontDatabase.addApplicationFont("Cairo-Bold.ttf")
dir_ = QDir("Cairo-light")
_id = QFontDatabase.addApplicationFont("Cairo-Light.ttf")
class Downloader(QDialog):

    def __init__(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        QDialog.__init__(self)
        layout = QFormLayout()
        self.playinglist = False
        self.i =0
        self.folder = ""
        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.file_name = QLineEdit()
        self.progress = QProgressBar()
        self.cb = QComboBox()
        self.formating = QComboBox()
        self.line = QLabel("The copyrights © for Azzam")
        self.line.setAlignment(Qt.AlignCenter)
        self.playlist = QCheckBox("قائمة يوتيوب")
        font = QFont("Cairo")
        font1 = QFont("Cairo-light")
        btn_download = QPushButton("بدء التحميل")
        btn_path = QPushButton("اختر مسار التحميل")
        btn_info = QPushButton("معلومات", self)
        btn_info.move(100,100)

        self.file_name.setPlaceholderText("ضع هنا اسم الملف")
        self.url.setPlaceholderText("رابط الفيديو المراد تحميله")
        self.cb.setPlaceholderText("دقة الفيديو (1080,720,480,360,240,144)")
        self.formating.setPlaceholderText("نوع الملف")
        self.formating.setPlaceholderText("الصيغة")
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        #combo boxes

        self.cb.addItem("144p")
        self.cb.addItem("240p")
        self.cb.addItems(["360p", "480p", "720p","1080p"])

        self.formating.addItems(["Video","Audio"])


        self.playlist.clicked.connect(self.defplaylist)



        # FONTS

        self.line.setFont(font)
        self.cb.setFont(font)
        self.cb.setFont(font)
        self.url.setFont(font)
        btn_download.setFont(font)
        btn_info.setFont(font1)
        btn_path.setFont(font)
        self.formating.setFont(font)


        layout.addWidget(self.playlist)
        layout.addWidget(self.url)
        layout.addWidget(self.formating)
        layout.addWidget(self.file_name)
        layout.addWidget(self.cb)
        layout.addWidget(self.progress)
        layout.addWidget(btn_download)
        layout.addWidget(btn_path)
        #layout.addWidget(btn_info)
        layout.addWidget(self.line)
        btn_info.setGeometry(10, 250, 10, 10)

        self.line.setGeometry(10,10,101,10)
        self.formating.currentTextChanged.connect(self.check_formats)
        self.url.textChanged.connect(self.checktext)

        #system settings
        self.setLayout(layout)
        self.setWindowTitle("محمل برامج بواسطة عزام")

        self.setFocus()
        #self.setMaximumSize(500,500)
        self.hight = 300
        self.width = 500
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.hight)
        self.setAutoFillBackground(10)
        self.setWindowIcon(QIcon(os.path.join(current_dir, 'download.ico')))

        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)

        #layouts settings
        btn_download.setFixedWidth(473)
        btn_download.setFixedHeight(45)
        self.url.setFixedWidth(473)
        self.url.setFixedHeight(35)
        self.formating.setFixedWidth(70)
        self.formating.setFixedHeight(30)
        btn_info.unsetLayoutDirection()
        btn_info.setFixedWidth(45)
        btn_info.setFixedHeight(45)
        btn_info.setFocus()
        #hide all this things when start the program

        self.progress.hide()
        self.file_name.hide()
        self.formating.hide()
        self.cb.hide()
        self.cb.setFixedHeight(35)
        btn_download.clicked.connect(self.download)
        btn_path.clicked.connect(self.path)
        btn_info.clicked.connect(self.info)
        btn_path.setFixedHeight(45)
        btn_path.setFixedWidth(100)
    def defplaylist(self):
        self.i += 1

        if self.i % 2 == 0:
            print("Unchecked")
            self.playinglist = False
        if self.i % 2 != 0:
            print("Checked")
            self.playinglist = True




    def check_formats(self):
        if self.formating.currentText() == "Video":
            self.cb.show()
        if self.formating.currentText() == "Audio":
            self.cb.hide()
    def checktext(self,text): #checking function for url if it is from youtube

        if str(text).count("www.youtube") == 1:
            self.cb.hide()
            self.progress.hide()
            self.file_name.hide()
            self.formating.show()
            self.playlist.show()

        elif str(text).count("www.youtube") == 0:
            self.cb.hide()
            self.playlist.hide()
            self.formating.hide()
            self.file_name.show()
            self.progress.show()

    def path(self):
        try:
            self.folder = QFileDialog().getExistingDirectory(self, "اختر المكان الذي تريد الحفظ فيه")
        except Exception as ex:
            QMessageBox.warning(self, "تحذير","يرجى ادخال مسار لحفظ الفيديو اولا")


    def download(self):#دالة التحميل
        #الصيغ مال التحميل
        formats = [".mp4",".jpg",".png",".gif",".pdf",
                   ".tiff",".psd",".raw",".al",".mp3",
                   ".mp4",".mvp",".m4a",".flac",".wav",
                   ".wma",".aac",".mov",".wmv",".flv",
                   ".ppt",".exe",".msi",".lnk",".jar",
                   ".java",".py",".pyc",".txt",".zip",
                   ".rar",".wsd",".docx",".iso",".aep",
                   ".dll",".bat"]
        url = self.url.text()
        res = self.cb.currentText()
        name = self.file_name.text()
        formating = self.formating.currentText()

        format = ".mp4" #الصيغة الافتراضية
        for i in formats:
            if url.count(i) == 1:
                format = i
        save_location = self.folder + "/" + name + format  # مكان الحفظ ل اي شي برا يوتيوب
        if url.count("www.youtube") == 1:
            try:
                v = pytube.YouTube(url)
                try:



                    if formating == "Video":
                        print("MP4")
                        v = pytube.YouTube(url)
                        video = v.streams.get_by_resolution(res)
                        print("gffff")

                        try:

                            video.download(output_path=self.folder+"/Downloads/", filename=video.title)
                            QMessageBox.information(self, "معلومات", "تم تحميل الملف بنجاح")
                            print("THis is test")
                        except Exception as ex:
                            print("dd")
                            QMessageBox.warning(self, "تحذير", "يرجى ادخال مسار لحفظ الفيديو اولا")

                    elif formating == "Audio":

                        print("MP3")
                        v = pytube.YouTube(url)
                        video = v.streams.get_by_itag(251)

                        if self.folder == "" or self.folder == None:
                            QMessageBox.warning(self, "تحذير", "يرجى ادخال مسار لحفظ الفيديو اولا")
                        else:
                            video.download(output_path=self.folder+"/Downloads/", filename=video.title)
                            QMessageBox.information(self, "معلومات", "تم تحميل الملف بنجاح")
                except Exception as ex:
                    video = v.streams.get_highest_resolution()
                    QMessageBox.warning(self, "خطأ", "لاتوجد هذه الدقه في هذا الفيديو لذلك سوف يتم تحميل اعلى دقه")
                    if self.folder != "" or self.folder != None:
                        video.download(output_path=self.folder + "/Downloads/")
                        QMessageBox.information(self, "معلومات", "تم تحميل الملف بنجاح")
                    else:
                        QMessageBox.warning(self, "تحذير", "يرجى ادخال مسار لحفظ الفيديو اولا")

            except Exception as ex:
                QMessageBox.warning(self,"تحذير","عنوان الرابط الذي ادخلته غير صحيح يرجى التحقق منه")


        elif url.count("www.youtube") == 0: # check if the url youtube link or not

            try:
                urllib.request.urlretrieve(url,save_location, self.report)
                QMessageBox.information(self, "معلومات", "مبروك تم تحميل الملف")
            except Exception as ex:
                print(save_location)
                QMessageBox.warning(self, "تحذير", "عنوان الرابط الذي ادخلته غير صحيح يرجى التحقق منه")
        # empting all things
        self.progress.setValue(0)
        self.url.setText("")
        self.folder = ""
        self.cb.setCurrentText("ادخل دقة جديدة")
        self.file_name.setText("")
        self.formating.setCurrentText("اختر الصيغة")

    def info(self):
        QMessageBox.information(self,"معلومات عن البرنامج ","تم انشاء هذا البرنامج بواسطة عزام وهو قيد التطوير\n\n  إصدار البرنامج: 1.3v \n")
    def report(self,blocknum,blocksize,totalsize):
        result = blocknum * blocksize
        if totalsize > 0:
            percent = result * 100 / totalsize
            self.progress.setValue(int(percent))



dialog = Downloader()
dialog.show()
app.exec_()
