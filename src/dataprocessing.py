import sys ,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from settings import *
from priority_classes.datahandler.datahandler import Handler

hd = Handler()
