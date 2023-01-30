function setViewModal(id_number, firstname, middlename, lastname, birthdate, position, contact_number, dp){

    document.getElementById("view_id_number").value = id_number;
    document.getElementById("view_firstname").innerHTML = firstname;
    document.getElementById("view_middlename").innerHTML = middlename;
    document.getElementById("view_lastname").innerHTML = lastname;
    document.getElementById("view_birthdate").value = birthdate;
    document.getElementById("view_position").value = position;
    document.getElementById("view_contact_number").value = contact_number;
    document.getElementById("view_image").src = "/static/members/"+id_number+"/"+dp;
    
 

}

$(function(){
    $('#account_delete').click(function() {

        $("tr[id=account_confirmdelete]").removeAttr('hidden');
        $(this).attr("hidden", true);
        $('.account_delete_checkbox').removeAttr('hidden');

    
    });

    $('#account_canceldelete').click(function (){
     
        $('#account_confirmdelete').attr("hidden", true);
        $('#account_delete').removeAttr("hidden");
        $('.account_delete_checkbox').attr('hidden', true);

    });
});