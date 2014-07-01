G21 ; set units to millimeters
M107
M104 P30 ; set temperature
G28 ; home all axes
G90 ; use absolute coordinates
G1 
G0 Z0.500 
G0 X1.011 Y1.015 
G1 X1.073 Y1.076  
G1 X2.048 Y1.014 
G1 X2.061 Y1.068 
G1 X7.039 Y1.068 
G1 X7.045 Y1.065 
G1 X8.085 Y1.011 
G1 X8.024 Y1.073 
G1 X8.086 Y2.048 
G1 X8.032 Y2.061 
G1 X8.032 Y7.039 
G1 X8.035 Y7.045 
G1 X8.089 Y8.085 
G1 X8.027 Y8.024 
G1 X7.052 Y8.086 
G1 X7.039 Y8.032 
G1 X2.061 Y8.032 
G1 X2.055 Y8.035 
G1 X1.015 Y8.089 
G1 X1.076 Y8.027 
G1 X1.014 Y7.052 
G1 X1.068 Y7.039 
G1 X1.068 Y2.061 
G1 X1.065 Y2.055 
G1 X1.074 Y1.080 
G0 X2.089 Y2.089 
G1 X2.075 Y2.068
G1 X7.025 Y2.068 
G1 X7.011 Y2.089 
G1 X7.032 Y2.075 
G1 X7.032 Y7.025 
G1 X7.011 Y7.011 
G1 X7.025 Y7.032 
G1 X2.075 Y7.032 
G1 X2.089 Y7.011 
G1 X2.068 Y7.025 
G1 X2.068 Y2.075 
G1 X2.089 Y2.089 
G28 X0  ; home X axis
M84     ; disable motors
