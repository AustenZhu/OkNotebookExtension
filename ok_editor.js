define(['require', 'jquery', 'base/js/namespace'], function (require, $, IPython) {
    "use strict"; 
    var create_ok_buttons = function() {
        //finding the location of all grading cells
        var notebook = $("#notebook");
        var counter = 0; 
        
        $(notebook).find(".cell").map(function(i, cell) {
            if(cell.className.includes("code_cell")) {
                $(cell).find(".cm-property").map(function(i, prop) {
                    if (prop.innerText === 'grade') {
                        //Idea for buttons - add an attribute that stores the IPython cell
                        //WILL WORK WOOOHOOOO!
                        if ($(cell).find(".ok-btn").length === 0){
                            var button = $('<button/>');
                            button.cell = IPython.notebook.get_cell(counter);
                            button.addClass("ok-btn")
                            //button.css({'height':'25px', 'width':'25px', 'padding': '0'});
                            //button.text('OK'); 
                            button.click(function() {
                                var location = IPython.notebook.find_cell_index(button.cell);
                                IPython.notebook.insert_cell_below('code', location);
                                var newcell = IPython.notebook.get_cell(location+1); 
                                var testspan = $(cell).find('.cm-string')[0].innerText.replace('.py', '');
                                newcell.set_text('%ok ' + testspan);
                            });
                            button.append($('<img/>').attr({
                                src: 'ok_assets/ok.svg',
                                title: 'OKPIC'
                            }));

                            $(cell).append(button);
                        }
                    }
                })
            }
            counter += 1
        }); 
    };

    var ok = function() {
        create_ok_buttons(); 
    };
    
    var import_css = function() {
        var link = document.createElement('link');
        link.type = 'text/css'; 
        link.rel = 'stylesheet'; 
        link.href = require.toUrl('./ok.css');
        document.getElementsByTagName("head")[0].appendChild(link);
    };


    var toggle_ok = function() {
        
    };

    var ok_toolbar_button = function(){
        if (!IPython.toolbar) {
            $([IPython.events]).on('app_initialized.NotebookApp', ok_toolbar_button); 
            return; 
        }
        if ($('ok_button').length === 0) {
            IPython.toolbar.add_buttons_group([
                {
                    'label' : 'Okpy', 
                    'icon'  : 'fa-check-circle',
                    'callback'  : toggle_ok, 
                    'id'    : 'ok_button'
                },
            ]);
        }
    };
})
