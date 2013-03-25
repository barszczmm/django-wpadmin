jQuery(document).ready(function($) {

	// filters
	$('#changelist-filter .filter').each(
		function() {
			$(this).width($(this).width());
		}
	);
	$('#changelist-filter .filter ul').each(
		function() {
			$(this).css({'left': $(this).position().left});
		}
	);

	// icons
	$('#changelist-form img[src$="icon-yes.gif"]').hide()
		.after('<i class="icon-ok-sign"></i>');

	$('#changelist-form img[src$="icon-no.gif"]').hide()
		.after('<i class="icon-minus-sign"></i>');
});