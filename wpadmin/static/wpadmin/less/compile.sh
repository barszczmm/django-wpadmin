#!/bin/bash

# Less v2.4.0 is used, but it may also work with other versions

lessc -x wpadmin.less > ../css/wpadmin.css
lessc -x themes/blue/theme.less > ../css/themes/blue.css
lessc -x themes/coffee/theme.less > ../css/themes/coffee.css
lessc -x themes/default/theme.less > ../css/themes/default.css
lessc -x themes/ectoplasm/theme.less > ../css/themes/ectoplasm.css
lessc -x themes/light/theme.less > ../css/themes/light.css
lessc -x themes/midnight/theme.less > ../css/themes/midnight.css
lessc -x themes/milo/theme.less > ../css/themes/milo.css
lessc -x themes/milo-light/theme.less > ../css/themes/milo-light.css
lessc -x themes/ocean/theme.less > ../css/themes/ocean.css
lessc -x themes/sunrise/theme.less > ../css/themes/sunrise.css

