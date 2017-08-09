A Jupyter Notebook extension that allows you to write okpy tests in cell. 

To use and install the extension, run the following lines in your terminal

```bash
mv ok_assets ok_editor.py ~/.ipython/extensions/
```

To load the extension into a notebook, run the following in a cell: 

```bash
%load_ext ok_editor
```

To use the extension, run a line magic: 
```python
%ok name_of_ok_test
```

Make sure to only specify the name - the extension will use the tests directory (if it exists, or create it if it does not) to find your specified name. 

If a test does not exist, the ok_editor automatically populates the test with a template for a test.

In order to save a test, simply run the cell. 

To be finished: 
You can use -t <source> to specify a source for the template.