#Make a program that reads any angle and shows on the screen the heat of the sine, cosine and tangent of that angle.

import math

ang = float(input('Enter the angle you want: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('The angle of {} has the sine {:.2F}'.format(ang,sen))
print('The angle of {} has the cosine {:.2F}'.format(ang,cos))
print('The angle of {} has the tangent {:.2F}'.format(ang,tan))