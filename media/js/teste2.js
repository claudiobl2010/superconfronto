$(document).ready(function() {
	
	$('#btn-ok').click(function() {
        $.ajax({
			type: "POST",
			url: "/teste3",
			data: {nome: $('#nome').html(), sobrenome: $('#sobrenome').val()},
			dataType: "json",
			success: function(response) {
				var inner_html = '';
				inner_html += response.nome + ' ' + response.sobrenome;
				inner_html += '<br>';
				inner_html += '<ul>';
				
				$.each(response.lista, function(index, element) {
					inner_html += '<li>' + (index + 1) + '. = ' + element + '</li>';
				});
				
				inner_html += '</ul>';
				
				$('#nome-completo').html(inner_html)
			},
			error: function() {
				alert("error!!!");
			}
        });		
	});

});
