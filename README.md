Ok Editor
===============

NOTE: MAKE SURE that you install the ok_magic first!

Frontend extension for editing oktests using the %ok cell magic.

To automatically install both the magic and the nbextension, copy install.sh and then run 
```bash
sudo bash install.sh
```

To manually install: 
```bash
jupyter nbextension install --user https://rawgit.com/AustenZhu/OkNotebookExtension/master/ok_editor.js
curl -L https://rawgit.com/AustenZhu/OkNotebookExtension/master/ok.css > $(jupyter --data-dir)/nbextensions/ok.css
```
And then follow the README in the ok_magic folder to install the magic. 