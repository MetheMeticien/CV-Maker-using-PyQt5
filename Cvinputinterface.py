import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("TalentMap")
        
        #set layout
        
        #self.setLayout(qtw.QVBoxLayout())
        

        
        
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)
        
        #Add stuffs/widgets
        label_1 = qtw.QLabel("This is a Cool Label Row")
        label_1.setFont(qtg.QFont("Helvetica", 24))
        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)
        
        #adding rows
        form_layout.addRow(label_1)
        form_layout.addRow("First Name", f_name)
        form_layout.addRow("First Name", l_name)
        form_layout.addRow(qtw.QPushButton("press me", clicked = lambda: press_it()))
        
        #create a label
        my_label = qtw.QLabel("Enter Your Information")
        self.layout().addWidget(my_label)
        
        
        
        
        #changing fontsize
        
        my_label.setFont(qtg.QFont('Helvetica', 18))
        
        # #creating a box
        # my_entry = qtw.QLineEdit()
        # my_entry.setObjectName("Name Field")
        # my_entry.setText("Enter name")
        # self.layout().addWidget(my_entry)
        

        
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
        
        #creating a spinbox
        
        my_spin=qtw.QSpinBox(self, value=10, maximum=100, minimum=0, singleStep=5, prefix=("You are inteded to work her for "), suffix=(" years" ))
        #QDoubleSpinbox for doubles
        my_spin.setFont(qtg.QFont('Helvetica', 18))
        
        self.layout().addWidget(my_spin)
        
        
        #creating a Text box
        my_text = qtw.QTextEdit(self,
			plainText="Work Experience",
			#html = "<center><h1><em>Big Header Text!</em></h1></center>",
			acceptRichText= False,
			lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
			lineWrapColumnOrWidth=75,
			placeholderText="Enter your job description",
			readOnly=False,
			)
        self.layout().addWidget(my_text)
        
        
        
        #show the app
        self.show()
        
        def press_it():
            #add name to the label
            my_label.setText(f'Hello sweet {my_spin.value()}')
            #my_entry.setText(f'You clicked {my_spin.value()}!')
            my_text.setPlainText(f'You wrote {my_text.toPlainText()}!')
            label_1.setText(f'You clicked the button, {f_name}!')
            

    
app=qtw.QApplication([])
mw=MainWindow()
        
 
app.exec_()