import sqlite3

from Filtros  import OpcionesDeFiltro

class Genero:
    def __init__(
        self,
        genero_id=None,
        name=None,
        is_active=1
    ):
        self.genero_id = genero_id
        self.name = name
        self.is_active = is_active

    def __getitem__(self, key):
        return getattr(self, key)

class Nodegenero:
    def __init__(self, data = None, prev = None, next = None):
        self.data: Genero = data
        self.prev: Nodegenero = prev
        self.next: Nodegenero = next

class Listgenero:
    def __init__(self):
        self.list: Nodegenero = None

    def getList(self):
        return self.list

    def getByFilter(self, filters):
        filteredData = Listgenero()

        tempList = self.list
        count = 0

        while(True):
            validations = []

            for filter in filters:
                if (filter.exact == True):
                    validations.append(filter.value == tempList.data[filter.key])
                else:
                    validations.append(filter.value.lower() in tempList.data[filter.key].lower())

            if (False not in validations):
                tempList.data.pos = count
                filteredData.insert(tempList.data)

            if (tempList == None or tempList.next is None):
                break
            else:
                count += 1
                tempList = tempList.next

        return filteredData

    def insert(self, data: Genero):
        def insertValue(tempList: Nodegenero):
            if (tempList is None):
                newList = Nodegenero(data)
                return newList
            if (tempList.next is None):
                newList = Nodegenero(data, tempList)
                tempList.next = newList
                return tempList
            else:
                tempList.next = insertValue(tempList.next)
                return tempList

        self.list = insertValue(self.list)

    def update(self, pos: int, data: Genero):
        def updateValue(tempList: Nodegenero, tempPos: int):
            if (tempList is None):
                return tempList
            else:
                if (tempPos == pos):
                    tempList.data = data
                    return tempList
                else:
                    tempList.next = updateValue(tempList.next, tempPos + 1)
                    return tempList

    def delete(self, pos: int):
        def deleteValue(tempList: Nodegenero, tempPos: int):
            if (tempList is None):
                return tempList
            else:
                if (tempPos == pos):
                    if (tempList.prev == None):
                        newList = tempList.next
                        newList.prev = None

                        return newList
                    else:
                        newList = tempList.next
                        newList.prev = tempList.prev
                        
                        return newList
                elif (tempPos + 1 == pos and tempList.next.next == None):
                    tempList.next = None

                    return tempList
                else:
                    tempList.next = deleteValue(tempList.next, tempPos + 1)
                    return tempList

        self.list = deleteValue(self.list, 0)

class generosModel:
    def __init__(self):
        self.table = 'genero'
        self.database = 'cinema.db'

    def getAll(self):
        # create DB connection
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        try:
            result = cursor.execute(f'SELECT * FROM ' + self.table).fetchall()

            if (result):
                conn.close()
                data = []

                for i, row in enumerate(result):
                    data.insert(i, Genero(row[0], row[1], row[2]))

                return data
            else:
                conn.close()
                return []
        except:
            conn.close()
            return []

    def create(self, user: Genero):
        # create DB connection
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        try:
            result = cursor.execute('INSERT INTO ' + self.table + ' (' + ('genero_id, ' if user.genero_id != None else '') + 'name, is_active) VALUES (' + (':genero_id, ' if user.genero_id != None else '') + ':name, :is_active)',  {'genero_id': user.genero_id, 'name': user.name, 'is_active': user.is_active})
            conn.commit()
            
            if (result):
                return True
            else:
                conn.close()
                return None
        except:
            conn.close()
            return None
    
    def deleteAll(self):
        # create DB connection
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        try:
            result = cursor.execute('DELETE FROM ' + self.table + ' WHERE 1 = 1')
            conn.commit()
            
            if (result):
                return True
            else:
                conn.close()
                return None
        except:
            conn.close()
            return None
