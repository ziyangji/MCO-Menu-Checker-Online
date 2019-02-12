$(function () {
	$('.card-body').click(function () {
		for (var i = 0; i < 4; i++) {
			if($(this).children('card-text').hasClass("1")) {
				alert(module);
			}
		}
		
	})
});