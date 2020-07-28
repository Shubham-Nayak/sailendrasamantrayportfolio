jQuery(document).on('submit', '#ajax-save-form', function(e){

    e.preventDefault();
    var ajax_save_form = jQuery(this);
    var formaction = ajax_save_form.attr('action');
  
    jQuery('.successformdiv').html('');
    jQuery('.errormessageformdiv').html('');
    $.ajax({
      enctype: 'multipart/form-data',
      url: formaction,
      data: new FormData(this),
      method:'post',
      dataType: 'json', 
      processData: false,
      contentType: false,
      cache: false,
      timeout: 600000,
      beforeSend: function() {
        $("#dcare__btn").hide();
        //jQuery('#submitscnow').prop('disabled',true);     
      },
      success : function(json) {
        swal("Your Form Has Been Submitted!", {
          icon: "success",
        });
        window.location.href = "/";
                  $('.ajax-save-form')[0].reset();

    },
       error : function(xhr,errmsg,err) {
        $('#errormessageformdiv').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
    }
  //     success : function(response) {
  //       jQuery('.successformdiv').html();
  //       jQuery('.errormessageformdiv').html('');

  //       jQuery('#submitscnow').val('Submit');
  //       if(response.status) {
  // alert('i')

  //         swal("Your Form Has Been Submitted!", {
  //           icon: "success",
  //         });
         
  //         $('.ajax-save-form')[0].reset();
  
  
  //         $('.request-area').html();
  
  
  //         $('#responsecontainer').html();
  
  //         // ajax_save_form.hide();
  //         if(response.http_redirect) {
  //           window.location.href = response.http_redirect;
  //         }
  //       } else {

  //         jQuery('.errormessageformdiv').html(response.message);
  //         jQuery('.successformdiv').html();
  //         var alert = $('div.alert[auto-close]');
  //         alert.each(function() {
  //           var that = $(this);
  //           var time_period = that.attr('auto-close');
  //           window.setTimeout(function() {
  //             that.fadeTo(500, 0).slideUp(500, function(){
  //               that.remove(); 
  //             });
  //           }, time_period);
  //         });
  //       }
  //     }
      // error: function(jq,status,message) { alert('A jQuery error has occurred. Status: ' + status + ' - Message: ' + message); }
    });
  });
   $(".my-carouselevent").owlCarousel({
          autoplay: true,
          dots: true,
          loop: true,
          margin:15,
          nav: true,
          responsive: {
            0: {
              items: 1
            },
            768: {
              items: 2
            },
            900: {
              items: 3
            }
          }
        });
  $(".my-carousel4").owlCarousel({
          autoplay: true,
          loop: true,
          margin:15,
          responsive: {
            0: {
              items: 1
            },
            575: {
              items: 2
            },
            768: {
              items: 3
            },
            900: {
              items: 6
            }
          }
        });
  $(".my-carousel").owlCarousel({
          autoplay: true,
          dots: true,
          loop: true,
          margin:15,
          nav: true,
          responsive: {
            0: {
              items: 1
            },
            768: {
              items: 2
            },
            900: {
              items: 3
            }
          }
        });
        $(".my-carousel1").owlCarousel({
          autoplay: true,
          loop: true,
          margin:15,
          responsive: {
            0: {
              items: 1
            },
            768: {
              items: 2
            },
            900: {
              items: 3
            }
          }
        });
  
  
      
        