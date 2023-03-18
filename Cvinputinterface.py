import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("TalentMap")
        
        #set layout
        
        self.setLayout(qtw.QVBoxLayout())
        
        #create a label
        my_label = qtw.QLabel("Enter Your Information")
        self.layout().addWidget(my_label)
        
        #changing fontsize
        
        my_label.setFont(qtg.QFont('Helvetica', 18))
        
        #creating a box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("Name Field")
        my_entry.setText("Enter name")
        self.layout().addWidget(my_entry)
        

        
        #creating a combobox
        my_combo= qtw.QComboBox(self, editable= True, insertPolicy=qtw.QComboBox.InsertAtTop)
        #my_combo.addItem("Designation")  #alternate method to add combos are down below as a list and using additems
        
        
        # my_combo.addItems(["<Default designation>","Teacher","BBA peep"])
        
        
        # if my_combo.addItem("Teacher")==True:
            
        #     my_combo.addItems(["<Default designation>","Assistant", "General Assistant", "Headmaster"])
            
        #     self.layout().addWidget(my_combo)
            
        # elif my_combo.addItem("BBA peep")== True:
            
        #     my_combo.addItems(["<Default designation>","General Secretary", "Sectretary", "CEO"])
            
        #     self.layout().addWidget(my_combo)
        
        my_combo.addItems(["<Default designation>","Teacher", "Doctor", "Plumber"])
        
        
        self.layout().addWidget(my_combo)
        
        
        #creating a button
        my_button = qtw.QPushButton("Click to check",
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        #show the app
        self.show()
        
        def press_it():
            #add name to the label
            my_label.setText(f'Hello {my_combo.currentText()}')
            my_entry.setText(f'You clicked {my_combo.currentText()}')
            
        #creating a spinbox
        
        my_spin
    
app=qtw.QApplication([])
mw=MainWindow()
        
 
app.exec_()