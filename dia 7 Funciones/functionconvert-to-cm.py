def convert_to_cm(mi=0, yd=0, ft=0, inc=0):
    """Transforma valores del sistema imperial a centimetros."""
    cm = 2.54
    inc_to_cm = inc * cm
    ft_to_cm = ft * 12 * cm
    yd_to_cm = yd * 3 * 12 * cm
    mi_to_cm = mi * 1760 * 3 * 12 * cm
    total = inc_to_cm +ft_to_cm + yd_to_cm +mi_to_cm
    return total

result = convert_to_cm(yd=4,ft=7)
print(result)