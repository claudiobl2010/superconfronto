$(document).ready(function() {
	
	$("#img-salvar").mouseover(function() {
		$(this).attr("src", "/media/img/btn_salvar_cadastro_pressed.png");
	}).mouseout(function() {
		$(this).attr("src", "/media/img/btn_salvar_cadastro.png");
	});
	
	$('#id-salvar').click(function() {
		if ($('#id-nome-pessoa').val() == "") {
			$('#id-label-nome-pessoa').css("color", "#FF3333");
		}
		else {
			$('#id-label-nome-pessoa').css("color", "#999999");
		}

		return false;
	});


});
