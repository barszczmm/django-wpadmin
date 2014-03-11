from django.contrib import admin


class TestModelAdmin(admin.ModelAdmin):
    pass
    #raw_id_fields = ('foreign_key',)


class MoreComplicatedTestModelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': ('big_integer',
                       ('boolean', 'char', 'comma_separated_integer')),
        }),
        ('Wide fieldset', {
            'fields': (('date', 'date_time', 'time')),
            'classes': ('wide',),
        }),
        ('Collapsed fieldset', {
            'fields': ('decimal', 'email', 'file_path', 'float'),
            'classes': ('collapse',),
        }),
        ('Fieldset with description', {
            'fields': ('integer', 'ip_address', 'generic_ip_address',
                       'null_boolean'),
            'classes': ('collapse',),
            'description': 'A string of optional extra text to be displayed '
                           'at the top of each fieldset, under the heading of '
                           'the fieldset.<br /><br />'
                           'Note that this value is not HTML-escaped when '
                           'it\'s displayed in the admin interface. This lets '
                           'you include HTML if you so desire.'
        }),
        ('Collapsible but opened by default fieldset', {
            'fields': ('positive_integer', 'positive_small_integer', 'slug',
                       ('small_integer', 'text', 'url')),
            'classes': ('collapse collapse-opened',),
            'description': 'A string of optional extra text to be displayed '
                           'at the top of each fieldset, under the heading of '
                           'the fieldset.<br /><br />'
                           'Note that this value is not HTML-escaped when '
                           'it\'s displayed in the admin interface. This lets '
                           'you include HTML if you so desire.'
        }),
        ('Foreign and many to many', {
            'fields': ('foreign_key', 'many_to_many', 'one_to_one'),
        }),
    )
    radio_fields = {'foreign_key': admin.VERTICAL,
                    'one_to_one': admin.HORIZONTAL}
    #raw_id_fields = ('foreign_key',)
    #filter_horizontal = ('many_to_many',)
    #filter_vertical = ('many_to_many',)

