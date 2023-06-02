$(document).ready(function() {
    $("#month_year").change(function(){
        var data = $(this).val();
            window.location.href = '/reports?date='+data;
    })

        
    });

