def split(ip, sep, start):
    lines = ip.split(sep)
    return lines[start : len(lines) : 1]
