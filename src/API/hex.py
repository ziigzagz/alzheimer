import re
hx = "#535353"
hsl = False
def hex_to_rgb(hx, hsl=False):
    if re.compile(r'#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$').match(hx):
        div = 255.0 if hsl else 0
        if len(hx) <= 4:
            return tuple(int(hx[i] * 2, 16) / div if div else
                         int(hx[i] * 2, 16) for i in (1, 2, 3))
        return tuple(int(hx[i:i + 2], 16) / div if div else
                     int(hx[i:i + 2], 16) for i in (1, 3, 5))
    raise ValueError(f'"{hx}" is not a valid HEX code.')

print(hex_to_rgb("#353535"))