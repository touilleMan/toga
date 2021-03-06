identifier = id


class App(object):
    '''The App is the top level of any GUI program. It is the manager of all
    the other bits of the GUI app: the main window and events that window
    generates like user input.

    When you create an App you need to provide it a name, an id for uniqueness
    (by convention, the identifier is a "reversed domain name".) and an
    optional startup function which should run once the App has initialised.
    The startup function typically constructs some initial user interface.

    Once the app is created you should invoke the main_loop() method, which
    will hand over execution of your program to Toga to make the App interface
    do its thing.

    Here is the absolute minimum App::

        app = toga.App('Empty App', 'org.pybee.empty')
        app.main_loop()
    '''
    _MAIN_WINDOW_CLASS = None
    app = None

    def __init__(self, name, app_id, icon=None, id=None, startup=None, document_types=None):
        App.app = self

        if self._MAIN_WINDOW_CLASS is None:
            raise NotImplementedError('App class must define _MAIN_WINDOW_CLASS')

        self.name = name
        self._app_id = app_id
        self._id = id if id else identifier(self)

        self.icon = icon

        self.document_types = document_types
        self._documents = []

        self._startup_method = startup

    @property
    def app_id(self):
        '''The identifier for the app.

        This is the reversed domain name, often used for targetting resources, etc.
        '''
        return self._id

    @property
    def id(self):
        '''The DOM identifier for the app.

        This id can be used to target CSS directives
        '''
        return self._id

    @property
    def documents(self):
        '''Return the list of documents associated with this app.'''
        return self._documents

    def add_document(self, doc):
        '''Add a new document to this app.'''
        doc.app = self
        self._documents.append(doc)

    def open_document(self, fileURL):
        '''Add a new document to this app.'''
        raise NotImplementedError('Application class must define open_document()')

    def startup(self):
        '''Create and show the main window for the application'''
        self.main_window = self._MAIN_WINDOW_CLASS(self.name)
        self.main_window.app = self

        if self._startup_method:
            self.main_window.content = self._startup_method(self)

        self.main_window.show()

    def main_loop(self):
        '''Invoke the application to handle user input.

        This method typically only returns once the application is exiting.
        '''
        raise NotImplementedError('Application class must define main_loop()')
