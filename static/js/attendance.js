$(document).ready(function() {
    $("#sort_form").change(function(){
        var sort = $(this).find(":selected").val();
        var filter = $('#filter').find(":selected").val();
        // var page = $("#page").val();
        var target = $('#target_attendance').find(":selected").val();
        if(filter == 'all')
        {
            window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
        }
        if(filter == 'today')
        {
            window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
        }
        if(filter == 'thisweek')
        {
            $("#month_input").attr("hidden", true);
            $("#day_input").attr("hidden", true);
            window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
        }
        if(filter == 'lastweek')
        {
            $("#month_input").attr("hidden", true);
            $("#day_input").attr("hidden", true);
            window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
        }
        if(filter == 'day')
        {
            
             var day = $("#day_input_form").val();
     
    
            location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&day="+day+"&page=1";
        }
        if(filter == 'month')
        {
            var month = $("#month_input_form").val();
     
    
            location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&month="+month+"&page=1";
        }
        
    });
    $("#target_attendance").change(function(){
        var sort = $('#sort_form').find(":selected").val();
        var filter = $('#filter').find(":selected").val();
        var target = $(this).find(":selected").val();
        // var page = $("#page").val();

        if(filter == 'all')
        {
            window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
        }
        if(filter == 'today')
        {
            window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
        }
        if(filter == 'thisweek')
        {
            $("#month_input").attr("hidden", true);
            $("#day_input").attr("hidden", true);
            window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
        }
        if(filter == 'lastweek')
        {
            $("#month_input").attr("hidden", true);
            $("#day_input").attr("hidden", true);
            window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
        }
        if(filter == 'day')
        {
            
             var day = $("#day_input_form").val();
     
    
            location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&day="+day+"&page=1";
        }
        if(filter == 'month')
        {
            var month = $("#month_input_form").val();
     
    
            location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&month="+month+"&page=1";
        }
           
       
        
    });
    $("#filter").change(function(){
        var sort = $('#sort_form').find(":selected").val();
        var filter = $(this).find(":selected").val();
        var target = $('#target_attendance').find(":selected").val();

        if(filter == 'all')
        {
            $("#month_input").attr("hidden", true);
            $("#day_input").attr("hidden", true);
            window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
        }
        if(filter == 'today')
        {
            $("#month_input").attr("hidden", true);
            $("#day_input").attr("hidden", true);
            window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
        }
        if(filter == 'thisweek')
        {
            $("#month_input").attr("hidden", true);
            $("#day_input").attr("hidden", true);
            window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
        }
        if(filter == 'lastweek')
        {
            $("#month_input").attr("hidden", true);
            $("#day_input").attr("hidden", true);
            window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
        }
        if(filter == 'day')
        {
            $('#day_input').removeAttr("hidden");
            $("#month_input").attr("hidden", true);
        }
        if(filter == 'month')
        {
            $('#month_input').removeAttr("hidden");
            $("#day_input").attr("hidden", true);
        }
        
    });
    $("#day_input").change(function(){
        var sort = $('#sort_form').find(":selected").val();
        var filter = $('#filter').find(":selected").val();
        var target = $('#target_attendance').find(":selected").val();
    

        var day = $('#day_input_form').val();
     
    
        window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&day="+day+"&page=1";

        
    });
    $("#month_input").change(function(){
        var sort = $('#sort_form').find(":selected").val();
        var filter = $('#filter').find(":selected").val();
        var month = $('#month_input_form').val();
        var target = $('#target_attendance').val();
        
        window.location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&month="+month+"&page=1";

        
    });

    $("#target_attendance").change(function(){
        var sort = $('#sort_form').find(":selected").val();
        var filter = $('#filter').find(":selected").val();
        var target = ('#target_attendance_form').find(":selected").val();
        
        window.location.href = '/attendance?filter='+filter+"&sort="+sort+"&month="+month+"&target="+target+"&page=1";

        
    });
    
});

function nextPage(){
    page = parseInt(document.getElementById("page").value)+1;
    filter = document.getElementById("filter").value;
    sort = document.getElementById("sort_form").value;
    target = document.getElementById("target_attendance").value;
    
    console.log('NextPage');
    if(filter == 'all')
    {
   
        location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
    }
    if(filter == 'today')
    {
    
        location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
    }
    if(filter == 'thisweek')
    {

        location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
    }
    if(filter == 'lastweek')
    {

        location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
    }
    if(filter == 'day')
    {
        var day = document.getElementById("day_input_form").value;
     
    
        location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&day="+day+"&page=1";
    }
    if(filter == 'month')
    {
        var month = document.getElementById("month_input_form").value;
        
        location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&month="+month+"&page=1";
    }
   

};
function previousPage(){
    page = parseInt(document.getElementById("page").value)-1;
    filter = document.getElementById("filter").value;
    sort = document.getElementById("sort_form").value;
    target = document.getElementById("target_attendance").value;
  
   
    if(filter == 'all')
    {
   
        location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
    }
    if(filter == 'today')
    {
    
        location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
    }
    if(filter == 'thisweek')
    {

        location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
    }
    if(filter == 'lastweek')
    {

        location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&page=1";
    }
    if(filter == 'day')
    {
        var day = document.getElementById("day_input_form").value;
     
    
        location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&day="+day+"&page=1";
    }
    if(filter == 'month')
    {
        var month = document.getElementById("month_input_form").value;
        
        location.href = '/attendance?target='+target+'&filter='+filter+"&sort="+sort+"&month="+month+"&page=1";
    }
   

};
