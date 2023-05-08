% x =0.1:0.01:1;
% y = 0.1:0.01:1;
% [xx,yy]=meshgrid(x,y);
% z = 1 ./ (xx .* yy);
% 
% surf(x,y,z)

t = 1:0.01:3;
x1 = sin(t);
y1 = cos(t);
z1 = sin(t) + cos(t);

x2 = sin(t);
y2 = cos(t);
z2 = 0.5 * t ./ t;
plot3(x1, y1, z1);
hold on;
plot3(x2, y2, z2);