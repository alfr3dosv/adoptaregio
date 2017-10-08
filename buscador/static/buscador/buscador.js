
$(document).ready( function() {
			$('#buscar').click(function () {
				console.log(mascotas);
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
			console.log(texto);
		}
	});
});