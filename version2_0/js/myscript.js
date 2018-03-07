
 
 $( document ).ready(function() {
   var href= $(location).attr('href'); 
       var rez1= href.indexOf('?');   
      var  z = href.substr(rez1+1,href.length)
        
     if(z=='post=result_traning'){
						var root= $('.root').val();
						var model_name= $('.model_name').val();		
                    $.ajax({
                        url: "/hi.py?post=start_trening",
                        type: "post",
                        datatype:"json",
                        data: {'root':root,'model_name':model_name},
                        success: function(response){
						$('h1').text(response.message);
						$('h2').text(response.keys);
						
                        }
                    });
     }
      $(document).click(function(event) {  
    if ($(event.target).closest(".metkaForm").length) return;
    $('.loginForm').hide();
    event.stopPropagation();
  });
       var countFileInputAdd=0;
       var countFileInputChange=0;
        $.eventFileImage = function(slClass){
            var lenghtElement=slClass;
                       $('#file'+lenghtElement).change(function () {
           
        var input = $(this)[0];
                           
        if (input.files && input.files[0]) {
               
     
       
            if (input.files[0].type.match('image.*')) {
                var reader = new FileReader();
                 
                reader.onload = function (e) {
                         countFileInputAdd++;
                      if(countFileInputAdd<2)
                        {
                            $(".buttonStartTraning").hide();
                            $(".buttonStartTraningText").hide();
                        }
                     else
                        {
                             $(".buttonStartTraning").show();
                             $(".buttonStartTraningText").show();
                        }
                 
                    $('.img'+lenghtElement).attr('src', e.target.result);
                     $('.img'+lenghtElement).show();
                    $('.button'+lenghtElement).show();
                     $('.ServerImage').hide();
                  
                }
                reader.readAsDataURL(input.files[0]);
            } else {
                console.log('ошибка, не изображение');
            }
        } else {
            console.log('хьюстон у нас проблема');
              countFileInputAdd--;
            if(countFileInputAdd<2)
                {
                    $(".buttonStartTraning").hide();
                    $(".buttonStartTraningText").hide();
                }
            else
                {
                     $(".buttonStartTraning").show();
                    $(".buttonStartTraningText").show();
                }
        }
    });
        };
          $.fileLoad = function(slClass){
         var lenghtElement=slClass;
               $("#prodId").val((lenghtElement));
        $(".ElementDinamic").append("<span class='numform"+lenghtElement+"'>Class "+(lenghtElement+1)+"</span><br class='numform"+lenghtElement+"'><div class='formFile numform"+lenghtElement+"'><input class='numform"+lenghtElement+"' type='file' id='file"+lenghtElement+"' name='file"+lenghtElement+"'  multiple='' accept='image/x-png,image/gif,image/jpeg' /><br class='numform"+lenghtElement+"'><div id='numform"+lenghtElement+"' class='delFileInput'>Remove Image</div></div>");
    };
    //Train Neural Network Создание form input file
    $.fileLoad(0);
    $.fileLoad(1);
    //Train Neural Network Привязка к событию input file
      $.eventFileImage(0);
      $.eventFileImage(1);
     //Classify an Image Привязка к событию input file
      $.eventFileImage(900);
     //Train Neural Network Скритие кнопок удалить
    $(".delFileInput").hide();
        //Login форма
    $('.loginButton').click(function (e){
       var display= $('.loginForm').css('display');
        if(display=="none") {
            $('.loginForm').show();
        }
        else
        {
            $('.loginForm').hide();
        }
        e.preventDefault();
    });
     
       $( ".formMenyFiles" ).submit(function( event ) {
                        
                  $('#loading1').show();
                 $('#loadingFon').show();
                $('#loading1 p').show();
           
   
        });

             $( ".formFile" ).submit(function( event ) {
                        
                  $('#loading1').show();
                 $('#loadingFon').show();
        });

      $(".inputId").on("change paste keyup", function() {
       if($(this).val().length==8&&$.isNumeric($(this).val()))
           {
               $(".inputfileCenter").show();
                $( ".inputId").css("border-color","gray");
           }
          else
            {
                $(".inputfileCenter").hide();
                $( ".inputId").css("border-color","red");
            }
      });
     // добавить form input
     $('.addFileInput').click(function (e){
          var lenghtElement=$('.formFile').length;
         if(lenghtElement<4)
             { }
         else{
              $( ".addFileInput").hide();
         }
          // Нарисовать формы и кнопки
          $.fileLoad(lenghtElement);
          // Удалить форму form input
            $('.delFileInput').click(function (e){
           
         var lenghtElement=$('.formFile').length;
                    if(lenghtElement<6)
             {
                   $( ".addFileInput").show();
             }
              var id= $(this).attr("id")
                //Удаление всего кроме кнопки
              $( "."+ id).empty();
             $( "."+ id).remove();
                //Удаление кнопки
             $( "#"+ id).empty();
             $( "#"+ id).remove();
                 lenghtElement=$('.formFile').length;
                     var i = 0;
                  var divs = $('.ElementDinamic span');
                        while (i < lenghtElement) {
                         $(divs[i]).text("Class "+(i+1));
                            i++;
                        }
                  $("#prodId").val((lenghtElement-1));
            });
          
         //События подключить
            $.eventFileImage(lenghtElement);
         
     });
  
  
});
  
 

