$(document).ready(function() {
	
	$("#img-acessar").mouseover(function() {
		$(this).attr("src", "/media/img/btn_acessar_pressed.png");
	}).mouseout(function() {
		$(this).attr("src", "/media/img/btn_acessar.png");
	});

	$("#img-cadastre-se-agora").mouseover(function() {
		$(this).attr("src", "/media/img/btn_cadastre-se_agora_pressed.png");
	}).mouseout(function() {
		$(this).attr("src", "/media/img/btn_cadastre-se_agora.png");
	});
	
	$('#id-autenticacao').click(function() {
		if ($('#id-login').val() == "" || $('#id-senha').val() == "") {
			inner_html = '<strong>atenção!</strong>';
			$('#id-msg-login-1').html(inner_html);
			$('#id-msg-login-1').addClass('sc-msg-login-1-error');
			$('#id-msg-login-1').removeClass('sc-msg-login-1');
			
			inner_html = '<strong>login e/ou senha não preenchidos</strong>';
			$('#id-msg-login-2').html(inner_html);
			$('#id-msg-login-2').addClass('sc-msg-login-2-error');
			$('#id-msg-login-2').removeClass('sc-msg-login-2');
		}
		else {
	        $.ajax({
				type: "POST",
				url: "/autenticacao",
				data: {login: $('#id-login').val(), senha: $('#id-senha').val()},
				dataType: "json",
				success: function(response) {
					if (response.tipo == 1) {
						$(location).attr("href", "/home");
					}
					else {
						inner_html = '<strong>atenção!</strong>';
						$('#id-msg-login-1').html(inner_html);
						$('#id-msg-login-1').addClass('sc-msg-login-1-error');
						$('#id-msg-login-1').removeClass('sc-msg-login-1');
						
						inner_html = '<strong>' + response.msg + '</strong>';
						$('#id-msg-login-2').html(inner_html);
						$('#id-msg-login-2').addClass('sc-msg-login-2-error');
						$('#id-msg-login-2').removeClass('sc-msg-login-2');
						
						$('#id-login').val("");
						$('#id-senha').val("");
						$('#id-login').focus();
					}
				},
				error: function() {
					inner_html = '<strong>atenção!</strong>';
					$('#id-msg-login-1').html(inner_html);
					$('#id-msg-login-1').addClass('sc-msg-login-1-error');
					$('#id-msg-login-1').removeClass('sc-msg-login-1');
					
					inner_html = '<strong>ocorreu erro, tente novamente</strong>';
					$('#id-msg-login-2').html(inner_html);
					$('#id-msg-login-2').addClass('sc-msg-login-2-error');
					$('#id-msg-login-2').removeClass('sc-msg-login-2');
					
					$('#id-login').val("");
					$('#id-senha').val("");
					$('#id-login').focus();

					alert("Ocorreu um erro ao tentar efetuar o login.\nTente novamente.");
				}
	        });
		}
		return false;
	});

});
