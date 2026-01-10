
---
###### What is the Reference Rule ? 
It is the rule that governs the relationship between two distinct types of **non-primitive data**, such as data based on **structs** and **lists**.

This rule appears when a **compound data type** contains (or relies on) another compound data type inside it. This requires us to understand the difference between two types of data:
- **Primitive Data:** These are simple (atomic) data, such as Strings and Numbers. This data does not require a special definition because the language understands it directly.
- **Non-Primitive Data:** These are compound or complex data, such as lists or struct-based data, which we usually define ourselves following the **HtDD** (How to Design Data) recipe.

This rule applies when we define a list (e.g., a ListOfSchools) where a single element within this list is a struct (e.g., School) that has **its own separate data definition**.

Here, the **"Reference Rule"** is established, as the list of schools **refers** to the definition of the school.
###### Template : 
```
;; Data definition : 
(define-struct school (name tuition))
;; school is (make-school String Number)
;; interp. name is the school's name, tuition is international studen's tuition
(define S1 (make-school "School1" 5555))
(define S2 (make-school "School2" 6666))
(define (fn-for-school s )
	(... (school-name s)
		 (school-tuition s)))
;; Template rules used : 
;; - compound : (make-school String Number)


;; ListOfSchool is one of : 
;; - empty                       ;base case
;; - (cons School ListOfSchool)  ;self-reference case
;; interp. a list of schools
(define LOS1 empty)
(define LOS2 (cons S1 (cons S2 empty)))

(define (fn-for-los los)
	(cond [(empty? los) (...)]
		  [else (... (fn-for-school (first los))  ;natural helper here
					  (fn-for-los (rest los)))])) ;natural recursion here

;; Template rules used:
;; - one of : 2 cases
;; - atomic Distinct: empty
;; - compound: (cons School ListOfSchool) 
;; - reference: (first los) 
;; - self-reference: (rest los) is ListOfSchool
```

- We have a natural **Self-Reference** in ListOfSchools, denoted as **SR**.
    
- We have a **Reference** in the ListOfSchools data definition, where School refers to its own separate data definition, denoted as **R**.
    
- We have **Natural Recursion** in the ListOfSchools function template, denoted as **NR**.
    
- We have a **Natural Helper**, which is the function (fn-for-school). It takes (first los) as an argument (or parameter), which is essentially a School that has its own specific data.
    
- What is a **Natural Helper**?
    
    - It is a function that appears naturally in the template because the data definition enforces it (due to nested complex data). Its purpose is to consume and process the subtype **School**.
        
    - When do we use it?
        
        - Here lies the importance of writing **detailed examples**. They explain exactly what we want before we start writing the function, and they tell us precisely whether we need a helper function (Natural Helper) or not. The **indicator** is the moment we realize the example is becoming complex and overloaded with functionality. At this point, we immediately use the **Wish List** strategy: we change the name of the (Natural Helper) to the name of a function we wish existed (e.g., calc-tuition), and then we implement it separately later.
            
        - In both cases, the School element **must be processed**. The difference is **where** we process it: either in a separate function (via the **Wish List**) or by processing it directly inside the main function (**Inline**).
            
    - What are its advantages?
        
        - First, it allows us to separate functions and distribute workloads and responsibilities across multiple functions, so that each function focuses on a specific task (**Separation of Concerns**).
            
        - Second, it facilitates maintenance. If we encounter a problem, we know exactly where it is without affecting other functions (**Maintainability**). For example, modifying the School struct will not break the ListOfSchools function.
###### To sum up:

- The flow is as follows (**from data definition to implementation decision**) :
    
    - Nested complex data
        
    - Results in a separate data definition for each element
        
    - And this results in using the reference rule
        
    - And here we split into two points:
        
        - Option one (wish list): Either use a natural helper if the examples are complex.
            
        - Option two (inline): If we see that the natural helper function will help us with something very trivial like an addition operation or similar, then it is better to skip it and perform the task directly inside the main function.