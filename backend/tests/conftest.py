import sys
from pathlib import Path

# Asegurar que el directorio backend esté en sys.path independientemente de cómo se invoque pytest
backend_dir = Path(__file__).resolve().parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))
