from toga.interface.window import Window as WindowInterface
from .container import Container
from . import dialogs


class Window(WindowInterface):
    _CONTAINER_CLASS = Container
    _DIALOG_MODULE = dialogs

    def __init__(self, title=None, position=(100, 100), size=(640, 480), toolbar=None, resizeable=True, closeable=True, minimizable=True):
        super().__init__(title=None, position=(100, 100), size=(640, 480), toolbar=None, resizeable=True, closeable=False, minimizable=False)
        self._create()

    def create(self):
        pass


    def _set_content(self, widget):
        self._impl.setContentView_(self._container._impl)

    def show(self):
        # Do the first layout render.
        self.content._update_layout(
            # width=self._screen.bounds.size.width,
            # height=self._screen.bounds.size.height
        )
        pass

    def _set_title(self, title):
        print("WINDOW TITLE", title)
