$(document).ready(function(){
    $('btn-init').click((event)=>{
        var data = new FormData($('#form-data-eda')[0]);
        $.ajax({
            url: '/analisis-eda',
            data: form_data,
            type: 'POST',
            contentType: false,
            processData: false,
            success: function(response){
                $("#features-container").css("display","block");
                var tabla_completa = response[0];
                var shape = "<p><b>Shape: </b>"+response[1]+"</p>";
                var type = "<p><b>Types: </b>"+response[2]+"</p>";
                var nulos = "<br><p>"+response[3]+"</p>";
                var realcion = response[4];
                var imagen_heap = response[5];
                var imagen_heap_inf = response[6];
                var imagen_heap_sup = response[7];
                var labels = response[8];
                $("#tabla_data").html(response[0]);
                //$("#shape").html(response[1]);
                $("#dtype").html(response[2]);
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
                console.log(response);
            },
            error: function(error){
                console.log(response);
            }
        });
    });
});