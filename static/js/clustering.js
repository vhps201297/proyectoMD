$(document).ready(function(){
    $("#res-cluster").hide();
    $('#btn-clustering').click(function(event){
        event.preventDefault();
        var data = new FormData($('#form-read-cluster')[0]);
        var url;
        console.log(data);
        if($("#check-jerar").prop("checked")){
            url = '/clust-jerarq';
        }else{
            url = '/clust-kmeans';
        }
        
        $.ajax({
            url: url,
            data: data,
            type: 'POST',
            contentType: false,
            processData: false,
            success: function(response){

                $("#res-cluster").show();
                $("#t-data").html(response['clust-table']);
                $("#id-tdata").DataTable({ 
                    responsive: true,
                });

                $("#t-num-elem").html(response['n_elements']);
                $("#id-nelem").DataTable({ 
                    "paging": false,
                    "ordering": false,
                    "info": false
                });

                $("#t-cluster").html(response['centroid']);
                $("#id-cen").DataTable({ 
                    "paging": false,
                    "ordering": false,
                    "info": false
                });
                
                console.log(response);
            },
            error: function(error){
                console.log(error);
            }
        });
    });
});