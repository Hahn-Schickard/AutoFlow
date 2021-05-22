"""This is a splittet method from the Mainwindow class which contain the logic for the AutoMLData window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""

from src.GUILayout.UIConstraintsWindow import *
        
def ConstraintsWindow(self, n, target):
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
      table_handle:
        An open smalltable.Table instance.
      keys:
        A sequence of strings representing the key of each table row to
        fetch.  String keys will be UTF-8 encoded.
      require_all_keys:
        Optional; If require_all_keys is True only rows with values set
        for all keys will be returned.

    Returns:
      A dict mapping keys to the corresponding table row data
      fetched. Each row is represented as a tuple of strings. For
      example:

      {b'Serak': ('Rigel VII', 'Preparer'),
       b'Zim': ('Irk', 'Invader'),
       b'Lrrr': ('Omicron Persei 8', 'Emperor')}

      Returned keys are always bytes.  If a key from the keys argument is
      missing from the dictionary, then that row was not found in the
      table (and require_all_keys must have been False).

    Raises:
      IOError: An error occurred accessing the smalltable.
    """
    
    if n == "Next":
        self.target = target
        print(self.target)
        
        if self.target == "?":
            self.Dot.setVisible(False)
        if self.target == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
             
            msg.setText("Please choose a task")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            
            return

    self.Window3 = UIConstraintsWindow(self.FONT_STYLE, self)
    
    if "Params" in self.constraints:
        self.Window3.Params.setChecked(True)
        self.set_params()
        self.Window3.Params_factor.setText(str(self.params_factor))
    if "Floats" in self.constraints:
        self.Window3.Floats.setChecked(True)
        self.set_floats()
        self.Window3.Floats_factor.setText(str(self.floats_factor))
    if "Complex" in self.constraints:
        self.Window3.Complex.setChecked(True)
        self.set_complex()
        self.Window3.Complex_factor.setText(str(self.complex_factor)) 
        
    self.Window3.Params.toggled.connect(self.set_params)
    self.Window3.Floats.toggled.connect(self.set_floats)
    self.Window3.Complex.toggled.connect(self.set_complex)

    
    self.Window3.Back.clicked.connect(lambda:self.TaskWindow("Back"))
    self.Window3.Next.clicked.connect(lambda:self.SettingsWindow("Next"))
    
    self.setCentralWidget(self.Window3)
    self.show()