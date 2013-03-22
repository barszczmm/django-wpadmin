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

});