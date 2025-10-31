
import pygame


class stage(object):

    def __init__(self):
       
        self.rectangle = pygame.Rect(500,500,10,10)

    def draw(self,surface):
        pygame.draw.rect(surface,(255,255,255),self.rectangle)
    

    def map(self):

        wall_list = []

        with open("obstacle.txt", "r") as row:
            lines = row.readlines()
        
        for row_index, line in enumerate(lines):
            for col_index, char in enumerate(line.strip()):
                

                wall = stage()

                x = col_index * 10
                y = row_index  * 10

                wall.rectangle.x = x
                wall.rectangle.y = y

                if char == "1":
                    wall_list.append(wall)
            
        return wall_list
        
class collectables(object):
    def __init__(self,x,y,radius):
       
       self.x = x

       self.y = y

       self.radius = radius

       self.rect = pygame.Rect(self.x,self.y,6,6)
       
    
    def draw(self,surface):
        pygame.draw.rect(surface,(0,0,0),self.rect)
        pygame.draw.circle(surface,(255,0,255),(self.x,self.y),self.radius)
        

    
    def pallet_map(self):

        

        pallet_list = []


        with open("obstacle.txt", "r") as row:
            lines = row.readlines()
        
        for row_index, line in enumerate(lines):
            for col_index, char in enumerate(line.strip()):

                pallets = collectables(col_index * 10 ,row_index * 10 ,8)

                if char == "2":
                    pallet_list.append(pallets)
                    
                
        return pallet_list
   

                




        







        