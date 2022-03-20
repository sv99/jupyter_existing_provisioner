#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     11.03.2022
# Copyright:   (c) user 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""An example of embedding a RichJupyterWidget in a PyQT Application.
This uses a normal kernel launched as a subprocess. It shows how to shutdown
the kernel cleanly when the application quits.
To run:
    python3 embed_qtconsole.py
"""
import os, sys
#from pyqt import QtWidgets
from PyQt5 import QtWidgets

from jupyter_core.paths import jupyter_runtime_dir

from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.manager import QtKernelManager

# The ID of an installed kernel, e.g. 'bash' or 'ir'.
USE_KERNEL = 'python3'

def _new_connection_file() -> str:
    cf = ""
    while not cf:
        # we don't need a 128b id to distinguish kernels, use more readable
        # 48b node segment (12 hex chars).  Users running more than 32k simultaneous
        # kernels can subclass.
        cf = os.path.join(jupyter_runtime_dir(), "kernel-%s.json" % os.getpid())
        # only keep if it's actually new.  Protect against unlikely collision
        # in 48b random search space
        cf = cf if not os.path.exists(cf) else ""
    return cf


def make_jupyter_widget_with_kernel():
    """Start a kernel, connect to it, and create a RichJupyterWidget to use it
    """
    kernel_manager = QtKernelManager(
        kernel_name=USE_KERNEL,
        connection_file=_new_connection_file())
    kernel_manager.start_kernel()

    print(kernel_manager.connection_file)
    kernel_client = kernel_manager.client()
    kernel_client.start_channels()

    jupyter_widget = RichJupyterWidget()
    jupyter_widget.kernel_manager = kernel_manager
    jupyter_widget.kernel_client = kernel_client
    return jupyter_widget


class MainWindow(QtWidgets.QMainWindow):
    """A window that contains a single Qt console."""
    def __init__(self):
        super().__init__()
        self.jupyter_widget = make_jupyter_widget_with_kernel()
        self.setCentralWidget(self.jupyter_widget)

    def shutdown_kernel(self):
        print('Shutting down kernel...')
        self.jupyter_widget.kernel_client.stop_channels()
        self.jupyter_widget.kernel_manager.shutdown_kernel()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.aboutToQuit.connect(window.shutdown_kernel)
    sys.exit(app.exec_())