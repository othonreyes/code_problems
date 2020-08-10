from . import echo # importing a sibling module
from ..effects import * ## import all the effects in a uncle package
from .. import formats # import the whole module
from ..outputs import midi

formats.wavread()
midi()

def surround():
    pass