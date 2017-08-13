define(['require', 'jquery', 'base/js/namespace'], function (require, $, IPython) {
    "use strict"; 
    
    var make_link = function (h) {

    }



    var create_ok_buttons = function() {

    }

    var ok = function() {

    }

    var toggle_ok = function() {
        $("#ok-wrapper").toggle();
        //recreating buttons: 
        ok();
    };

    var ok_button = function(){
        if (!IPython.toolbar) {
            $([IPython.events]).on('app_initialized.NotebookApp', ok_button); 
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
