from library.Ship import Ship
import csv
def main() -> None:

 #leemos el archivo
    Barco=[]
    ListaShips=[]
    ListaCruise=[]
    ListaCargo=[]
    with open("ships.csv") as file:
        reader=csv.reader(file)
        for row in reader:
            Barco.append(row)
            if row[2] == '' and row[3] == '': #Si estan vacios los ultimos dos es un Ship
              ListaShips.append(row) #copio datos a listaShip
            if row[2] != '' and row[3] != '':
              ListaCargo.append(row) #copio datos a listaCargo
            if row[2] !='' and row[3]== '':
              ListaCruise.append(row) #copio datos a listacruise






if __name__ == "__main__":
  main()
