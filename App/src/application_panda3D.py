#Panda3D Modules
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor

#Personnal Modules
from application import Application

print("Balise : fichier panda")

class Panda(ShowBase):
    print("Balise : classe panda")
    def __init__(self):
        ShowBase.__init__(self)

        # Load Panda3D Scene
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(8, 42, 0)

        # Load Panda3D actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.06, 0.06, 0.06)
        self.pandaActor.reparentTo(self.render)

        # Loop its animation.
        self.pandaActor.loop("walk")


#Main Guard (temporary)
if __name__ == "__main__":
    panda_instance = Panda()
    panda_instance.run()
