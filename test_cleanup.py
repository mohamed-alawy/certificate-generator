import sys, types
# Stub eventlet so tests can import app without installing eventlet
sys.modules['eventlet'] = types.SimpleNamespace(monkey_patch=lambda: None)

# Minimal stub for flask (used at import-time in app.py)
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

flask = types.SimpleNamespace(
    Flask=DummyFlask,
    render_template=lambda *a, **k: '',
    jsonify=lambda *a, **k: {},
    request=types.SimpleNamespace()
)
sys.modules['flask'] = flask

# Minimal stub for flask_socketio
class DummySocketIO:
    def __init__(self, *a, **k):
        pass
    def emit(self, *a, **k):
        return None
    def on(self, *args, **k):
        def decorator(f):
            return f
        return decorator

flask_socketio = types.SimpleNamespace(SocketIO=DummySocketIO, emit=lambda *a, **k: None)
sys.modules['flask_socketio'] = flask_socketio

from app import clean_name


def test_remove_sheikh_full_forms():
    # Feminine forms should be removed entirely (not leave 'ه' or 'ة')
    assert clean_name('شيخه محمد') == 'محمد'
    assert clean_name('شيخة محمد') == 'محمد'
    assert clean_name('محمد شيخه') == 'محمد'
    assert clean_name('محمد شيخة') == 'محمد'


def test_remove_sheikh_male_form():
    assert clean_name('شيخ محمد') == 'محمد'
    assert clean_name('الشيخ محمد') == 'محمد'


def test_sheikh_punctuation_and_embedded():
    # Slash near start should be trimmed and title removed
    assert clean_name('شيخه/محمد') == 'محمد'
    assert clean_name('/شيخه محمد') == 'محمد'
    # Should not remove 'شيخ' when it's part of a larger name like 'عبدالشيخ'
    assert clean_name('عبدالشيخ احمد') == 'عبدالشيخ احمد'


def test_single_letter_tokens():
    # Arabic single-letter prefix/suffix
    assert clean_name('د دعاء حبيب') == 'دعاء حبيب'
    assert clean_name('د. دعاء حبيب') == 'دعاء حبيب'
    assert clean_name('و محمود') == 'محمود'
    # Latin single-letter cases
    assert clean_name('A John Doe') == 'John Doe'
    assert clean_name('John D') == 'John'


if __name__ == '__main__':
    # Simple runner for manual checks
    for fn in [test_remove_sheikh_full_forms, test_remove_sheikh_male_form, test_sheikh_punctuation_and_embedded, test_single_letter_tokens]:
        try:
            fn()
            print(f"OK: {fn.__name__}")
        except AssertionError as e:
            print(f"FAIL: {fn.__name__}")
            raise
