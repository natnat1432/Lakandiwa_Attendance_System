$(document).ready(function() {
    $("#month_year").change(function(){
        var data = $(this).val();
            window.location.href = '/reports?date='+data;
    })

       
    $("#filter_member").change(function(){
        var data = $("#month_year").val();
        var filter = $(this).val();
        window.location.href = '/reports?date='+data+'&filter='+filter;
    });
    });

