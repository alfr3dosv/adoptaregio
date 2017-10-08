
$(document).ready( function() {
	function find() {
		for(var indice = 0; indice < mascotas.length; indice++) {
			$("#"+mascotas[indice]['id']).hide();
			console.log("#"+mascotas[indice]['id']);
			for(var valor = 0; valor < caracteristicas.length; valor++) {
				var mascota = mascotas[indice];
				$("#"+mascota.pk).hide();
				var texto = mascota[caracteristicas[valor]];
				var textoBuscado = $("#buscar-texto").val();
				console.log(texto + " N " + textoBuscado);
				if(texto.toUpperCase().includes(textoBuscado.toUpperCase()) ) {
						$("#"+mascota.id).show();
				}
			}
		}
	}

	$('#buscar').click(function () {
		find();
	});

	$('#buscar').keyup(function (e) {
	    if (e.wich === 13) {
	    	find();
 	   }
    });
});