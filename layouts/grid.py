#!/usr/bin/env python

spacing = 0.11 # m
grid_size = 11 #

lines = []
for c in range(-(grid_size-2)/2, (grid_size+2)/2):
    rs = [reversed(range(grid_size)), range(grid_size)][c % 2]
    for r in rs:
        lines.append('  {"point": [%.2f, %.2f, %.2f]}' %
                     (c*spacing, 0, (r-grid_size/2)*spacing))
print '[\n' + ',\n'.join(lines) + '\n]'
