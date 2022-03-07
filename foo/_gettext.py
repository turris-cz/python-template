import gettext
import pathlib

_ = gettext.translation("foo", pathlib.Path(__file__).parent / "locale", fallback=True).gettext
