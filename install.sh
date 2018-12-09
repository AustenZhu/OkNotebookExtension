git clone https://github.com/AustenZhu/OkNotebookExtension ~/OkNotebookExtension
mv OkNotebookExtension/ok_magic/ok_editor.py OkNotebookExtension/ok_magic/ok_assets ~/.ipython/extensions/
jupyter nbextension install --user https://cdn.jsdelivr.net/gh/AustenZhu/OkNotebookExtension@master/ok_editor.js
curl -L https://cdn.jsdelivr.net/gh/AustenZhu/OkNotebookExtension@master/ok.css > $(jupyter --data-dir)/nbextensions/ok.css
#rm -rf OkNotebookExtension