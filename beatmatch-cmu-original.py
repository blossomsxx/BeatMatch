#consol instructions
print('pay attention to the beats (purple circles) falling down.')
print('press the corresponding keys a, s, k, and l and match them with the corresponding targets.')
print('if you hit the corresponding target, your hit counter will go up. If you miss, you miss counter will go up.')
print('to win, get at least 50 hits. You will love the game if you get more than 30 misses.')

app.background = 'skyBlue'

#background
Group (Circle(51,400,175,fill = 'steelBlue'), Circle(400,400,200,fill ='steelBlue'), Circle(167,374,100,fill ='steelBlue'), Circle(215,330,100,fill='steelBlue'))

#beat interface
beats = Group()

#for loop to make lines
for i in range (3):
    x = 100  + 100 * i
    lines = Group (Line(x,0,x,400, fill = 'white'))
    

#declares target variables and brings them to the front
target1 = Circle(50,300, 20 , fill = 'darkSlateBlue')
target2 = Circle(150,300, 20 , fill = 'darkSlateBlue')
target3 = Circle(250,300, 20 , fill = 'darkSlateBlue')
target4 = Circle(350,300, 20 , fill = 'darkSlateBlue')
target1.toFront()
target2.toFront()
target3.toFront()
target4.toFront()

#defnes custom createBeats function
def createBeats(x):
    if len(beats.children) < 20:
        beat = Circle(x,0,15, fill = 'slateBlue')
        beats.add(beat)
    beats.toFront()

#defines custom function game over
def gameOver():
    app.background = 'black'
    Label('Game Over', 200,200, fill = 'white', size = 80)
    app.stop()

#defines custom function win game
def winGame():
    app.background = 'green'
    Label('CONGRATS! You Won!', 200,200, fill = 'white', size = 80)
    app.stop()

#generates random number
import random
app.random = random.randrange(0,5)

app.number = 0
#defines onStep to move beats down
def onStep():
    
    #slows down the number generator
    app.number += 1
    if (app.number % 5 == 0):
        app.random = randrange(0,5)
    

    #creates different beats based off the random number generated
    if app.random == 0:
        createBeats(50)
    if app.random == 1:
        createBeats(150)
    if app.random == 2:
        createBeats(250)
    if app.random == 3:
        createBeats(350)
    if app.random == 4:
        createBeats(50)
        createBeats(350)

    #moves the beats down and removes the shape when it hits the bottom
    for beat in beats.children:
        beats.dy = 5
        beat.centerY+=beats.dy
        
        if beat.top>=400:
            beats.remove(beat)
    
    #stops the game when you hit your goal of 50 targets
    if(app.counter>=30):
        gameOver()
        app.stop()
    elif(app.hit>=50):
        winGame()
        app.stop()
    


#defines missCounter custom function to print how many misses and hits you have
#same with hitCounter
app.counter = 0
app.hit = 0
def missCounter():
    app.counter += 1
    print("miss")
    print(app.counter)

def hitCounter():
    app.hit += 1
    print('hit')
    print(app.hit)

#checks if the beat is near the target
def isNear(beat,target):
    return abs(beat.centerX - target.centerX) <10 and abs(beat.centerY - target.centerY) < 10

#every time you press a key, and the beat doesn't hit the target, your miss counter goes up by 1
#when the beat hits the target, your hit counter goes up by 1
def onKeyPress(keys):
    hit = False
    for beat in beats.children:
        if (isNear(beat,target1) and keys == 'a'):
            hit = True
        elif(isNear(beat,target2) and keys == 's'):
            hitCounter() 
            hit = True
        elif(isNear(beat,target3) and keys == 'k'):
            hitCounter()
            hit = True
        elif(isNear(beat,target4) == True and keys == 'l'):
            hitCounter()
            hit = True
    if not hit:
        missCounter()
    if hit == True:
        hitCounter()
#every time you release a key, and the beat doesn't hit the target, your miss counter goes up by 1
#when the beat hits the target, your hit counter goes up by 1
def onKeyRelease(keys):
    hit = False
    for beat in beats.children:
        if (isNear(beat,target1) and 'a' in keys):
            hit = True
        elif(isNear(beat,target2) and 's' in keys):
            hitCounter() 
            hit = True
        elif(isNear(beat,target3) and 'k' in keys):
            hitCounter()
            hit = True
        elif(isNear(beat,target4) == True and 'l' in keys):
            hitCounter()
            hit = True
    if not hit:
        missCounter()
    if hit == True:
        hitCounter()

#checks app key release to be a key release                
app.onKeyRelease = onKeyRelease
