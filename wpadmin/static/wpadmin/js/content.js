jQuery(document).ready(function($) {

	// filters
	$('#changelist-filter .filter').each(
		function() {
			$(this).width($(this).outerWidth(true) + 15);
		}
	);
	$('#changelist-filter .filter ul').each(
		function() {
			$(this).css({'position': 'absolute', 'left': $(this).position().left});
		}
	);

	// icons
	$('img[src$="/admin/img/icon-yes.gif"][alt="True"]').hide()
		.after('<i class="fa fa-fw fa-check-square-o"></i>');

	$('img[src$="/admin/img/icon-no.gif"][alt="False"]').hide()
		.after('<i class="fa fa-fw fa-minus-square-o"></i>');

	// collapsible fieldsets
	$('.module.collapse.collapse-opened h2 .collapse-toggle').click();

	// fix bottom bar buttons widths
	function fixBottomBar() {
		var $bar = $('#bottombar').removeClass('wp-narrow'),
			width = 0;
		if ($bar.length) {
			$bar.children().each(
				function() {
					width += $(this).outerWidth(true);
				}
			);
			if (width > $('#content').outerWidth(true)) {
				$bar.addClass('wp-narrow');
			}
		}
	}

	$(window).resize(fixBottomBar).resize();
});