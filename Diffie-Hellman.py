q = 353;
a = 3;
xa = 97;
xb = 233;
ya = (a**xa)%q;
yb = (a**xb)%q;
ka = (yb**xa)%q;
kb = (ya**xb)%q;
print(ya);
print(yb);
if(ka==kb):
    print("Key Generated: ");
    print(ka);
else:
    print("Key Exchange Failed");
