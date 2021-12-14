$(document).ready(function(){
    $("#eda-analisis-cont").hide();
    $('#btn-init').click(function(event){
        event.preventDefault();
        var data = new FormData($('#form-read-eda')[0]);
        console.log(data);
        
        //var content = $('#eda-analisis-cont');
        //content.style.display = 'block';
        $.ajax({
            url: '/edaanalisis',
            data: data,
            type: 'POST',
            contentType: false,
            processData: false,
            success: function(response){

                $("#eda-analisis-cont").show();
                $("#table-eda").html(response['eda-table']);
                $("#eda-t").DataTable({ 
                    responsive: true,
                });
                $("#dtype").html(response["dtype"]);
                $("#eda-dtype").DataTable({ 
                    "paging": false,
                    "ordering": false,
                    "info": false
                });
                $("#faltantes").html(response["faltantes"]);
                $("#eda-null").DataTable({ 
                    "paging": false,
                    "ordering": false,
                    "info": false
                });

                $("#describe").html(response["describe"]);
                $("#eda-desc").DataTable({ 
                    "paging": false,
                    "ordering": false,
                    "info": false
                });

                $("#corr").html(response["corr"]);
                $("#eda-corr").DataTable({ 
                    "paging": false,
                    "ordering": false,
                    "info": false
                });
                $("#corr-heap").html(response["heapmap"])
                console.log(response);
            },
            error: function(error){
                console.log(error);
            }
        });
    });
});