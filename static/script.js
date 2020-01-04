
$(document).ready(function(){
   $('#contact_form').bootstrapValidator({
       live:"submitted",
    fields:{
    firstname: {
            validators: {
                    stringLength: {
                    min: 2,
                },
                    notEmpty: {
                    message: 'Please enter your First Name'
                }
            }
        },
         lastname: {
            validators: {
                 stringLength: {
                    min: 2,
                },
                notEmpty: {
                    message: 'Please enter your Last Name'
                }
            }
        },
    
    }});
});



