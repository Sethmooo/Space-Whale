import pygame 



class player(object):

    def __init__(self,x,y):

        self.horiz = 0
        self.vert = 0
        self.last_rect = None
        self.rect = pygame.Rect((x,y,50,50)) # Rect takes in the corridnates, we use it in our draw function for the paramenters
        self.direction = [0]
        self.speed = 5
        
    def collisions_test(self):

        from Boundries import stage

        wall = stage()

        current_collisions = []

        wall_list = wall.map()
        for wall in wall_list:
            if self.rect.colliderect(wall.rectangle):
                if self.rect.right > wall.rectangle.left and self.last_rect.right <= wall.rectangle.left:
                    current_collisions.append("right")
                    #print("Hit left side of wall")
                if self.rect.left < wall.rectangle.right and self.last_rect.left >= wall.rectangle.right:
                    current_collisions.append("left")
                    #print("Hit right side of wall")
                if self.rect.bottom > wall.rectangle.top and self.last_rect.bottom <= wall.rectangle.top:
                    current_collisions.append("bottom")
                    #print("Hit top of wall")
                if self.rect.top < wall.rectangle.bottom and self.last_rect.top >= wall.rectangle.bottom:
                    current_collisions.append("top")
                    #print("Hit bottom of wall")
            if current_collisions == None:
                current_collisions.append("none")
        return current_collisions
                

    



    def check_pallet_collisons(self,pallet_list):


        for pallet in pallet_list:

            if self.rect.colliderect(pallet.rect):
                pallet_list.remove(pallet)

   

            
    def moving(self):
        
 
        self.last_rect = self.rect.copy()

        if self.horiz == -1:
            self.rect.x -= self.speed
            if "left" in self.collisions_test():
                self.rect.x = self.last_rect.x
           

        if self.horiz == 1:
            self.rect.x += self.speed 
            if "right"in self.collisions_test():
                self.rect.x = self.last_rect.x
           
          
        if self.vert == -1:
            self.rect.y -= self.speed
            if "top" in self.collisions_test():
                self.rect.y = self.last_rect.y
            
            
        if self.vert == 1:
            self.rect.y += self.speed
            if "bottom" in self.collisions_test():
                self.rect.y = self.last_rect.y
           
            
        key = pygame.key.get_pressed()
        

        if key[pygame.K_LEFT]: 
            self.horiz = -1     # -1 is to the left 
            self.vert = 0    
              # Need to reset or it will keep last vert entered
            

        elif key[pygame.K_RIGHT]:
            self.horiz = 1     # 1 is to the right
            self.vert = 0      # Need to reset
           

        elif key[pygame.K_UP]: 
            self.vert = -1   # -1 is to the top 
            self.horiz = 0
            
        

        elif key[pygame.K_DOWN]:
            self.vert = 1     # 1 is to the bottom 
            self.horiz = 0
          
        
     
        
        
    
    def drawing(self,surface):
        pygame.draw.rect(surface, (255,100,0), self.rect) # This rect draws the player 



        
        



    

        
    
    