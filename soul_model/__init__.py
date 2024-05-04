# soul_model/__init__.py

# Import individual modules
from .soul_object import SoulObject
from .emotions import Emotions
from .memories import Memories
from .personality import Personality
from .beliefs import Beliefs
from .consciousness import Consciousness

# Define __all__ to specify exported symbols
__all__ = [
    'SoulObject',
    'Emotions',
    'Memories',
    'Personality',
    'Beliefs',
    'Consciousness'
]
