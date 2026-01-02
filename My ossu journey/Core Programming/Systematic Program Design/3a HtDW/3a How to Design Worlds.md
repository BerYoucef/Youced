
---

This module shows us a new recipe which is (HtDW = How to Design Worlds) and worlds here means Programs.
The recipe is quite simple, it has only 2 parts , the first part is **Domain Analysis** and the second one is **Build the actual program** .
#### 1) Domain Analysis : 
This part is the most important one in the whole process. and we simply design the functionalities of the program with a pen and paper without any code. 
It has 4 steps like the following: 
- Sketch Program scenarios.
- Identify constant information. 
- Identify changing information.
- Identify Big-bang Options. 

1) Sketch Program scenarios:
	- In this step we just draw some pictures of the program in a different states, like the initial state, middle state, end state. 
	- and we should focus on what we drawing, because from this step we can go through other steps, without it we cannot identify constants nor changing information. 
2) Identify constant information: 
	- in this step we simply declare the constant values. like the image width and height, and everything is constant. 
3) Identify changing information : 
	- Just like the step before (1.2), we declare changing information, like for example the speed, coordinates.
    - Both the information either constants or changing are based on the program and the quality of our sketch from the step 1.1 . 
4) Identify Big-bang Options: 
	- Here we declare Big-bang Options like `to-draw` `on-tick`  `on-key` , each one do something, and the big-bang just squeeze all of this pieces together in one runtime program that is based on events, because each piece is an event, like `on-key` will work only when we press something on the keyboard.
From that we finish the first part. 
#### 2) Build the Program :
At this Part, we are ready to build our program, we just convert the **Domain Analysis** to a code.
We have **3** main steps here.
1) Constants :
	- We simply convert our constant list from 1.2 to code like (define C 2). 
2) Data definition using **HtDD** :
	- we simply use the changing information from the domain analysis with HtDD recipe. nothing more, nothing less. 
3) Functions using **HtDF** :
	- At this step we have 2 sub-steps :
		1) main first :
			- define the main function, that we will use to run the program. 
		2) wish list entries for big-bang handlers: 
			- here we define the functions that we need in the main inside the big-bang function. 
			- they are not a full functions but just the name of the function we need, then we add it to the wish-list to finish it later when we have the full wish list.
4) Then we work on the wish lists until we finish them all.

Example:
```
Problem: 
Animate a cat moving from left to right.
```

We start with Domain Analysis : 
##### Domain Analysis : 
- we draw 3 images of the states of this cat on different time : 
	- Image 1 : the cat is in the left edge of the screen    (x = 0      , y = (height / 2))
	- Image 2 : the cat is in the middle of the screen       (x = 300 , y = (height / 2))
	- Image 3 : the cat is in the right edge of the screen (x = 600 , y = (height / 2))
- Identify Constant information : 
	- from the images we can get some constants like :
		- Image width
		- Image height 
		- Y coordinate
		- Cat Image it self 
		- background (empty-scene).
	- All of this constants can be change when the program get bigger and better, so this list isn't fixed. 
- Identify changing information : 
	- here ask yourself a question : what the thing is changing over time ? simply is x coordinates. 
- Identify Big-bang Options: 
	- because the cat is just moving from left to right over time . we need : 
		- `on-tick` : which is an option that change the state of the program each second. like on the first second x = 0 , on the second 10 x = 50 for example . 
		- `to-draw` : this option is to draw the cat image on the screen (render it ). 
##### Build the Program: 
Here I'm using Racket : 
- Constants : from the Domain Analysis

```
;; =================
;; Program Name:
;; Animated Cat
;; =================
;; Constants:
(define WIDTH 400 )
(define HEIGHT 300)
(define CTR-Y (/ HEIGHT 2))
(define CAT-IMG (square 20 "solid" "purple"))
(define MTS (empty-scene WIDTH HEIGHT))
```
For CAT-IMG Constant I used a square not a really cat img. 

- HtDD : 
```
;; =================
;; Data definitions:

;; Cat-x is Number 
;; interp. Cat-x is the x coordinate of the current position of the cat 
(define c1 0)
(define c2 (/ WIDTH 2))
(define c3 WIDTH)
#;
(define (fn-for-cat-x c)
  (... c))
;; Template rules used:
;; - atomic Non-Distinct: Number
```
we just used the HtDD recipe on the changing information (x coordinates) 

- Functions with HtFD :
	- main definition and wish list entries for big-bang handlers :
		- as we can see the cat-new-x and render are both function (on the wish list) "just the name of them"
```
(define (main Cat-x)
  (big-bang Cat-x                     ; Cat-x
            (on-tick   cat-new-x)     ; Cat-x -> Cat-x
            (to-draw   render)))      ; Cat-x -> Image           
```

- Work through wish list until done : 
```
;; Cat-x -> Cat-x
;; produce the next cat x coordinate by adding SPEED pixels to right 
(check-expect (cat-new-x 5) (+ 5 SPEED))
;; (define (cat-new-x 5) 6) ; stub
;; <template used from Cat-x>
(define (cat-new-x Cat-x)
  (+ Cat-x SPEED))

;; Cat-x -> Image
;; render the CAT-IMG into MTS with the given coordinate of Cat-x 
(check-expect (render 5) (place-image CAT-IMG 5 CTR-Y MTS)) 
;; (define (render Cat-x) MTS)
;; <template used from Cat-x>
(define (render Cat-x)
  (place-image CAT-IMG Cat-x CTR-Y MTS))
```
as we  can see here we finished the functions one by one until we finish them all , 
also if you look more closely you will see the SPEED Constant, we add it on a newer version of the Program, so the new Constants List is : 
- Image width
- Image height 
- Y coordinate
- Cat Image it self 
- background (empty-scene).
- SPEED
So the Constants are not fixed.  

---

“In conclusion, the **HtDW recipe** is not merely a way to write code , but a method for organizing your thinking. By separating **Domain Analysis**  from the actual programming , we ensure that we understand _what_ we want to do  before getting busy with _how_ to write it . This methodology is what transforms building complex programs from a random process into organized, reliable steps .”

---

**I didn't explain much about the program itself, but I focused more the recipe itself. **
