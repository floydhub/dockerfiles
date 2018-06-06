# Configuration file for ipython.

#------------------------------------------------------------------------------
# InteractiveShellApp(Configurable) configuration
#------------------------------------------------------------------------------

## lines of code to run at IPython startup.
c.InteractiveShellApp.exec_lines = ['%load_ext autoreload', '%autoreload 2']

## A list of dotted module names of IPython extensions to load.
c.InteractiveShellApp.extensions = ['autoreload']
