$(document).ready(function (){

	$("#button_pearson").click(function(event){
		event.preventDefault();
		var data = new FormData($('#form_pearson')[0]);
		$.ajax({
			url: '/read_data_for_sc', //ruta para el manejo con python
			data: data,
			type: 'POST',
			contentType: false,
			processData: false,
			success: function(response){
				$('#matrizPearson').html(response['keyPearson'])				
			},
			error: function(error){
				console.log(error);
				event.preventDefault();
			}
		});    
	});


});


