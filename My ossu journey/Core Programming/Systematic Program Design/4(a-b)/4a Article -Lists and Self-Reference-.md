
---

4a points : 
- [x] explain list , its structure, how to use it in racket (cons)  
- [x] what is a self -reference ? well-formed ? 
- [x] when to use them ? (arbitary)
- [x] how to write examples ? 
- [x] natural recursion
- [x] how the template looks like? 
- [x] mention (base, contribution of first, combination).



#  Lists and Self-Reference 

## 1. The List Data Structure


- **Explanation of the List**
    - Lists fall under the category of **Compound Data**. They are simply a collection of elements linked together.
- **Structure of a List**
    - Its structure is based on "Cumulative Construction". It is not a single box where we put things; instead, it is a **chain**. Every cons adds **one** element to the front, and it must hold a **List** with its other hand (even if that list is just empty).
- **How to use it in Racket (cons)**
    - We can create lists in Racket using cons. The syntax looks like this:
    ```
    (cons <Element> <List>)
    (cons 1 empty)
    (cons 10 (cons 5 empty))
    ```

    - Here, we created two lists. The first one contains a single element, the number "1", linked with empty.
    - The same applies to the second list: we linked the 10 with the current existing list, which is (cons 5 empty).
    - **Important Notes:**
        1. The cons function requires two inputs (arguments): the first is called **First**, and the second is called **Rest** (which is the rest of the list). In the first example, **Rest** is empty, and in the second example, **Rest** is (cons 5 empty).
        2. The cons function always needs an element (String, Number, etc.) combined with the "rest of the list".
        3. cons stands for **Construct**. Notice that we always link the new element with an existing list. This places the new element at the **front** of the new list: (cons <**First**> <**List**>).
## 2. Self-Reference

- **What is Self-Reference?**
    
    - Self-Reference is a term we use specifically when **defining data**. It means that the data type refers to itself within its own definition.
        
    - **Example:**
        
        - When we define a list named List22 as an element combined with List22:
            
        
        codeText
        
        ```
        List22 is one of:
        - empty
        - (cons Number List22)
        ```
        
        - Notice that we used List22 to define (cons Number List22).
            
    - This self-reference in the data definition is what **forces** us later to make the program call itself (Recursion).
        
- **What is a "Well-Formed" Self-Reference?**
    
    - Simply put, it is a rule we follow to ensure the self-reference is valid. To be well-formed, the definition must have:
        
        1. **At least one Base Case:** This acts as a **stopping point** to avoid infinite loops. It does not contain a self-reference (typically empty).
            
        2. **At least one Self-Reference Case:** This is the part that contains the self-reference (like the cons example mentioned above).
## 3.  When to Use Self-Reference ?

- **What is arbitrary sized data?**
    
    - Simply put, it refers to an unknown amount of information (it could be 0, or it could be more).
        
    - **Example:** If we need to count all students in a school, we don't know the exact number at that moment (it is variable and not fixed). Therefore, we are dealing with unknown information that requires **flexible data**.
        
- **The Role of Self-Reference:**
    
    - This is where the benefit of **Self-Reference** lies. It allows us to build a chain of data as long as we need (e.g., matching the number of students).
        
    - Because the data definition refers to itself, we can write a program that repeats the operation for each student until it reaches the **Base Case** and stops.
        
- **Conclusion:**
    
    - Thus, an arbitrary amount of information requires **arbitrary-sized data**, and this specifically requires a **well-formed self-reference**.
## 4. Writing Examples

- **How to write data examples for lists:**
    
    - Writing examples is straightforward; we simply need to follow the conditions of the well-formed self-reference definition.
        
    - Let's assume we have a list of bird weights (ListOfNumber):
        
        - **Base Case:** empty.
            
        - **Self-Reference Case:** (cons Number ListOfNumber).
            
- **Pro Tip:**
    
    - Always start by writing the example for the **Base Case** first. From personal experience, jumping directly to complex lists makes things harder. Once you have the base case (the empty list), you can easily build larger lists on top of it.
        

```
;; Data Definition:
;; ListOfNumber is one of:
;;  - empty                        ;; Base Case
;;  - (cons Number ListOfNumber)   ;; Self-Reference Case

;; Examples:
(define LON1 empty)                    ;; Example 1: The Base Case
(define LON2 (cons 5 empty))           ;; Example 2: Self-Reference
(define LON3 (cons 10 (cons 5 empty))) ;; Example 3: Self-Reference

;; Notice that in LON3, the part (cons 5 empty) is actually LON2.
;; This confirms that the list is built upon itself.
```
## 5. The Template
- **How the template looks like:**
    

```
(define (fn-for-lon lon)
  (cond [(empty? lon) (...)]
        [else (... (first lon)
                   (fn-for-lon (rest lon)))]))
```

- **(first lon):** Represents the first element in the list.
    
- **(fn-for-lon (rest lon)):** Here, we simply call the same function on the rest of the elements (without the first one). This is exactly what **Natural Recursion** is.
    
- **The Base Case:**
    
    - It is the answer in the first cond expression (what happens when the list is empty).
        
- **Contribution of the First:**
    
    - (first lon) is the first item in the current list. It contributes its value based on the program's goal (we can use it, calculate with it, delete it, or replace it).
        
- **Combination (Recursive Step):**
    
    - Represented by the first three dots (...) in the else clause. It simply shows us **how to combine** the result of the first element with the result of the recursion (e.g., using +, and, cons, or an if statement).
        


## 6. Natural Recursion

- Explanation of Natural Recursion
	- It is essentially the **functional realization** of the Self-Reference found in the Data Definition.
	- Since the data definition says "a List contains a List", the function naturally says "I will call myself on the rest of the List". This ensures the function processes the entire data chain until it hits the Base Case.