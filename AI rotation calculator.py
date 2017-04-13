Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> vec2 distance = *desiredPosition - position;
float rot = atan2(distance.y, distance.x);
rot = rot * 180.f / PI + 90.f;

if (rot < angle)
{
    angle -= dAngle;
    boat->RotateImage(-dAngle);
}
if (rot > angle)
{
    angle += dAngle;
    boat->RotateImage(dAngle);
}

velocity += vec2(acceleration * cos((angle - 90) * PI / 180.0), acceleration * sin((angle - 90) * PI / 180.0));


How do I ensure it won't rotate in the wrong direction there?


Thanks to Richard Byron (accepted answer below), the problem is fixed. Taking the dot product is better than using degrees.

The final code:
vec2 distance = desiredPosition - position;
normal = vec2(sin((angle - 90) * PI / 180.0), cos((angle - 90) * PI / 180.0) * -1);
float dir = normal.x * distance.x + normal.y * distance.y;

//turn
if (dir > 0)
{
    angle -= dAngle;
    boat->RotateImage(-dAngle);
}
if (dir < 0)
{
    angle += dAngle;
    boat->RotateImage(dAngle);
}

velocity += vec2(acceleration * cos((angle - 90) * PI / 180.0), acceleration * sin((angle - 90) * PI / 180.0));

