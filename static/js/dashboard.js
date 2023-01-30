function emptywork() {
    var x;
    x = document.getElementById("work_done").value;
    if (x == "") {
        alert("Fill the work done!");
        return false;
    };
}