class Engine(object)
  init #makes a scene map
  
  def play #sets current scene to opening scene
      while True #forever
      next_scene_name = current_scene.enter()
            print "next scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "map returns new scene", current_scene
            
class Map(object)#how we get from one scene to the next.
#a list of scenes in order
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }
    
    __init__ scene_map
    
    opening_scene  #initial state 
    
    next scene in list, set current to next

  

class Scene(object)
  def enter #prints intro text and exit(1)
  #all text below is included in enter(self)
  
  prompt #how the game leads you to if, elif, else
  
  if, elif, else #way to get to next scene? or way to die ????
  
  where is next scene actually incrementing ?? while??

play()

