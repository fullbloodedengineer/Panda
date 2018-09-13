
class Color:
    def __init__(self,r,g,b):
        self.color = (r,g,b)

    def __str__(self):
        print "Here"
        return "R:%s,G:%s,B:%s" %self.color

    def scale(self,scalar):
        r,g,b = self.color
        return Color(r*scalar,g*scalar,b*scalar)

class ColorMap:
    def __init__(self,minVal,maxVal,**kwargs):
        self.minVal = minVal
        self.maxVal = maxVal
        self.colorMap = []
        self.mapper = None
    
    def returnColor(self,val):
        if not self.mapper:
            assert 0, "No defined map"
        else:
            return self.mapper(self,val)

def SequentialMapper(owner,val):
    color1 = owner.colorMap[0]

    minV = owner.minVal
    maxV = owner.maxVal
    dV = maxV-minV
    if minV < val and val < maxV:
        print "Something in the middle"
        scalar = val / dV    
    elif minV <= val:
        scalar = 0

    elif minV >= val:
        scalar = 1

    else:
        raise ValueError, "Value is not within the given range"

    print "Scalar",scalar
    return color1.scale(scalar)

if __name__ == "__main__":
    color = Color(100,100,100)
    CMap = ColorMap(0.,3000.)
    CMap.mapper = SequentialMapper
    CMap.colorMap = [color]
    print CMap.returnColor(100)

    map(CMap.returnColor,range(3000))
    