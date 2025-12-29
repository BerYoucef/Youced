We have a problem which is ask to design a function that produce true if the SeatNum is on the aisle.
 we have a data definition :
- SeatNum is Interval[1, 32]
 so basically we created a new Data type based on an interval and its range is 1 to 32.  
- then we have the interpretation (interp.) 
	- "Seat Numbers in a row, 1 and 32 are aisle seats"
so from this point we know that the aisle seats are 1 and 32.
- Next we have constant : 
	- ```
	  (define SN1  1)
	  (define SN2 12)
	  (define SN3 32)
	  ```
to make it easier to the programmer to test or not needed to touch the function Body.
- For the Template , we just used the atomic non distinct template 
```
(define (fn-for-seat-num sn)    ;; fn-for-seat-name is a temporarly name.
							   ;; sn in the name of the input variable.
	(... sn))                   ;; Body of the function.
```

- newt we move to the Function Design to solve the Problem, and we'll use the HtDF (How to Design Function) recipe : 
- it have 5 steps :
	- Signature, Purpose, Stub.
	- Examples.
	- Template.
	- Code Body .
	- Testing and Debugging.

- Signature is a contract :
	- ```
	  ;; SeatNum => Boolean   ; Input => Output.
	  ```
the input is SeatNum [Interval] and it produce [True, False] "Boolean" .

- then we have the Purpose, or a small Definition for the function functionality .
	- "Produce True if the given SeatNum is aisle seat, otherwise False".
- then we define the Stub, and with this step we can define the following:
	- Function Name.
	- Input Variable Name.
	- a Dummy Result.
	- Commented.
and the Purpose of the stub is the see how the function looks like in the final result, 

- The next step is the examples, and here we try to cover all cases like : 
	- aisle
	- middle
	- out of range
	- strings ...etc
and this examples are inside a check-expect function to relate it with the last step "Testing and Debugging". 

- The Third step is the Template .
we simply get it from the Data Definition , But we also use the Stub here to grab the Name of the Function . 
- The Fourth Step, is the "Code Body"
and here we check Purpose again . the rule is simple (True if the SeatNum is aisle, otherwise false) . 
so here we'll use the **OR** Function with this pattern **<OR <expression 1> <expression 2>>**.
and the expression either 1 or 2 will produce **True** if the **sn** input variable equal to one of the aisle numbers "1 or 32 ", otherwise **False** . 
- in the last we check the **Check-expect** result and see it the examples have passed the test or no, and based on that we decide to debug the function or no.