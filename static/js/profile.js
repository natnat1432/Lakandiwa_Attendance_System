function samePassword() {
    var x;
    x = document.getElementById("newpassword").value;
    y = document.getElementById("confirmpassword").value;

    if (!x || !y )
    {
        alert("Please fill in the password fields.");
        return false;
    }
    if ( x != y) {
        alert("Passwords are not the same. Check your password inputs again");
        return false;
    };
}


function editProfile(){
    edit = document.getElementById("edit_profile");
    cancel = document.getElementById("cancel_edit_profile");
    confirmedit = document.getElementById("confirm_edit_profile");

    firstname = document.getElementById("firstname");
    middlename = document.getElementById("middlename");
    lastname = document.getElementById("lastname");
    birthdate = document.getElementById("birthdate");
    contact_number = document.getElementById("contact_number");


    edit.setAttribute("hidden", true);
    cancel.removeAttribute("hidden");
    confirmedit.removeAttribute("hidden");

    firstname.removeAttribute("disabled");
    middlename.removeAttribute("disabled");
    lastname.removeAttribute("disabled");
    birthdate.removeAttribute("disabled");
    contact_number.removeAttribute("disabled");


    
}

function cancelEdit(){
    location.reload();
}

function emptyEdit() {
   
    firstname = document.getElementById("firstname").value;
    middlename = document.getElementById("middlename").value;
    lastname = document.getElementById("lastname").value;
    birthdate = document.getElementById("birthdate").value;
    contact_number = document.getElementById("contact_number").value;

    if (firstname == "" || middlename == "" || lastname == "" || birthdate == "" || contact_number == "") {
        alert("Fill all the fields!");
        return false;
    };
}


function emptyImage(){
    if( document.getElementById("image-input").files.length == 0 ){
        alert("Upload image first!");
        return false;
    };
}