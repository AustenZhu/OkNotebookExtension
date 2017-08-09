from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic, line_cell_magic)
import os
import subprocess

@magics_class
class OkMagics(Magics):
    """Magics related to Okpy"""
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
        """
        opts, args = self.parse_options(arg_s, 'yns:r:') 

        if not args: 
            raise ValueError('Missing ok_test name') 

        #Creating relative path to tests: 
        args = 'tests/' + args 
        
        if not os.path.exists('tests'):
            subprocess.call('ok_assets/default.sh')

            
        search_ns = 'n' in opts #TO-DO: make sure that template choice works
        if 't' in opts: 
            template_path = opts['t']
            if not os.path.exists(template_path): 
                print("File Doesn't Exist - Reverting to default template")
                template_path = '~/.ipython/extensions/ok_assets/template.py'
        else: 
            template_path = '~/.ipython/extensions/ok_assets/template.py'

        try: 
            contents = self.shell.find_user_code(args, search_ns=search_ns)
        except NameError as error:
            print(error) 
            contents = self.shell.find_user_code(template_path, search_ns=False)
        except ValueError as error:
            print(error) 
            contents = self.shell.find_user_code(template_path, search_ns=False)

        contents = "%%writefile {}\n".format(args) + contents 

        self.shell.set_next_input(contents, replace=True)
        
def load_ipython_extension(ipython): 
    ipython.register_magics(OkMagics)