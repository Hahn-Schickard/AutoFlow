"""This is a splittet method from the Mainwindow class which contain the logic for the AutoMLData window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""

from src.GUILayout.AutoMLData import *
def AutoMLData(self):
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
        
        self.Window1d = UIMarcusWindow4(self.FONT_STYLE, self)
        
        if self.output_path_ml != None:
            self.Window1d.Output_Pfad.setText(self.output_path_ml)
        
        if self.project_name != None:
            self.Window1d.Projekt_Name.setText(self.project_name)

        if self.data_loader_path_ml != None:
            self.Window1d.Daten_Pfad.setText(self.data_loader_path_ml)
        
        self.Window1d.Output_Pfad_Browse.clicked.connect(lambda:self.get_output_path_ml(self.Window1d))
        self.Window1d.Daten_einlesen_Browse.clicked.connect(lambda:self.get_data_loader_path_ml(self.Window1d))
        self.Window1d.Next.clicked.connect(lambda:self.TaskWindow("Next"))
        self.Window1d.Back.clicked.connect(self.GUIStart)
        
        self.setCentralWidget(self.Window1d)
        self.show()