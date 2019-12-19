import os
import biblioteca
import libro
nombre_bibli=os.sys.argv[1]
autor_lib=os.sys.argv[2]
al=libro.Libro(autor_lib,"tornado",250,"1kg","140pag")
nb=biblioteca.Biblioteca(nombre_bibli,al,20,40,10)
print("la biblioteca se llama:"+nb.getNombre())
print("el autor es:"+al.getAutor())
nb.setLibro(al)
print(nb.investigar())