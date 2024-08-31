# ---DOCUMENTATION--------------------------------------------------------------
#-------------------------------------------------------------------------------
# Paramore - Brick By Boring Brick ( R3dX PUNKGOESDNB REMIX )
#--------------------------------------------------------------------------------
# > Afficher le suite nes "nb" premiers termes d'une suite u(n+1) = u(n)*q :
#--------------------------------------------------------------------------------
# u(n) est le premier terme
# q est la raison de la suite
# nb sera le nombre de termes à afficher, assimilable au nombre d'itérations
#--------------------------------------------------------------------------------
# hviviane@gmail.com !)
#--------------------------------------------------------------------------------

u0=int(input("premier terme ?"))
r=int(input("raison ?"))
nb=int(input("nombre de termes successifs à afficher ?"))

i=0

suite=""

while i<nb :
    n=u0*r
    u0=n
    i+=1
    suite+=str(n)+"|"

print(suite)