define(['require', 'jquery', 'base/js/namespace'], function (require, $, IPython) {
    "use strict"; 

    var create_ok_buttons = function() {
        //finding the location of all grading cells
        var notebook = $("#notebook");
        var counter = 0; 
        //Refactor this code to search within all cells, incrementing counter
        //  And then adding button if conditions met 



        notebook.find(".cell").map(function(i, cell) {
            if(cell.className.includes("code_cell")) {
                $(cell).find(".cm-property").map(function(i, prop) {
                    if (prop.innerText === 'grade') {
                        //Idea for buttons - add an attribute that stores the IPython cell
                        //WILL WORK WOOOHOOOO!

                        /*
                        var button = $('<div/>')
                        button.cell = IPython.notebook.get_cell(counter);
                        button.text('OK'); 
                        button.click(function() {
                            var location = IPython.notebook.find_cell_index(button.cell);
                            IPython.notebook.insert_cell_below('code', location);
                            var newcell = IPython.notebook.get_cell(location+1); 
                            var testspan = //get correct info;
                            cell1.set_text(testspan);
                        })
                        */
                        

                        IPython.Notebook.insert_cell_below('code', counter);
                        var newcell = IPython.notebook.get_cell(counter+1); 
                        var testspan = cell.find("span:contains('q*.py')")[0].innerText;
                        cell1.set_text('%ok q');
                    }
                })
            }
            counter += 1
        });

        var cells = IPython.notebook.get_cells(); 


        notebook.find('.code_cell').map(function(i, cell) { 
            cell.find('.cm-property').map(function(i, prop) {
                if(prop.innerText === 'grade') {
                    //Add id to div in order to set css properly
                    var id = 'prop' + counter.toString(); 
                    prop.attr('id', id);
                    //Add button div adjacent to grading cell
                    notebook.append(
                        $('<div/>')
                        .addClass('ok-btn')
                        .text('OK')
                        .click(function() {
                            //Inserts new cell below and prepopulate with magic %ok method
                            IPython.notebook.insert_cell_below('code',0);
                        })
                    )
                }
            });
        });
    };

    var ok = function() {

    };


    var toggle_ok = function() {
        $("#ok-wrapper").toggle();
        //recreating buttons: 
        ok();
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
