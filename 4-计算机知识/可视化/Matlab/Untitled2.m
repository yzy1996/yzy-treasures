n = 200;

x = linspace(0,1.8,n);
y = linspace(-0.2,1.8,n);
[xx, yy]=meshgrid(x,y);
zz = ones(n);
C = zz;


t1 = linspace(0,2,n);
x1 = t1;
y1 = (cos(2 * t1) + 1) / 2;
z1 = cos(4 * t1 - 1) / 2 + sin(t1);

t2 = linspace(0.2,1.8,n);
x2 = t2;
y2 = (cos(2 * t2) + 1) / 2;
z2 = ones(1,n);
p1 = plot3(x1, y1, z1);
p1.LineWidth = 2;
hold on;
p2 = plot3(x2, y2, z2);
p2.LineWidth = 2;
hold on;
s = surf(xx,yy,zz);
s.FaceColor = 'c';
s.EdgeColor = 'none';
s.FaceAlpha = 0.3;
hold on;
p3 = plot3(1.43,0.02,1,'.');
p3.Color = 'black';
p3.MarkerSize = 20;
set(gca,'xtick',[],'xticklabel',[])
set(gca,'ytick',[],'yticklabel',[])
set(gca,'ztick',[],'zticklabel',[])
xlabel('X_{share}','FontSize',16);
text(1.3,0.02,1.2,'A','FontSize',16);
set(gca,'YAxisLocation','origin'); 
