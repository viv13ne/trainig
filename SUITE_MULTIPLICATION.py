# ---DOCUMENTATION--------------------------------------------------------------
#-------------------------------------------------------------------------------
# Paramore - Brick By Boring Brick ( R3dX PUNKGOESDNB REMIX )
#--------------------------------------------------------------------------------
# > Afficher la suite nes "nb" premiers termes d'une suite u(n+1) = u(n)*q :
#--------------------------------------------------------------------------------
# u(n) est le premier terme
# u(n+1) est le terme qui va directement suivre le terme u(n)
# q est la raison de la suite
# nb sera le nombre de termes à affiche = le nombre d'itérations
#--------------------------------------------------------------------------------
# hviviane@gmail.com !)
#--------------------------------------------------------------------------------
# Merci
#--------------------------------------------------------------------------------

u0=int(input("premier terme ?"))
r=int(input("raison ?"))
nb=int(input("nombre de termes successifs à afficher ?"))

i=0
somme=0
suite=""

while i<nb :
    n=u0*r
    somme+=n
    u0=n
    i+=1
    suite+=str(n)+"|"

print(f"{suite} > Somme des {nb} premiers termes = {somme}")
