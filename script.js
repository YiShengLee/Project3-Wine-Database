$('#submit').submit(function (e){
   e.preventDefault(); 
   ('#contact_form').bootstrapValidator({
    first_name: {
            validators: {
                    stringLength: {
                    min: 2,
                },
                    notEmpty: {
                    message: 'Please enter your First Name'
                }
            }
        },
         last_name: {
            validators: {
                 stringLength: {
                    min: 2,
                },
                notEmpty: {
                    message: 'Please enter your Last Name'
                }
            }
        },
    
    });
});



