(function($) {

	function readWPAdminCookie() {
		var cookieJsonMode = $.cookie.json,
			cookieValue;
		$.cookie.json = true;
		cookieValue = $.cookie(window.__wpadmin_cookie_name);
		$.cookie.json = cookieJsonMode;
		if (cookieValue) {
			return cookieValue;
		}
		return {};
	}

	function writeWPAdminCookie(cookieValue) {
		var cookieJsonMode = $.cookie.json;
		$.cookie.json = true;
		$.cookie(window.__wpadmin_cookie_name,
				 cookieValue,
				 {'path': window.__admin_url,
				  'expires': 10});
		$.cookie.json = cookieJsonMode;
	}

	function updateMenuToolTexts($menuTool, newText) {
		$('a', $menuTool).text(newText);
	}

	function collapsibleLeftMenu() {
		var settings = readWPAdminCookie();
		if (!$('body').hasClass('wp-folded')) {
			$('body').addClass('wp-folded');
			updateMenuToolTexts($('#collapse-menu'), $('#collapse-menu').data('text-collapsed'));
			settings['folded'] = true;
		} else {
			$('body').removeClass('wp-folded');
			updateMenuToolTexts($('#collapse-menu'), $('#collapse-menu').data('text-expanded'));
			settings['folded'] = false;
		}
		writeWPAdminCookie(settings);
	}

	function pinnableLeftMenu() {
		var settings = readWPAdminCookie();
		if (!$('body').hasClass('wp-pinned')) {
			$('body').addClass('wp-pinned');
			updateMenuToolTexts($('#pin-menu'), $('#pin-menu').data('text-pinned'));
			settings['pinned'] = true;
		} else {
			$('body').removeClass('wp-pinned');
			updateMenuToolTexts($('#pin-menu'), $('#pin-menu').data('text-unpinned'));
			settings['pinned'] = false;
		}
		writeWPAdminCookie(settings);
	}

	function fitTopMenu() {
		var $topMenu = $('#adminbar').removeClass('wp-narrow'),
			maxWidth = $topMenu.outerWidth(true),
			width = 0;

		$topMenu.children('li').each(
			function() {
				width += $(this).outerWidth(true);
			}
		);

		if (width > maxWidth) {
			$topMenu.addClass('wp-narrow');
		}
	}

	function fitLeftMenu() {
		if ($(window).width() < 780) {
			$('body').addClass('wp-folded wp-force-folded');
			$('#collapse-menu').hide();
		} else {
			if ($('body').hasClass('wp-force-folded')) {
				var settings = readWPAdminCookie();
				$('#collapse-menu').show();
				$('body').removeClass('wp-force-folded');
				if (!settings['folded']) {
					$('body').removeClass('wp-folded');
				}
			}
		}
	}

	$(document).ready(function() {

		var settings = readWPAdminCookie();
		if (settings['folded'] && !$('body').hasClass('wp-folded')) {
			collapsibleLeftMenu();
		}
		if (settings['pinned'] && !$('body').hasClass('wp-pinned')) {
			pinnableLeftMenu();
		}

		$(window).resize(
			function() {
				fitTopMenu();
				fitLeftMenu();
			}
		).resize();

		$('#collapse-menu').click(function() {
			collapsibleLeftMenu();
		});

		$('#pin-menu').click(function() {
			pinnableLeftMenu();
		});

		// left submenus should stay on page
		$('#adminmenu .wp-has-submenu').hover(
			function() {
				if (!$(this).hasClass('wp-menu-top') || ($('body').hasClass('wp-folded') || $(this).hasClass('wp-menu-not-open'))) {
					var $submenu = $(this).children('.wp-submenu').css({'visibility': 'hidden', 'display': 'block'}),
						extra_margin = 0,
						window_bottom_edge = $(window).scrollTop() + $(window).height(),
						submenu_bottom_edge = $submenu.offset().top + $submenu.outerHeight() + extra_margin;

					if (window_bottom_edge < submenu_bottom_edge) {
						$submenu.css({'margin-top': '-' + (submenu_bottom_edge - window_bottom_edge) + 'px'});
					}
					$submenu.css({'visibility': 'visible'});
				}
			},
			function() {
				$(this).children('.wp-submenu').removeAttr('style');
			}
		);

		// top submenus should stay on page
		$('#adminbar .wp-has-submenu').hover(
			function() {
				var $submenu = $(this).children('.wp-submenu').css({'visibility': 'hidden', 'display': 'block'}),
					extra_margin = 0,
					window_right_edge = $(window).width(),
					submenu_right_edge = $submenu.offset().left + $submenu.width() + extra_margin;

				if (window_right_edge < submenu_right_edge) {
					$submenu.css({'margin-left': '-' + (submenu_right_edge - window_right_edge) + 'px'});
				}
				$submenu.css({'visibility': 'visible'});
			},
			function() {
				$(this).children('.wp-submenu').removeAttr('style');
			}
		);

	});

})(jQuery);