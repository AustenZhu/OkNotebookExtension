define(['require', 'jquery', 'base/js/namespace'], function (require, $, IPython) {
    "use strict"; 
    
    var make_link = function (h) {

    }

    var create_ok_buttons = function() {
        //finding the location of all grading cells
        $('#notebook').find('.cm-property').map(function(i,prop) {
            if(prop.innerText === 'grade') {
                //Adding button div here, adjacent to grading cell
            };
        });
    }

    var ok = function() {

    }

    var toggle_ok = function() {
        $("#ok-wrapper").toggle();
        //recreating buttons: 
        ok();
    };

    var ok_button = function() {
        
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
