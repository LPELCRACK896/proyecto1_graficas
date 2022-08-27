
class Obj(object):
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.lines = file.read().splitlines()

        self.vertices = []
        self.texcoords = []
        self.normals = []
        self.faces = []
        cont = 1
        for line in self.lines:
            try:
                prefix, value = line.split(' ', 1)
            except:
                continue

            if prefix == 'v': # Vertices
                try:
                    self.vertices.append( list(map(float,value.split(' '))))
                except:
                    rightFormat, list_vertices = self.vert_ln_proccesor(list(map(str, value.split(' '))))
                    if rightFormat and list_vertices:
                        self.vertices.append(list_vertices)

            elif prefix == 'vt':
                self.texcoords.append( list(map(float, value.split(' '))))
            elif prefix == 'vn':
                self.normals.append( list(map(float, value.split(' '))))
            elif prefix == 'f':
                try:
                     self.faces.append([  list(map(int, vert.split('/'))) for vert in value.split(' ')] )
                except:
                    rightFormat, list_faces = self.faces_ln_proccesor([list(map(str, vert.split('/'))) for vert in value.split(' ')])
                    if rightFormat and list_faces:
                        self.faces.append(list_faces)
            cont += 1
    
    def vert_ln_proccesor(self, line):
        newLn = []
        nums = '-0123456789'
        newLn = [float(char) for char in line if len(char)>0 if list(char)[0] in nums]
        return (True, newLn) if len(newLn)==3 else (False, [])            
    def faces_ln_proccesor(self, line):
        fcs = []
        for face in line:
            add = True
            fc = []
            cont = 0
            while add and cont<len(face):
                try:
                    f = int(face[cont])
                    fc.append(f)
                except:
                    add = False
                cont += 1
            
            if add and len(fc)==3:
                fcs.append(fc)    
        
        return (True, fcs) if len(fcs)==4 else (False, [])  
                
            




        
