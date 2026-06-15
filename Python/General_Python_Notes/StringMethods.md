| Method         | Purpose                      | Example                    | Output          |
| -------------- | ---------------------------- | -------------------------- | --------------- |
| `lower()`      | Convert to lowercase         | `"HeLLo".lower()`          | `"hello"`       |
| `upper()`      | Convert to uppercase         | `"hello".upper()`          | `"HELLO"`       |
| `strip()`      | Remove spaces from both ends | `" hi ".strip()`           | `"hi"`          |
| `lstrip()`     | Remove left spaces           | `" hi".lstrip()`           | `"hi"`          |
| `rstrip()`     | Remove right spaces          | `"hi ".rstrip()`           | `"hi"`          |
| `split()`      | Split into list              | `"a,b,c".split(",")`       | `['a','b','c']` |
| `join()`       | Join iterable into string    | `"-".join(['a','b'])`      | `"a-b"`         |
| `replace()`    | Replace substring            | `"abc".replace("a","x")`   | `"xbc"`         |
| `find()`       | First index, `-1` if absent  | `"hello".find("l")`        | `2`             |
| `index()`      | First index, error if absent | `"hello".index("l")`       | `2`             |
| `count()`      | Count occurrences            | `"banana".count("a")`      | `3`             |
| `startswith()` | Check prefix                 | `"hello".startswith("he")` | `True`          |
| `endswith()`   | Check suffix                 | `"hello".endswith("lo")`   | `True`          |
| `isalpha()`    | All letters?                 | `"abc".isalpha()`          | `True`          |
| `isdigit()`    | All digits?                  | `"123".isdigit()`          | `True`          |
| `isalnum()`    | Letters or digits?           | `"abc123".isalnum()`       | `True`          |
| `isspace()`    | All spaces?                  | `"   ".isspace()`          | `True`          |
| `capitalize()` | First letter uppercase       | `"hello".capitalize()`     | `"Hello"`       |
| `title()`      | Capitalize each word         | `"hello world".title()`    | `"Hello World"` |
| `swapcase()`   | Reverse case                 | `"HeLLo".swapcase()`       | `"hEllO"`       |
| `zfill()`      | Pad with leading zeros       | `"42".zfill(5)`            | `"00042"`       |
