import sys, types, os

# Ensure project root is in sys.path so 'app' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Stubs so we can import app without installing all deps
sys.modules['eventlet'] = types.SimpleNamespace(monkey_patch=lambda: None)
class DummyFlask:
    def __init__(self, *a, **k):
        self.config = {}
    def route(self, *a, **k):
        def decorator(f):
            return f
        return decorator
    def before_first_request(self, *a, **k):
        def decorator(f):
            return f
        return decorator
    def run(self, *a, **k):
        return None
sys.modules['flask'] = types.SimpleNamespace(Flask=DummyFlask, render_template=lambda *a, **k: '', jsonify=lambda *a, **k: {}, request=types.SimpleNamespace())
class DummySocketIO:
    def __init__(self, *a, **k):
        pass
    def emit(self, *a, **k):
        return None
    def on(self, *args, **k):
        def decorator(f):
            return f
        return decorator
sys.modules['flask_socketio'] = types.SimpleNamespace(SocketIO=DummySocketIO, emit=lambda *a, **k: None)

from app import clean_name

cases = [
    'دعاء حبيب المحمد',
    'د دعاء حبيب المحمد',
    'عاء حبيب المحم',
    'و محمود خلاه محو',
    'عهود خالد خلاها خال'
]

for s in cases:
    print(f"{s!r} -> {clean_name(s)!r}")
