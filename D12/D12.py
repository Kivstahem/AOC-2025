# Day 12, input: 
# 0: (# is part of the shape . is NOT)
# ###
# ##.
# ##.

# lastly
# 4x4: 0 0 0 0 2 0
# 12x5: 1 0 1 0 2 2
# 12x5: 1 0 1 0 3 2
# (WIDTH) 4x4 (HEIGHT) : 0 of present index[0] 0 of present index[1] 0 of present index[3] 0 of present index[4] 2 of present index[5]



import time
from collections import deque
from functools import lru_cache
starttime = time.time()
debug = False

class shape:    
    def __init__(self, index, grid):
        self.index = index;
        self.grid  = grid;
        self.cells = self.__process_grid(grid);
        self.orientations = self.all_orientations(self.cells)
        self.area  = len(self.cells)
    
    def __process_grid(self, grid):
        cells = set();
        for r, row in enumerate(grid):
            for c, index in enumerate(row):
                if index == "#":
                    cells.add((int(r),int(c)));
        return cells
    
    def normalize(self, cells):
        cells = list(cells)
        if not self.cells:
            print("Why the fuck are you empty?")
        min_r = min(r for r, _ in cells)
        min_c = min(c for _, c in cells)
        return frozenset({(r - min_r, c - min_c) for (r, c) in cells})
    
    #waarschijnlijk kan dit significant efficienter, maar fuck dat
    def rotate_90(self, cells): ## Rotate, 90 degrees to the right 
        return self.normalize((c,-r) for (r,c) in cells)
    
    def rotate_180(self, cells):
        return self.normalize((-r,-c) for (r,c) in cells)

    def rotate_270(self, cells):
        return self.normalize((-c,r) for (r,c) in cells)
    
    def flip_horizontal(self, cells):
        return self.normalize((r,-c) for (r,c) in cells)

    def all_orientations(self,cells):
        cells = self.normalize(cells)
        # dit ziet er uhhhh.... efficient? uit??
        rot_0        = cells;
        rot_90       = self.rotate_90(cells);
        rot_180      = self.rotate_180(cells);
        rot_270      = self.rotate_270(cells);
        flip_rot_0   = self.flip_horizontal(rot_0);
        flip_rot_90  = self.flip_horizontal(rot_90);
        flip_rot_180 = self.flip_horizontal(rot_180);
        flip_rot_270 = self.flip_horizontal(rot_270);
        
        return frozenset({rot_0, rot_90, rot_180, rot_270, flip_rot_0, flip_rot_90, flip_rot_180, flip_rot_270}) # should remove duplicates
        # frozenset added to silence python compiler (set cannot be mutated)
    
    def bark(self):
        print(f"{self.index} is barking")


def load_data(filename):
    class_shapes = []
    shapes = []
    field = []
    filling_shapes = False;
    with open(filename) as file:
        for line in file:
            # if line [0:] -> index               (first entry shapes)
            # ### (or something like that         (append to shapes)
            # empty                               (end shapes)
            # 4x4: 0 1 0 0 0                      (field) [4,4,0,1,0,0,0]
            temp = line.strip().strip(":")
            if len(temp) == 0:
                filling_shapes = False;
                shapes.append(temp_shapes)
            elif len(temp) == 1:
                filling_shapes = True
                temp_shapes = []
            elif temp.__contains__("x"):
                ## FIELD!
                field.append(temp.replace("x", " ").replace(":", " ").split())
            elif filling_shapes:
                temp_shapes.append(temp)   
                
            # all data has been processed, now to use the class to make the shapes nicer
            
        for i in range(len(shapes)):
            temp_shape = shape(i, shapes[i]);
            class_shapes.append(temp_shape);

    return class_shapes, field;

def dancingLinks(field, shapes):
    width  = int(field[0]); 
    height = int(field[1]);
    needed_shapes =[]
    
    for i in range(2,len(field)):
        index = int(field[i]);
        count = i-2;
        # print(i, index, field[i])
        for j in range(int(field[i])):
            needed_shapes.append(shapes[count])
    # print(needed_shapes)
    # now all shapes are loaded in, time to FIT them...
    
    # all inputs are 3x3, so if there are enough full 3x3 squares available the system will fit
    if len(needed_shapes)*9 < width*height:
        # print("It can easily fit")
        return 1
    
    # let's first check if they can actually fit in the square...
    local_area = 0;
    for temp_shape in needed_shapes:
        local_area += temp_shape.area
    if local_area > (width*height): 
        # simplest check, if the cells already exceed the area this CANNOT be a valid implementation
        # print("The area is toooooo large... sorry")
        return 0
    
    # print("Let's run an algorithm")
    return 1 #
    

def main():
    starttime = time.time();
    totalP1 = 0;
    totalP2 = 0;
    filename = "input.txt"; #P1: 485 , P2: ?
    # filename = "input_test.txt"; # P1: 2
    shapes, field = load_data(filename);
    for i in range(len(field)):
        totalP1 += dancingLinks(field[i], shapes);

    print("The total output is P1: ", totalP1, "P2: ", totalP2);
    stoptime = time.time()
    print("Total time:",stoptime-starttime,"seconds");



if __name__=="__main__":
    main()
