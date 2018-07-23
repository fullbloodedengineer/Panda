from panda3d.core import loadPrcFileData

import direct.directbase.DirectStart
from panda3d.core import WindowProperties
from panda3d.core import AmbientLight,PointLight,DirectionalLight
from panda3d.core import TextNode
from panda3d.core import Point3,Vec3,Vec4
from direct.task.Task import Task
from direct.showbase.DirectObject import DirectObject
import sys,os


class FPSCamera(DirectObject):

    def __init__(self):

        self.room = loader.loadModel("models/world")
        self.room.reparentTo(render)
        self.room.setShaderAuto()
        #self.room.setScale(100,100,100)

        self.character = loader.loadModel("assets/characters/knight")
        self.character.reparentTo(render)
        self.character.setPos(0,0,0)

        self.character2 = loader.loadModel("assets/characters/king")
        self.character2.reparentTo(render)
        self.character2.setPos(0,0,0)
        self.character2.setColor((1,0,0,1))

        base.camera.reparentTo(self.character)
        base.camera.setPos(0,-50,5)
        base.camera.lookAt(self.character)

        # Make the mouse invisible, turn off normal mouse controls
        base.disableMouse()
        props = WindowProperties()
        #props.setCursorHidden(True)
        base.win.requestProperties(props)

        # Set the current viewing target
        self.focus = Vec3(0,0,0)
        self.heading = 0
        self.pitch = 0
        self.mousex = 0
        self.mousey = 0
        self.last = 0
        self.keys = {'move forward':False,
                    'move backward':False,
                    'strafe left':False,
                    'strafe right':False,
                    'zoom-out':False}

        # Start the camera control task:
        taskMgr.add(self.controlCamera, "camera-task")
        self.accept("escape", sys.exit, [0])

	#Define a keymap for 'WASD' Movement
        self.accept("w", self.setKeys, ['move forward', True])
        self.accept("w-up", self.setKeys, ['move forward', False])
        self.accept("s", self.setKeys, ['move backward', True])
        self.accept("s-up", self.setKeys, ['move backward', False])
        self.accept("a", self.setKeys, ['strafe left', True])
        self.accept("a-up", self.setKeys, ['strafe left', False])
        self.accept("d", self.setKeys, ['strafe right', True])
        self.accept("d-up", self.setKeys, ['strafe right', False])
        self.accept("q", self.setKeys, ['zoom-out', True])
        self.accept("q-up", self.setKeys, ['zoom-out', False])

        
        # Create some lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection((-5, -5, -5))
        directionalLight.setColor((1, 1, 1, 1))
        directionalLight.setSpecularColor((1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))

    #switch upon which buttons are pressed with if statements 
    def setKeys(self, action, value):
        self.keys[action] = value

    #Use mouse movements to effect direction vector    
    def controlCamera(self, task):
      md = base.win.getPointer(0)
      x = md.getX()
      y = md.getY()
      if base.win.movePointer(0, 100, 100): #Move cursor to know place
        self.heading = self.heading - (x - 100) * 0.2
        self.pitch = self.pitch - (y - 100) * 0.2

      #Confine the pitch movement to 45 degrees from center
      if (self.pitch < -45): self.pitch = -45
      if (self.pitch >  45): self.pitch =  45

      self.character.setHpr(self.heading,self.pitch,0)
      #base.camera.setHpr(self.heading,self.pitch,0)


      elapsed = task.time - self.last
      #dir = base.camera.getMat().getRow3(1)
      dir = self.character.getMat().getRow3(1)
      if (self.last == 0): elapsed = 0

      if (self.keys['zoom-out']):
            base.camera.setY(base.camera.getY()-1)
      #Fwd/Back events, assume +y current at forward
      if (self.keys['move forward']):
        print "Move fwd"
        dir = self.character.getMat().getRow3(1)
        self.focus = self.character.getPos() + dir * elapsed*40 #gives speed
        self.character.setPos(self.focus+dir*.1)

      if (self.keys['move backward']):
        dir = self.character.getMat().getRow3(1)
        self.focus = self.character.getPos() + dir * elapsed*40 #gives speed
        self.character.setPos(self.focus-dir*.1)

      return Task.cont

play = FPSCamera()

run()