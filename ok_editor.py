from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic, line_cell_magic)
import os
import sys
from subprocess import call 

@magics_class
class OkMagics(Magics):
    """Magics related to Okpy"""

    @line_magic
    def init_ok(self, arg_s): 
        """Initialize a .ok file

        \\Usage: 
            %init_ok [endpoint]

            Where endpoint specifies the okpy endpoint for the notebook
            NOTE: This is an optional argument, 

        The %init_ok magic will NOT override an existing ok file, so if 
            you want to edit an existing file, simply use: 
                %load name_of_ok_file

        Examples: 
            %ok cal/data8/sp17/lab07
            %ok cal/data8r/su17/lab08
        """
        opts, args = self.parse_options(arg_s, 'yns:r:') 
        
        if not args: 
            notebook_name = os.path.realpath(__file__).replace('.ipynb', '')
            call('ok_assets/init.sh ' + notebook_name, shell=True)

    @line_magic
    def ok(self, arg_s):
        """Load ok test into the current frontend.

        \\Usage:
            %ok [options] ok_test

            where ok_test is the name of the ok_test, NOT the relative path of the file containing the ok_test. 
            If no file is found, automatically creates a file with a default template.

        Options:
            -n : Include user's namespace when searching for source code.
            TODO: Finish -t method
            -t <source>: Specify what template that you want to use. source should be a relative path from the notebook.

        Examples: 
            %ok q1 
            %ok q2
        """
        opts, args = self.parse_options(arg_s, 'yns:r:') 

        if not args: 
            raise ValueError('Missing ok_test name') 
        
        #Run bash script to initialize tests folder 
        if not os.path.exists('tests'):
            try: 
                os.makedirs('tests')
            except OSError as error: 
                raise OSError(error)
            
        search_ns = 'n' in opts #TO-DO: make sure that template choice works
        
        if 't' in opts: 
            template_path = opts['t']
            if not os.path.exists(template_path): 
                print("File Doesn't Exist - Reverting to default template")
                template_path = '~/.ipython/extensions/ok_assets/template.py'
        else: 
            template_path = '~/.ipython/extensions/ok_assets/template.py'

        #Creating relative path to tests: 
        if 'py' not in args: 
            args = args + '.py'
        args = 'tests/' + args 

        try: 
            contents = self.shell.find_user_code(args, search_ns=search_ns)
        except (NameError, ValueError) as error:
            print(error)
            contents = self.shell.find_user_code(template_path, search_ns=False)
        
        contents = "%%writefile {}\n".format(args) + contents 

        self.shell.set_next_input(contents, replace=True)
        
def load_ipython_extension(ipython):
    ipython.register_magics(OkMagics)