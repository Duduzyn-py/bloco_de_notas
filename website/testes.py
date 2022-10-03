
from . import arquivobd
from . import db
from models import User, Note, SharedNote, Friendship, ImageNote, GroupUser, Group
import os

if __name__ == "__main__": # teste da classe
    if os.path.exists(arquivobd): # apagar o arquivo, se houver
        os.remove(arquivobd)
    db.create_all()

    #Usuário
    p1 = User(nome="Cleber Silva", email="cleber@cleber.com", first_name = "Cleber" )           
    db.session.add(p1) 
    db.session.commit() 
    print(p1)

    p2 = User(nome="Airton Silva", email="airton@airton.com", first_name = "Airton" )           
    db.session.add(p1) 
    db.session.commit() 
    print(p1)

    #Nota
    n1 = Note(data = "asdfasdfasdfasdf", user_id = p1)
    db.session.add(n1) 
    db.session.commit() 
    print(n1)

    #Nota por imagem
    in1 = ImageNote(name = "Pássaro", user_id = p1)
    db.session.add(in1) 
    db.session.commit() 
    print(in1)

    #Group
    g1 = Group(name = "Bandeclay Lovers")
    db.session.add(g1) 
    db.session.commit() 
    print(g1)

    #Notas compartilhada
    sn1 = SharedNote(note = n1, destinatario = p2)
    db.session.add(sn1) 
    db.session.commit() 
    print(sn1)

    #Amizade
    f1 = Friendship(user = p1, user_id = p2)
    db.session.add(f1) 
    db.session.commit() 
    print(f1)
