function showMessage(opts) {

	var box_msg = "";
	box_msg += "<div class='sc-box-msg'>";
	box_msg += "<div class='sc-msg-fechar'>";
	box_msg += "<a href='#'><img src='/media/img/msg_fechar.png'></a>";
	box_msg += "</div>";
	box_msg += "<div class='sc-msg-content'>";
	box_msg += "<img src='/media/img/msg_sucesso.png'>";
	box_msg += '<strong>Seu time foi escalado com sucesso!</strong>';	
	box_msg += "</div>";
	box_msg += "</div>";
	
    $(box_msg).appendTo($("#sc-doc"));
	
	$(".sc-box-msg").fadeIn("slow");
	
	
}