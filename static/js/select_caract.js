$(document).ready(function(){
	$("#analisis-sc").hide();
	$("#analisis-pca").hide();
	$("#btn-init-sc").click(function(event){
		event.preventDefault();
		var data = new FormData($('#form-read-sc')[0]);
		if($("#check-corr").prop("checked")){
			console.log("Correlacional");
			$.ajax({
				url: '/sc-corr', //ruta para el manejo con python
				data: data,
				type: 'POST',
				contentType: false,
				processData: false,
				success: function(response){
					$("#analisis-sc").show();
					$("#table-sc").html(response['sc-table']);
					$("#tsc-table").DataTable({ 
						responsive: true,
					});
					$("#sc-dtype").html(response["sc-dtype"]);
					$("#tsc-dtype").DataTable({ 
						"paging": false,
						"ordering": false,
						"info": false
					});
					$("#sc-faltantes").html(response["sc-faltantes"]);
					$("#tsc-null").DataTable({ 
						"paging": false,
						"ordering": false,
						"info": false
					});
					$("#sc-corr").html(response["sc-corr"]);
					$("#tsc-corr").DataTable({ 
						"paging": false,
						"ordering": false,
						"info": false
					});

					$("#sc-heapmap").html(response["heapmap"]);
				},
				error: function(error){
					console.log(error);
					event.preventDefault();
				}
			}); 
		} else{
			console.log("...PCA");
			$.ajax({
				url: '/sc-pca', //ruta para el manejo con python
				data: data,
				type: 'POST',
				contentType: false,
				processData: false,
				success: function(response){
					$("#analisis-sc").show();
					$("#table-sc").html(response['sc-table']);
					$("#tsc-table").DataTable({ 
						responsive: true,
					});
					$("#sc-dtype").html(response["sc-dtype"]);
					$("#tsc-dtype").DataTable({ 
						"paging": false,
						"ordering": false,
						"info": false
					});
					$("#sc-faltantes").html(response["sc-faltantes"]);
					$("#tsc-null").DataTable({ 
						"paging": false,
						"ordering": false,
						"info": false
					});
					$("#sc-corr").html(response["sc-corr"]);
					$("#tsc-corr").DataTable({ 
						"paging": false,
						"ordering": false,
						"info": false
					});
				},
				error: function(error){
					console.log(error);
					event.preventDefault();
				}
			}); 
		}

		   
	});


});


