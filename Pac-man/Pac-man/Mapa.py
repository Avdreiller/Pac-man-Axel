from random import randrange
class Mapa(object):
    
    def validar(x, y, cord1, cord2, cord3, cord4, cord5, cord6, cord7, cord8, cord9, cord10, m):
        if m[x+cord1][y+cord2] != '_' and (m[x+cord3][y+cord4] == '_' or m[x+cord5][y+cord6] == '_') and m[x+cord7][y+cord8] == '_' and m[x+cord9][y+cord10] == '_':
            return True
        return False
    
    def validar_Cruces(m, i, j, cord1, cord2, cord3, cord4, cord5, cord6):
        if m[i+cord1][j+cord2]=='#' and ((m[i+cord3][j+cord4]=='#'and m[i+cord5][j+cord6] != '#') or (m[i+cord3][j+cord4]!='#'and m[i+cord5][j+cord6] == '#')):
            if m[i+cord3][j+cord4]=='#':
                x = i+cord5
                y = j+cord6
                contador = 0
                if m[x][y+1]=='#':
                    contador += 1
                if m[x][y-1]=='#':
                    contador += 1
                if m[x+1][y]=='#':
                    contador += 1
                if m[x-1][y]=='#':
                    contador += 1
                if contador >=1:
                    return False
            else:
                x = i+cord3
                y = j+cord4
                contador = 0
                if m[x][y+1]=='#':
                    contador += 1
                if m[x][y-1]=='#':
                    contador += 1
                if m[x+1][y]=='#':
                    contador += 1
                if m[x-1][y]=='#':
                    contador += 1
                if contador >=2:
                    return False
            return True
        return False

    def validar_Cruces2(m, i, j, cord1, cord2, cord3, cord4, cord5, cord6):
        if m[i+cord1][j+cord2]!='#' and ((m[i+cord3][j+cord4]=='#'or m[i+cord5][j+cord6] == '#') or (m[i+cord3][j+cord4]=='#'and m[i+cord5][j+cord6] == '#')):
            return True
        return False

    def generar_Mapa(self):
        
        m =[]
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
                        if ran > 85:
                            if (i > 0 and i < 22) and (j > 0 and j < 22):
                                if m[i+1][j+1] == '_' and m[i-1][j-1] == '_' and m[i+1][j-1] == '_' and m[i-1][j+1] == '_' and m[i][j+1] == '_' and m[i][j-1] == '_' and m[i+1][j] == '_' and m[i-1][j] == '_':
                                    m[i][j] = '#'
                                if self.validar(i,j,0,1,1,1,-1,1,1,0,-1,0,m) or self.validar(i,j,0,-1,-1,-1,1,-1,1,0,-1,0,m) or self.validar(i,j,1,0,1,-1,1,1,0,1,0,-1,m) or self.validar(i,j,-1,0,-1,-1,-1,1,0,1,0,-1,m):
                                    if m[i+1][j+1] == '_' and m[i-1][j-1] == '_' and m[i+1][j-1] == '_' and m[i-1][j+1] == '_':
                                        m[i][j] = '#'
                                    else:
                                        if (m[i][j+1] == "#" or m[i][j-1] == "#") or (m[i][j+1] != "#" and m[i][j-1] != "#") or (m[i+1][j] == "#" or m[i-1][j] == "#") or (m[i+1][j] != "#" and m[i-1][j] != "#"):
                                            if self.validar_Cruces(m,i,j,1,1,1,0,0,1)==True and self.validar_Cruces(m,i,j,-1,-1,-1,0,0,-1)==True and self.validar_Cruces(m,i,j,-1,1,-1,0,0,1)==True and self.validar_Cruces2(m,i,j,1,-1,1,0,0,-1)==True:
                                                m[i][j] = '#'
                                            if self.validar_Cruces(m,i,j,1,1,1,0,0,1)==True and self.validar_Cruces(m,i,j,-1,-1,-1,0,0,-1)==True and self.validar_Cruces2(m,i,j,-1,1,-1,0,0,1)==True and self.validar_Cruces(m,i,j,1,-1,1,0,0,-1)==True:
                                                m[i][j] = '#'
                                            if self.validar_Cruces(m,i,j,1,1,1,0,0,1)==True and self.validar_Cruces2(m,i,j,-1,-1,-1,0,0,-1)==True and self.validar_Cruces(m,i,j,-1,1,-1,0,0,1)==True and self.validar_Cruces(m,i,j,1,-1,1,0,0,-1)==True:
                                                m[i][j] = '#'
                                            if self.validar_Cruces(m,i,j,1,1,1,0,0,1)==True and self.validar_Cruces2(m,i,j,-1,-1,-1,0,0,-1)==True and self.validar_Cruces(m,i,j,-1,1,-1,0,0,1)==True and self.validar_Cruces2(m,i,j,1,-1,1,0,0,-1)==True:
                                                m[i][j] = '#'
                                            if self.validar_Cruces(m,i,j,1,1,1,0,0,1)==True and self.validar_Cruces2(m,i,j,-1,-1,-1,0,0,-1)==True and self.validar_Cruces2(m,i,j,-1,1,-1,0,0,1)==True and self.validar_Cruces(m,i,j,1,-1,1,0,0,-1)==True:
                                                m[i][j] = '#'
                                            if self.validar_Cruces(m,i,j,1,1,1,0,0,1)==True and self.validar_Cruces2(m,i,j,-1,-1,-1,0,0,-1)==True and self.validar_Cruces2(m,i,j,-1,1,-1,0,0,1)==True and self.validar_Cruces2(m,i,j,1,-1,1,0,0,-1)==True:
                                                m[i][j] = '#'
                                            if self.validar_Cruces2(m,i,j,1,1,1,0,0,1)==True and self.validar_Cruces(m,i,j,-1,-1,-1,0,0,-1)==True and self.validar_Cruces(m,i,j,-1,1,-1,0,0,1)==True and self.validar_Cruces(m,i,j,1,-1,1,0,0,-1)==True:
                                                m[i][j] = '#'
                                            if self.validar_Cruces2(m,i,j,1,1,1,0,0,1)==True and self.validar_Cruces(m,i,j,-1,-1,-1,0,0,-1)==True and self.validar_Cruces(m,i,j,-1,1,-1,0,0,1)==True and self.validar_Cruces2(m,i,j,1,-1,1,0,0,-1)==True:
                                                m[i][j] = '#'
                                            if self.validar_Cruces2(m,i,j,1,1,1,0,0,1)==True and self.validar_Cruces(m,i,j,-1,-1,-1,0,0,-1)==True and self.validar_Cruces2(m,i,j,-1,1,-1,0,0,1)==True and self.validar_Cruces(m,i,j,1,-1,1,0,0,-1)==True:
                                                m[i][j] = '#'
                                            if self.validar_Cruces2(m,i,j,1,1,1,0,0,1)==True and self.validar_Cruces(m,i,j,-1,-1,-1,0,0,-1)==True and self.validar_Cruces2(m,i,j,-1,1,-1,0,0,1)==True and self.validar_Cruces2(m,i,j,1,-1,1,0,0,-1)==True:
                                                m[i][j] = '#'
                                            if self.validar_Cruces2(m,i,j,1,1,1,0,0,1)==True and self.validar_Cruces2(m,i,j,-1,-1,-1,0,0,-1)==True and self.validar_Cruces(m,i,j,-1,1,-1,0,0,1)==True and self.validar_Cruces(m,i,j,1,-1,1,0,0,-1)==True:
                                                m[i][j] = '#'
                                            if self.validar_Cruces2(m,i,j,1,1,1,0,0,1)==True and self.validar_Cruces2(m,i,j,-1,-1,-1,0,0,-1)==True and self.validar_Cruces(m,i,j,-1,1,-1,0,0,1)==True and self.validar_Cruces2(m,i,j,1,-1,1,0,0,-1)==True:
                                                m[i][j] = '#'
                                            if self.validar_Cruces2(m,i,j,1,1,1,0,0,1)==True and self.validar_Cruces2(m,i,j,-1,-1,-1,0,0,-1)==True and self.validar_Cruces2(m,i,j,-1,1,-1,0,0,1)==True and self.validar_Cruces(m,i,j,1,-1,1,0,0,-1)==True:
                                                m[i][j] = '#'
                                        
                        if i == 11:
                            m[i][j] = '_'

        archivo_texto.close()
        return m

