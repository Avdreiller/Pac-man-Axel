from random import randrange
def validar(x, y, cord1, cord2, cord3, cord4, cord5, cord6, cord7, cord8, cord9, cord10, m):
    if m[x+cord1][y+cord2] != '_' and (m[x+cord3][y+cord4] == '_' or m[x+cord5][y+cord6] == '_') and m[x+cord7][y+cord8] == '_' and m[x+cord9][y+cord10] == '_':
        return True
def ingresar_nuevodir():
    m = []

    archivo_texto=open("datos/plantilla.txt","r")
    lineas = []
    for line in archivo_texto:
        lineas.append(line)
        
    for x in range(23):
        m.append([])
        for j in range(23):
            m[x].append(lineas[x][j])
    for x in range(15):
        for i in range(23):
            for j in range(23):
                if m[i][j] == '_':
                    ran = randrange(100)
                    if ran > 50:
                        if (i > 0 and i < 22) and (j > 0 and j < 22):
                            if validar(i,j,0,1,1,1,-1,1,1,0,-1,0,m) or validar(i,j,0,-1,-1,-1,1,-1,1,0,-1,0,m) or validar(i,j,1,0,1,-1,1,1,0,1,0,-1,m) or validar(i,j,-1,0,-1,-1,-1,1,0,1,0,-1,m):
                                if m[i+1][j+1] == '_' and m[i-1][j-1] == '_' and m[i+1][j-1] == '_' and m[i-1][j+1] == '_':
                                    m[i][j] = '#'
                    if i == 11:
                        m[i][j] = '_'

        
    cadena = ''
    for i in range(23):
        cadena = ''
        for j in range(23):
            cadena += str(m[i][j])
        print(cadena)
    archivo_texto.close()

ingresar_nuevodir()
