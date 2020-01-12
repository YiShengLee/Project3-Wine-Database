// Add wine validatation section
$(document).ready(function(){
   $('#contact_form').bootstrapValidator({
       live:"submitted",
    fields:{
    firstname: {
            validators: {
                    stringLength: {
                        min: 2,
                        max: 30,
                        message: 'Firstname must be more than 2 and less than 30 characters long'
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
                        max: 30,
                        message: 'Lastname must be more than 2 and less than 30 characters long'
                    },
                    notEmpty: {
                        message: 'Please enter your Last Name'
                    }
            }
    },
    price: {
            validators: {
                    integar: {
                        message: 'The value is not an integar'
                    },
                    notEmpty: {
                        message: 'Please enter the cost of the wine'
                    }
            }
    },    
    
    }});
});


// Count down for number of wine data
$('.counter').each(function() {
  var $this = $(this),
      countTo = $this.attr('data-count');
  
  $({ countNum: $this.text()}).animate({
    countNum: countTo
  },

  {

    duration: 1200,
    easing:'linear',
    step: function() {
      $this.text(Math.floor(this.countNum));
    },
    complete: function() {
      $this.text(this.countNum);
      //alert('finished');
    }

  });  
  
  

});



