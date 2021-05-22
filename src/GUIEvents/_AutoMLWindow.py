"""This is a splittet method from the Mainwindow class which contain the logic for the AutoMLData window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
from src.GUILayout.UIAutoMLWindow import *

   
def AutoMLWindow(self, n):         
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
        self.max_epoch = self.Window4.epochs_factor.text()
        self.max_trials = self.Window4.max_trials_factor.text()
        self.max_size = self.Window4.max_size_factor.text()

    
    self.Window5 = UIAutoMLWindow(self.FONT_STYLE, self)
      
    self.Window5.Back.clicked.connect(lambda:self.SettingsWindow("Back"))
    self.Window5.Start.clicked.connect(lambda:self.ReturnWindow("Next"))
   
    self.Window5.Finish.clicked.connect(self.close)

    
    self.setCentralWidget(self.Window5)
    self.show()