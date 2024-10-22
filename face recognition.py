import pygame,sys, os 
from pygame.locals import * 
import cv2 
import face_recognition 
 
pygame.init() 
 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
RED = (255,0,0) 
BLUE = (0,0,255) 
BROWN=(150,75,0) 
 
WINDOWHEIGHT = 750 
WINDOWWIDTH = 750 
 
FONT = pygame.font.SysFont(None, 48) 
 
def terminate(): 
    pygame.quit() 
    sys.exit() 
 
def Menu(): 
    timer = 0 
    color = BLUE 
    switch = False 
    while True: 
        windowSurface.fill(WHITE) 
        Rects = [] 
        Rects.append(pygame.Rect(5, 450, 240, 100)) 
        Rects.append(pygame.Rect(255, 450, 240, 100)) 
        Rects.append(pygame.Rect(505, 450, 240, 100)) 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                terminate() 
            if event.type == KEYDOWN: 
                if event.key == K_ESCAPE: 
                    terminate() 
            if event.type == MOUSEBUTTONDOWN: 
                if Rects[0].collidepoint(pygame.mouse.get_pos()): 
                    Blurtype("FaceBlur") 
                if Rects[1].collidepoint(pygame.mouse.get_pos()): 
                    Blurtype("Shallow") 
                if Rects[2].collidepoint(pygame.mouse.get_pos()): 
                    Blurtype("Deep") 
        for rect in Rects: 
            pygame.draw.rect(windowSurface, BROWN, rect) 
        drawText("Blurring choices", windowSurface, 90, 150, pygame.font.SysFont(None, 112), BROWN) 
        drawText("FaceBlur", windowSurface, 83, 485, FONT , WHITE) 
        drawText("Shallow", windowSurface, 312, 485,FONT , WHITE) 
        drawText("Deep", windowSurface, 580, 485,FONT , WHITE) 
        mainClock.tick(60) 
        timer += 1 
        if timer % 100 == 0: 
            color = BLACK 
        elif timer % 50 == 0: 
            color = BLUE 
        pygame.display.update() 
 
def drawText(text, surface, x, y, font = FONT, color = WHITE): 
    textObject = font.render(text, 1, color) 
    textRect = textObject.get_rect() 
    textRect.topleft = (x,y) 
    surface.blit(textObject, textRect) 
 
mainClock = pygame.time.Clock() 
 
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
 
pygame.display.set_caption("Blurred") 
 
def Blurtype(type1): 
    if(type1 == "FaceBlur"): 
        def face_blur(src_img, dest_img, zoom_in=1): 
             
            ''' 
            Recognize and blur all faces in the source image file, then save as destination image file. 
            ''' 
            sys.stdout.write("%s:processing... \r" % (src_img)) 
            sys.stdout.flush() 
 
            # Initialize some variables 
            face_locations = [] 
            photo = face_recognition.load_image_file(src_img) 
 
            # Resize image to  1/zoom_in size for faster face detection processing 
            small_photo = cv2.resize(photo, (0, 0), fx=1/zoom_in, fy=1/zoom_in) 
 
            # Find all the faces and face encodings in the current frame of video 
            face_locations = face_recognition.face_locations(small_photo, model="cnn") 
 
            if face_locations: 
                print("%s:There are %s faces at " % (src_img, len(face_locations)), face_locations) 
            else: 
                print('%s:There are no any face.' % (src_img)) 
                return False 
             
            #Blur all face 
            photo = cv2.imread(src_img) 
            for top, right, bottom, left in face_locations: 
 
                # Scale back up face locations since the frame we detected in was scaled to 1/zoom_in size 
                top *= zoom_in 
                right *= zoom_in 
                bottom *= zoom_in 
                left *= zoom_in 
 
                # Extract the region of the image that contains the face 
                face_image = photo[top:bottom, left:right] 
 
                # Blur the face image 
                face_image = cv2.GaussianBlur(face_image, (51, 51), 0) 
 
                # Put the blurred face region back into the frame image 
                photo[top:bottom, left:right] = face_image 
 
            #Save image to file 
            cv2.imwrite(dest_img, photo) 
            print('Face blurred photo has been save in %s' % dest_img) 
            return True 
        def blur_all_photo(src_dir, dest_dir): 
            ''' 
            Blur all faces in the source directory photos and copy them to destination directory 
            ''' 
            src_dir = os.path.abspath(src_dir) 
            dest_dir = os.path.abspath(dest_dir) 
            print('Search and blur human faces in %s''s photo.' % src_dir) 
            for root, subdirs, files in os.walk(src_dir): 
                root_relpath = os.path.relpath(root, src_dir) 
                new_root_path = os.path.realpath(os.path.join(dest_dir, root_relpath)) 
                os.makedirs(new_root_path, exist_ok=True) 
                for filename in files: 
                    ext = os.path.splitext(filename)[1] 
                    if ext == '.jpg': 
                        srcfile_path = os.path.join(root, filename) 
                        destfile_path = os.path.join(new_root_path, os.path.basename(filename)) 
                        face_blur(srcfile_path, destfile_path) 
        if __name__ == '__main__': 
            sys.argv = ['faceblur.py', 'C:/Users/Dhananjay Pandey/Desktop/FaceRecog/sample.jpg', 'C:/Users/Dhananjay Pandey/Desktop/FaceRecog/blurred.jpg'] 
            if len(sys.argv) < 2: 
               print('Usage:python faceblur <src-image/src-directory> <dest-image/dest-directory>') 
            else: 
                if os.path.isfile(sys.argv[1]): 
                    face_blur(sys.argv[1], sys.argv[2]) 
                else: 
                    blur_all_photo(sys.argv[1], sys.argv[2]) 
            path='C:/Users/Dhananjay Pandey/Desktop/FaceRecog/blurred.jpg' 
            image=cv2.imread(path) 
            imagef=cv2.resize(image,(1080,720)) 
            cv2.imshow("Blurred image", imagef) 
        terminate() 
    elif(type1 == "Shallow"): 
        path = r'C:/Users/Dhananjay Pandey/Desktop/FaceRecog/sample.jpg' 

 
        # Reading an image in default mode 
        image = cv2.imread(path) 
 
        # Window name in which image is displayed 
        window_name = 'Blurred Image' 
 
        # ksize 
        ksize = (10, 10) 
 
        # Using cv2.blur() method 
        image = cv2.blur(image, ksize) 
        imagef=cv2.resize(image,(1080,720)) 
 
        # Displaying the image 
        cv2.imshow(window_name, imagef) 
        terminate() 
    elif(type1 == "Deep"): 
        path = r'C:/Users/Dhananjay Pandey/Desktop/FaceRecog/sample.jpg' 
 
        # Reading an image in default mode 
        image = cv2.imread(path) 
 
        # Window name in which image is displayed 
        window_name = 'Blurred Image' 
 
        # ksize 
        ksize = (30, 30) 
 
        # Using cv2.blur() method 
        image = cv2.blur(image, ksize) 
        imagef=cv2.resize(image,(1080,720)) 
 
        # Displaying the image 
        cv2.imshow(window_name, imagef) 
        terminate() 
Menu()
