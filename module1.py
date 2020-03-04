#coding:utf-8


# lire à partir d'un fichier text
fic= open("docs/donnees.txt","r")

nbEtud=0
nbAdmi=0
nbAdmiDette=0
nbAjourne=0
meilleureMoy=0
mauvaiseMoy=20
listeEtud = []
tab = []


for ligne in fic:
    tab.append(ligne)

for line in tab:

    listeEtud.append(line)
    print(listeEtud)

# creer un fichier html
fic2= open('tp.html','w')
fic2.write('''
            <html>
             <head>
                <title>tp python</title>
                <meta charset="utf-8"/>
              </head>
              <body>
               <table border="solid">
               <tr>
                <th>Nom</th>
                <th>Prenom</th>
                <th>Matricule</th>
                <th>S1</th>
                <th>S2</th>
                <th>Moyenne</th>
                <th>Cridet1</th>
                <th>Cridet2</th>
                <th>Unite_acuise </th>
                <th>resultat</th>
               </tr>''')
for e in listeEtud:
     #calculer le nb des etudiants:
        nbEtud=nbEtud+1

for li in listeEtud:
        a=li.replace(",","")
        b=a.split()
        fic2.write ( '<tr>' )
        fic2.write ( '<td>' )
        fic2.write ( str(b[0]))
        fic2.write ('</td>')
        fic2.write ( '<td>' )
        fic2.write ( str(b[1]))
        fic2.write ('</td>')
        fic2.write ( '<td>' )
        fic2.write ( str(b[2]))
        fic2.write ('</td>')
        fic2.write ( '<td>' )
        fic2.write ( str(b[3]))
        fic2.write ('</td>')
        fic2.write ( '<td>' )
        fic2.write ( str(b[4]))
        fic2.write ('</td>')
        fic2.write ( '<td>' )
        fic2.write ( str(b[5]))
        fic2.write ('</td>')
        fic2.write ( '<td>' )
        fic2.write ( str(b[6]))
        fic2.write ('</td>')
        fic2.write ( '<td>' )
        fic2.write ( str(b[7]))
        fic2.write ('</td>')
        fic2.write ( '<td>' )
        fic2.write ( str(b[8]))
        fic2.write ('</td>')
    # la meilleure et la mauvaise moyenne:
        if meilleureMoy >= float(b[5]):
              meilleureMoy = meilleureMoy
        else:

             meilleureMoy = float(b[5])

        if mauvaiseMoy>= float (b[5]):
            mauvaiseMoy= float(b[5])
        else:
            mauvaiseMoy=mauvaiseMoy




   # le résultat de l'années:
        if float (b[3]) >=10 and float (b[4]) >=10:
            nbAdmi  =nbAdmi+1
            fic2.write ( "<td>" )
            fic2.write ( "Admi" )
            fic2.write ( "</td>" )

        elif (float(b[6]) + float (b[7])) >=45:
          nbAdmiDette= nbAdmiDette+1
          fic2.write('<td>')
          fic2.write("admi avc dette")
          fic2.write('</td>')

        else:
          nbAjourne=nbAjourne+1
          fic2.write('<td>')
          fic2.write("ajournee")
          fic2.write('</td>')




fic2.write('</tr>')


fic2.write('</table>')

fic2.write('<p> la meilleure moyenne:'+str(meilleureMoy)+'</p>')
fic2.write('<p> la mauvaise moyenne:'+str(mauvaiseMoy)+'</p> ')
#les statistiques:
fic2.write('<p> les statistiques:</p>')
prcAdmi=(100 * nbAdmi ) / nbEtud
fic2.write('<p>le nombre des admis:'+str(nbAdmi)+'   et le pourcentage des admis:'+str(prcAdmi)+'%</p>')
prcAdmiDette=(100 * nbAdmiDette ) / nbEtud
fic2.write('<p> le nombre des admis par dettes:'+str(nbAdmiDette)+ 'et le pourcentage des admis par dettes:'
+str(prcAdmiDette)+'%</p>')
prcAjourne=(100 * nbAjourne ) / nbEtud
fic2.write('<p> le nombre des ajourne:'+str(nbAjourne)+ ' et le pourcentage des ajourne:'+str(prcAjourne)+'%</p>')
fic2.write('</body></html>')

fic.close()
fic2.close()