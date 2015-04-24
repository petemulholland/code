from building import Building, BuildingLayer, BuildingBlock, CompositeBuilding, Torch
from base.rooms import *
from base.enclosure import *
import mcpi.block as block
from mcpi.block import Block
from mcpi.vec3 import Vec3

# castle ground floor plan
# 
#sssssssgsssgsssgsssgssssssss 8
#swwwwww www www www wwwwwwws 7
#sw                        ws 6
#sw                        ws 5
#swff     c c c c c      ffws 4
#swff    ttttttttttt     ffws 3
#swff   ctttttttttttc    ffws 2
#swff    ttttttttttt     ffws 1
#sw       c c c c c        ws 02
#sw                        ws 9
#sw                        ws 8
#swwwwdwwwddwwwwwwddwwwwwwwws 7
#sssss sss  ssssss  sssssssss 6
#d          xxwwxx          d 5
#sssss ss   xxwwxx   ssssssss 4
#s      s     xx     s      s 3
#s      s     xx     s      s 2 
#s            xx            s 1
#s            xx            s 01
#s      s            s      s 9
#s      s            s      s 8
#sss  sss   p    p   sss  sss 7
#s      s            s      s 6
#s      s            s      s 5
#s                          s 4
#s                          s 3
#s      s            s      s 2 
#s      s    sdds    s      s 1
#sssssssssssss  sssssssssssss 0

#7654321098765432109876543210
#       2         1          

class Castle(CompositeBuilding):
	# * all levels 4 spaces high (need 5 for smelting room)
	# Ground floor:
	#	   main stairs
	#      dining hall at back,
	#      kitchen & pantry on one side
	#      smithy & enchanting room on other side.
	#      hallway to back/side door on smithy side
	#      Mine entrance room somewhere, stairs to base ment under main stairs
	#
	# first story
	# - master bedroom
	#      - Penthouse on roof to overlook walls.
	#      - 2 beds surrounded by fence posts with pressure plates & carpet on top for 4 poster
	#      - chest at end of bed
	#           => 4x4 area for bed + 2 minimum all round
	#      - fireplace
	# - store room (non food)
	#      - Sell-able stuff (near door, beside armory)
	#           - wheat, potato, carrots
	#           - string, coal, wool, 
	#           - paper, books
	#           - rotten meat
	#           - raw pork, raw chicken
	#           - leather.
	#      - building material
	# - crafting room, close to store
	# - smelting room -  will need to be 5 high
	# - brewery
	# - dye room
	# basement
	#	target practice room
	#	corridor
	#	mushroom farm
	#	portal room
	#	mine access
	#	mobtrap access
	#
	# oak wood rafters on ceilings & columns in atrium at start of stairs
	# for realism extend into walls, will need to add butresses on outer walls to shield beam ends
	# need to plan beam & column placement on all floors including basement & upper floor,
	# and then figure out butresses on outer wall
	# 
	# TODO: Update composite build with ordered list of collections 
	#		so that upper floor can be built before rooms upstairs
	#		draft build order:
	#		castle walls 
	#		floor (stone bricks)
	#		ground floor rooms
	#		corner turrets
	#		any remaining walls, windows & doors
	#		2nd floor floor
	#		main stairs & balcony
	#		2nd floor rooms
	#		corner turrets
	#		any remaining walls & windows
	#		balconys & doors
	#		rafters & support beams
	#		roof
	#		basement, stairs, corridor, mushroom farm, target practice, portal, mine access & mob farm access

							




	pass

class CastelEnclosure(CompositeBuilding):
	 #* well(s)

	 #* crop farm x4 - 2 wheat, 1 potato 1 carrot
	 #     - make plot sizes 8x7, with 7x dispensers - will need to work on surrounding automation for this.
	 #          - but could put the dispensers on the bottom easing automation
	 #          - could use redstone torches underneath dispensers & lever with power on normally
	 #     - this will run to 8x19 x 2
	 #* sugar cane farm x2 (10x9 for 1 plot)
	 #* pumpkin/melon farm - need to investigate designs.
	 #     http://minecraft.gamepedia.com/Tutorials/Pumpkin_and_melon_farming
	 #     check out semi automatic stackable design #7
	 #* mushroom farm - can go under other farms. (20x25 working well - although some mobs spawn inside)

	 #* Animal pens (make fences 2 high with double gates in 1 corner (animals are escaping from stiles in current designs)
	 #     - pens sizes (current = 9x8, maybe go to 10x10)
	 #     - cows, sheep, pigs, chickens
	 #     - could use leads to keep animals in pens.
	 #     - probably want a paddock area for horses too (horses can walk through non solid blocks so maybe just a stables)
	 #* stables - need to work on designs
	 #     - individual stalls & hay inside?
	 #     https://www.pinterest.com/mustanglani/minecraft-barns/
	 #     https://www.google.ie/search?q=minecraft+stable+blueprint&sa=X&biw=1920&bih=958&tbm=isch&tbo=u&source=univ&ei=M9g0Vd3UIoLW7AbXsYHQDA&ved=0CCAQsAQ
	 #     http://www.minecraftforum.net/forums/show-your-creation/screenshots/1588012-howto-build-a-barn (17x17 design, might no need such a high roof (try half slab steps for roof)
	 #* kennels - need to work on designs.
	 #     - think i read a dog bed design - 2 half slabs, with carpet on top & surrounded by signs.
	 #     http://mp3loot.ninja/index.php?q=20+wolf+dog+house+kennel+ideas+and+designs+minecraft&type=video&view=696d525161544e53795838

	 #* pond?

	pass
