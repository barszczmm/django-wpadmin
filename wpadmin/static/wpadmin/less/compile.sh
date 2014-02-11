#!/bin/bash

lessc -x wpadmin.less > ../css/wpadmin.css
lessc -x themes/default/theme.less > ../css/themes/default.css
lessc -x themes/sunrise/theme.less > ../css/themes/sunrise.css
lessc -x themes/ocean/theme.less > ../css/themes/ocean.css

