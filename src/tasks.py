import sys ,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from settings import *
import src.dataprocessing as dp
from priority_classes.datahandler.datahandler import Handler

hd = Handler()
