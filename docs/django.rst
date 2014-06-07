Changes in Django's ModelAdmin behaviour
========================================

Ignored ModelAdmin options
--------------------------

Some options of Django's ModelAdmin are ignored when Django WP Admin is used:

**ModelAdmin.actions_on_top**
    Actions and pagination are always visible above objects lists.

**ModelAdmin.actions_on_bottom**
    Actions and pagination are always visible below objects lists.

**ModelAdmin.save_on_top**
    Save buttons are always displayed at the bottom of the page.


Additional ModelAdmin options
-----------------------------

There is one additional class for fieldsets: ``collapse-opened`` - it tells Django to create collapsible fieldset but opened by default.

