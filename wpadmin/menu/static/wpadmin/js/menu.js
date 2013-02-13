jQuery(document).ready(function($) {

	function readWPAdminCookie() {
		var cookieValue = $.cookie('django_wp_admin_settings');
		if (cookieValue) {
			return cookieValue;
		}
		return {};
	}

	function writeWPAdminCookie(cookieValue) {
		$.cookie('django_wp_admin_settings', cookieValue, {'path': window.__admin_url, 'expires': 20 * 365 * 24 * 60 * 60 * 1000});
	}

	function updateMenuToolTexts($menuTool, newText) {
		$('.wp-menu-tool-button', $menuTool).attr('title', newText);
		$('span', $menuTool).text(newText);
	}

	$('#collapse-menu').click(function() {
		var settings = readWPAdminCookie();
		if (!$('body').hasClass('wp-folded')) {
			$('body').addClass('wp-folded');
			updateMenuToolTexts($(this), $(this).data('text-collapsed'));
			settings['folded'] = true;
		} else {
			$('body').removeClass('wp-folded');
			updateMenuToolTexts($(this), $(this).data('text-expanded'));
			settings['folded'] = false;
		}
		writeWPAdminCookie(settings);
	});

	$('#pin-menu').click(function() {
		var settings = readWPAdminCookie();
		if (!$('body').hasClass('wp-pinned')) {
			$('body').addClass('wp-pinned');
			updateMenuToolTexts($(this), $(this).data('text-pinned'));
			settings['pinned'] = true;
		} else {
			$('body').removeClass('wp-pinned');
			updateMenuToolTexts($(this), $(this).data('text-unpinned'));
			settings['pinned'] = false;
		}
		writeWPAdminCookie(settings);
	});

	var settings = readWPAdminCookie();
	if (settings['folded'] && !$('body').hasClass('wp-folded')) {
		$('#collapse-menu').click();
	}
	if (settings['pinned'] && !$('body').hasClass('wp-pinned')) {
		$('#pin-menu').click();
	}


	// bookmarks


	// left submenu should stay on page
	$('#adminmenu .wp-menu-top.wp-has-submenu.wp-menu-not-open').hover(
		function() {
			var $submenu = $(this).children('.wp-submenu'),
				extra_margin = 8;
			$submenu.css({'visibility': 'hidden', 'display': 'block'});
			var window_bottom_edge = $(window).scrollTop() + $(window).height();
			var submenu_bottom_edge = $submenu.offset().top + $submenu.height() + extra_margin;
			if (window_bottom_edge < submenu_bottom_edge) {
				$submenu.css({'margin-top': '-' + (submenu_bottom_edge - window_bottom_edge) + 'px'});
			}
			$submenu.css({'visibility': 'visible'});
		},
		function() {
			$(this).children('.wp-submenu').removeAttr('style');
		}
	);

});
