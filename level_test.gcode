G21 ; set units to millimeters
M107
M104 P30 ; set temperature
G28 ; home all axes
M109 P30 ; wait for temperature to be reached
G90 ; use absolute coordinates

G1 F1800.000 A-1.00000
G0 Z0.500 F7800.000
G0 X467.065 Y221.255 F7800.000
G1 A0.00000 F1800.000
G1 X468.211 Y219.215 A0.14774 F1080.000
G1 X469.973 Y217.676 A0.29548
G1 X472.148 Y216.814 A0.44322
G1 X473.561 Y216.668 A0.53290
G1 X526.439 Y216.668 A3.87195
G1 X528.745 Y217.065 A4.01970
G1 X530.785 Y218.211 A4.16744
G1 X532.324 Y219.973 A4.31518
G1 X533.186 Y222.148 A4.46292
G1 X533.332 Y223.561 A4.55260
G1 X533.332 Y276.439 A7.89165
G1 X532.935 Y278.745 A8.03939
G1 X531.789 Y280.785 A8.18713
G1 X530.027 Y282.324 A8.33488
G1 X527.852 Y283.186 A8.48262
G1 X526.439 Y283.332 A8.57230
G1 X473.561 Y283.332 A11.91135
G1 X471.255 Y282.935 A12.05909
G1 X469.215 Y281.789 A12.20683
G1 X467.676 Y280.027 A12.35457
G1 X466.814 Y277.852 A12.50231
G1 X466.668 Y276.439 A12.59199
G1 X466.668 Y223.561 A15.93105
G1 X467.052 Y221.329 A16.07405
G1 F1800.000 A15.07405
G0 X474.389 Y224.389 F7800.000
G1 A16.07405 F1800.000
G1 X474.975 Y224.268 A16.11183 F378.000
G1 X525.025 Y224.268 A19.27228
G1 X525.611 Y224.389 A19.31005
G1 X525.732 Y224.975 A19.34783
G1 X525.732 Y275.025 A22.50828
G1 X525.611 Y275.611 A22.54605
G1 X525.025 Y275.732 A22.58383
G1 X474.975 Y275.732 A25.74428
G1 X474.389 Y275.611 A25.78206
G1 X474.268 Y275.025 A25.81983
G1 X474.268 Y224.975 A28.98028
G1 X474.389 Y224.389 A29.01806
G1 F1800.000 A28.01806
M104 S0 ; turn off temperature
G28 X0  ; home X axis
M84     ; disable motors