from gui import *
from PyQt6.QtWidgets import *
from voter import Voter
import csv
import os

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        initialize the main window
        """
        super().__init__()
        self.setupUi(self)

        #wipes radioButton selections, unchecks opt_in box, and clears voter_id
        self.hide_fields()

        # vote button driving the interaction
        self.pushButton_vote.clicked.connect(lambda: self.submit())

    def hide_fields(self) -> None:
        """
        clears the 3 radio buttons, unchecks opt_in box, and clears voter_id
        """
        self.radioButton_independent.setChecked(False)
        self.radioButton_republican.setChecked(False)
        self.radioButton_democrat.setChecked(False)
        self.checkBox_opt_in.setChecked(False)
        self.lineEdit_voter_id.setText('')

    def check_voter_id(self) -> bool:
        """
        checks if the voter id is unique in the csv 'voter_id.csv'.
        creates the csv file if it doesn't exist.
        :return: returns true for a unique voter id and False otherwise.
        """
        #checks for the int of voter_id in the csv
        try:
            voter_id = int(self.lineEdit_voter_id.text())
            if len(self.lineEdit_voter_id.text()) == 0:
                QMessageBox.warning(self, "Input Error", "Please enter your numerical voter ID.")
                return False

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter your numerical voter ID.")
            return False


        # creates file if it doesn't exist
        while not os.path.isfile('voter_id.csv'):
            with open('voter_id.csv', 'a', newline='') as csvfile:
                content = csv.writer(csvfile)
                content.writerow(['Voter ID', 'Candidate', 'opt-in'])
                break

        # checks the csv file for the voter_id
        with open('voter_id.csv', 'r', newline='') as csvfile:
            entries = csv.reader(csvfile)
            for row in entries:
                if row[0] == str(voter_id):
                    QMessageBox.warning(self, "Input Error", "Your voter id is already in use.")
                    return False

        #return True if the id is unique
        return True


    def get_candidate(self) -> str | None:
        """
        returns the candidate as a string or exits when voter_id is empty
        :return: returns the candidate choice as a string or None is empty
        """

        if self.radioButton_independent.isChecked():
            return 'Independent'
        if self.radioButton_democrat.isChecked():
            return 'Democrat'
        if self.radioButton_republican.isChecked():
            return 'Republican'

        QMessageBox.warning(self, "Input Error", "Please select a candidate")
        return None

    def check_opt_in(self) -> str:
        """
        retrieves the opt_in choice from the box

        :return: 'Yes' if box is checked, 'No' if unchecked.
        """
        if self.checkBox_opt_in.isChecked():
            return 'Yes'
        else:
            return 'No'

    def submit(self) -> None:
        """
        submits the voter's id, candidate, and opt-in choice
        """
        #validates and creates voter_id
        if self.check_voter_id() == True:
            voter_id = self.lineEdit_voter_id.text().strip()
        else:
            return

        #retrieves candidate choice
        candidate = self.get_candidate()
        if self.get_candidate() == None:
            return



        #retrieves the opt-in choice
        opt_in = self.check_opt_in()

        #creates Voter instance
        self.current_voter = Voter(voter_id, candidate, opt_in)

        #submits the current voter info to the csv
        with open('voter_id.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile)
            id = self.current_voter.get_voter_id()
            candidate = self.current_voter.get_party()
            opt_in = self.current_voter.get_opt_in()
            content.writerow([id, candidate, opt_in])








