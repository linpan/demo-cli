
class ConstrainedUsername(ConstrainedStr):
    min_length = 3
    max_length = 64
    regex = re.compile(r"^[A-Za-z0-9-_.]+$")
    to_lower = True
    strip_whitespace = True