"""This is a splittet method from the Mainwindow class which contain the logic for the AutoMLData window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""


from src.GUILayout.UIHelperWindow import *
        
def HelperWindow(self):
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
    self.setFixedWidth(800)
    self.setFixedHeight(900)
    self.Window3a = UIHelperWindow(self.FONT_STYLE, self)
    
    
    
    self.Window3a.Forms.clicked.connect(self.Form_clicked)
    self.Window3a.Formm.clicked.connect(self.Form_clicked)
    self.Window3a.Forml.clicked.connect(self.Form_clicked)
    self.Window3a.Energies.clicked.connect(self.Form_clicked)
    self.Window3a.Energiem.clicked.connect(self.Form_clicked)
    self.Window3a.Energiel.clicked.connect(self.Form_clicked)
    self.Window3a.Flexs.clicked.connect(self.Form_clicked)
    self.Window3a.Flexm.clicked.connect(self.Form_clicked)
    self.Window3a.Flexl.clicked.connect(self.Form_clicked)
    self.Window3a.Preiss.clicked.connect(self.Form_clicked)
    self.Window3a.Preism.clicked.connect(self.Form_clicked)
    self.Window3a.Preisl.clicked.connect(self.Form_clicked)
    self.Window3a.Parameter.textChanged.connect(self.Form_clicked)
    self.Window3a.FPS.textChanged.connect(self.Form_clicked)
    
    
    self.Window3a.Back.clicked.connect(lambda:self.TargetWindow("Back", self.Window3a))
    self.Window3a.Next.clicked.connect(lambda:self.OptiWindow("Next","?"))
    
    self.setCentralWidget(self.Window3a)
    
    self.Dot = QLabel(self)
    Dotimg = QPixmap(os.path.join('src','GUILayout','Images', 'Dot.png'))
    self.Dot.setFixedSize(30, 30)
    self.Dot.setScaledContents(True)
    self.Dot.setPixmap(Dotimg)
    self.Dot.setVisible(False)
    
    
    self.show()