
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
                    print("Fallo")
                    newFces = self.face_ln_proccesor([  list(map(str, vert.split('/'))) for vert in value.split(' ') if not vert==''] )
                    if len(newFces): self.faces.append(newFces)
                    
            cont += 1
    
    def vert_ln_proccesor(self, line):
        newLn = []
        nums = '-0123456789'
        newLn = [char for char in line if len(char)>0 if list(char)[0] in nums]
        return (True, newLn) if len(newLn)==3 else (False, [])            
    
    def face_ln_proccesor(self, line):
        newLine = []
        for face in line:
            add = len(face)==3
            cont = 0
            int_face = []
            while add and cont<len(face):
                try:
                    int_face.append(int(face[cont]))
                except:
                    add = False
                cont += 1
            if add: newLine.append(int_face)
        return newLine         
            




        
