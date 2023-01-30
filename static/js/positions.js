
$(function(){

    $('#pl_delete').click(function() {

        $("tr[id=pl_confirmdelete]").removeAttr('hidden');
        $(this).attr("hidden", true);
        $('.pl_delete_checkbox').removeAttr('hidden');

    
    });

    $('#pl_canceldelete').click(function (){
     
        $('#pl_confirmdelete').attr("hidden", true);
        $('#pl_delete').removeAttr("hidden");
        $('.pl_delete_checkbox').attr('hidden', true);

    });

    $('#p_delete').click(function() {

        $("tr[id=p_confirmdelete]").removeAttr('hidden');
        $(this).attr("hidden", true);
        $('.p_delete_checkbox').removeAttr('hidden');

    
    });

    $('#p_canceldelete').click(function (){
     
        $('#p_confirmdelete').attr("hidden", true);
        $('#p_delete').removeAttr("hidden");
        $('.p_delete_checkbox').attr('hidden', true);

    });
  
  });
// function pl_delete(){
//     pl_delete = document.getElementById("pl_delete");
//     pl_confirmdelete = document.getElementById("pl_confirmdelete");

//     pl_delete.style.visibility = "hidden";

//     pl_delete_checkbox = document.getElementsByClassName("pl_delete_checkbox");

//     for(i=0; i < pl_delete_checkbox.length; i++){
//         pl_delete_checkbox[i].removeAttribute("hidden");
//     }

//     pl_confirmdelete.removeAttribute("hidden");
// }


// function pl_canceldelete(){
//     pl_delete = document.getElementById("pl_delete");
//     pl_confirmdelete = document.getElementById("pl_confirmdelete");
//     pl_canceldelete = document.getElementById("pl_canceldelete");

//     pl_delete.style.visibility = "visible";

//     pl_delete_checkbox = document.getElementsByClassName("pl_delete_checkbox");

//     for(i=0; i < pl_delete_checkbox.length; i++){
//         pl_delete_checkbox[i].setAttribute("hidden", true);
//     }

//     pl_confirmdelete.setAttribute("hidden", true);
//     pl_canceldelete.setAttribute("hidden", true);
// }