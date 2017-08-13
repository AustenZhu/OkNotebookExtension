import os
from shutil import copyfile
from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic, line_cell_magic)

@magics_class
class OkMagics(Magics):
    """Magics related to Okpy"""

    @line_magic
    def okinit(self, arg_s): 
        """Initialize a .ok file

        \\Usage: 
            %init_ok <filename>

            Where filename specifies the name of the ok file
            NOTE: This is an optional argument, and if any .ok file already
            exists, then that file will be loaded instead. 

        Examples: 
            %okinit
        """
        #Unused options
        ___, args = self.parse_options(arg_s, 'yns:r:') 
        
        #Checking if ok already exists
        print(os.getcwd())
        ok_file = [f for f in os.listdir() if '.ok' in f]
        if not ok_file:
            if args: 
                ok_file_name = args if '.ok' in args else args + '.ok'
            else: 
                ok_file_name = 'default.ok'
            true_path = '~/.ipython/extensions/ok_assets/default.ok'
        else: 
            #print('An ok file already exists. That file is being loaded')
            ok_file_name, true_path = ok_file[0], ok_file[0]

        #Loading in the content: 
        contents = self.shell.find_user_code(true_path, search_ns=False)

        contents = "%%writefile {}\n".format(ok_file_name) + contents 

        self.shell.set_next_input(contents, replace=True)


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

        WARNING: This magic method will load any file that you input into 
        the tests folder, so please use it only to load tests 
        ie. Don't put any large files into the test folder and then use 
        this magic method to edit them. 
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
    