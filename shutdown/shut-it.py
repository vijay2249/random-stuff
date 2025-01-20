import os
import sys
import time
import shutil
import platform
import threading
import subprocess
import PyQt5

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class Window(QMainWindow):
    def __init__(self, countDown):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 300, 200)
        self._countDownClass = countDown
        self.setWindowTitle("System shutdown countdown")
        self.home()
    
    def home(self):
        self.label = QLabel(self)
        self.label.setText(f"System will be shutdown in {self._countDownClass} seconds")
        self.label.adjustSize()
        self.label.move(150, 100)
        threading.Thread(target=self.showCountdown, daemon=True).start()
        self.show()
    
    def showCountdown(self):
        self.text = f"System will be shutdown in {self._countDownClass} seconds"
        while self._countDownClass > 0:
            self.label.setText(self.text)
            self._countDownClass -= 1
            time.sleep(0.99)
        return 1


class SleepWell:
    __slots__ = "_waitingTime", "_countDown"
    def __init__(self, waitingTime=300):
        self._waitingTime = waitingTime
        self._countDown = None
    
    def checkTime(self):
        localTime = time.localtime()
        hour = localTime.tm_hour
        return (hour>=23 or 0<=hour<=6)
    
    def warnUser(self):
        app = QApplication(sys.argv)
        GUI = Window(self._waitingTime)
        print(GUI.showCountdown)
        self._chooseOption()
    
    def _chooseOption(self, selectedOption):
        options = {
            1: self.shutDown(),
            2: self.forceShutdown(),
            3: self._hibernate(),
            4: self.__saveWorkBeforeShutdown(),
            5: self.help(),
            6: self.restart()
        }
        options[selectedOption]
    
    def restart(self):
        os.system('shutdown /r /f')

    def _hibernate(self):
        os.system("shutdown /h /f")

    def shutDown(self):
        os.system("shutdown /s")

    def forceShutdown(self):
        os.system("shutdown /p /f")

    def __saveWorkBeforeShutdown(self):
        pass

    def __restartControl(self):
        if platform.system() == "Windows":
            pass
            # self._registrySetUp()

    def _registrySetUp(self):
        sleepWell = os.environ['appdata'] + '\\Sleep_Well_Beta.exe'
        if not os.path.exists(sleepWell):
            shutil.copy(sys.executable, sleepWell)
            subprocess.call(
                f'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "{sleepWell}"',
                shell=True
            )
        pass
    
    def help(self):
        pass


if __name__ == '__main__':
    sleepWell = SleepWell()
    doShutdown = sleepWell.checkTime()
    if doShutdown:
        app = QApplication(sys.argv)
        GUI = Window(sleepWell._countDown)
        option = GUI.showCountdown()
        time.sleep(5)
        sleepWell._chooseOption(option)
        sys.exit(app.exec_())