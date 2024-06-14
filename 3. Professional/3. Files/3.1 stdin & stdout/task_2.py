# The scope of the data

import sys
from datetime import datetime

data = [datetime.strptime(i.strip('\n'), '%Y-%m-%d') for i in sys.stdin]

sys.stdout.write(str((max(data) - min(data)).days))