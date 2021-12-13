$(document).ready(function(){

    $('#btn-init').click(function(event){
        event.preventDefault();
        var data = new FormData($('#form-read-eda')[0]);
        console.log(data);
        $.ajax({
            url: '/edaanalisis',
            data: data,
            type: 'POST',
            contentType: false,
            processData: false,
            success: function(response){
                //$("#features-container").css("display","block");
                /*
                var tabla_completa = response[0];
                var shape = "<p><b>Shape: </b>"+response[1]+"</p>";
                var type = "<p><b>Types: </b>"+response[2]+"</p>";
                var nulos = "<br><p>"+response[3]+"</p>";
                var realcion = response[4];
                var imagen_heap = response[5];
                var imagen_heap_inf = response[6];
                var imagen_heap_sup = response[7];
                var labels = response[8];*/
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
                
                //$("#shape").html(response[1]);
                /*
                
                $("#faltantes").html(response[3]);
                //$("#relation_values").html(response[4]);
                $("#heap").html(response[5]);
                //$("#heap_inf").html(imagen_heap_inf);
                //$("#heap_sup").html(imagen_heap_sup);
                $("#abscisa_options").html(labels);
                $("#ordenada_options").html(labels);
                if( $('#table1').length){
                    $('#table1').DataTable( {
                        responsive: true
                    } );
                }
                if( $('#table2').length){
                    $('#table2').DataTable( {
                        responsive: true
                    } );
                }
                $("#js-loader").css("display","none");
                */
                console.log(response);
            },
            error: function(error){
                console.log(error);
            }
        });
    });
});