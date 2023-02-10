import os
import sys
import csv
from datetime import datetime, timedelta

# Related third party imports

# Local application/library specific imports
from mainWindow import *

ROOT_DIR = os.getcwd()
path = f"{ROOT_DIR}\\timer_results.csv"


class MyForm(QWidget):  # Main Window
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.start_time = 0
        self.stop_time = 0
        self.delta_t = 0
        self.elapsed_time = 0

        self.data_dict = {
            "client_name": "",
            "work_description": "",
            "hardware_used": "",
            "ticket_number": ""
        }

        self.ui.btn_stop.setEnabled(False)

        # Signals
        self.ui.btn_start.clicked.connect(self.assign_and_check_data)
        self.ui.btn_stop.clicked.connect(self.write_to_file)
    
    # Slots
    def assign_and_check_data(self):
        self.data_dict["client_name"] = self.ui.txt_client.text()
        self.data_dict["work_description"] = self.ui.txt_description.text()
        self.data_dict["hardware_used"] = self.ui.txt_hardware.text()
        self.data_dict["ticket_number"] = self.ui.txt_ticketNo.text()

        if all(value != "" for value in self.data_dict.values()):
            self.ui.btn_start.setEnabled(False)
            self.ui.btn_stop.setEnabled(True)
            self.ui.txt_startTime.clear()
            self.ui.txt_endTime.clear()
            self.ui.txt_duration.clear()
            self.start_time = datetime.now()
            self.ui.txt_startTime.setText(f"{self.start_time.strftime('%H')}:{self.start_time.strftime('%M')}:"
                                          f"{self.start_time.strftime('%S')}")
        else:
            print(f"Enter data for client, description, hardware, and ticket no.")

    def write_to_file(self):
        self.ui.btn_start.setEnabled(True)
        self.ui.btn_stop.setEnabled(False)
        self.stop_time = datetime.now()
        self.ui.txt_endTime.setText(f"{self.stop_time.strftime('%H')}:{self.stop_time.strftime('%M')}:"
                                    f"{self.stop_time.strftime('%S')}")
        self.delta_t = round((self.stop_time - self.start_time).total_seconds())
        self.elapsed_time = str(timedelta(seconds=self.delta_t))
        self.ui.txt_duration.setText(str(self.elapsed_time))

        # assign header columns
        header_list = ['Client', 'Description', 'Hardware', 'Ticket No.', 'Start time', 'End Time', 'Duration']

        if os.path.isfile(path):
            with open('timer_results.csv', 'a', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    [self.data_dict["client_name"], self.data_dict["work_description"], self.data_dict["hardware_used"],
                     self.data_dict["ticket_number"], self.start_time.strftime("%H:%M:%S"),
                     self.stop_time.strftime("%H:%M:%S"), self.elapsed_time])
        else:
            with open('timer_results.csv', 'a', newline='') as file:
                hw = csv.DictWriter(file, delimiter=';', fieldnames=header_list)
                hw.writeheader()
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    [self.data_dict["client_name"], self.data_dict["work_description"], self.data_dict["hardware_used"],
                     self.data_dict["ticket_number"], self.start_time.strftime("%H:%M:%S"),
                     self.stop_time.strftime("%H:%M:%S"), self.elapsed_time])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # 'Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion'
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
