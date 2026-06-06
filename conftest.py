import sys
from pathlib import Path

# Ajoute la racine du projet au PYTHONPATH pour permettre `import tools...`
_root = Path(__file__).parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))
