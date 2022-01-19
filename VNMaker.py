#makes visual novels from any inputted book
class VNCharacter:
    def __init__ (self,name, image, size, width, voice):
        self.name = name
        if size == "small":
            self.imagey = yval//4
        if size == "medium":
            self.imagey = yval//3.5
        if size == "middle":
            self.imagey = yval//3            
        if size == "large":
            self.imagey = yval//2.5
        if size == "giant":
            self.imagey = yval//2   
        self.imagex = int(self.imagey*float(width))
        
        self.image = image
        self.appeared = -1
    def appear(self,spot):
        surf = pygame.transform.scale (pygame.image.load(self.image), (int(self.imagex*2), int(self.imagey*2)))
        win.blit(surf, (xval//7*spot, yval - int(self.imagey*2)))
        self.appeared += 1
    def remove(self,spot):
        onScreen.pop(spot)
        self.appeared = -1