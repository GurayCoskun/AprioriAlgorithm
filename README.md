Problem is about which products stand side by side on the market shelves. I reached the solution with the APriori algorithm.
 By looking at the data of the products sold, we look at which products are sold together the most. The program lists the best selling products in combinations with us. I used a data structure with the "csv" extension. I wrote the "candidate" function, I separated the elements of the data.I created the first candidate list with the function "candidate_others" and compared the real combinations with "support_count" and prepared the list. Finally, I have listed combinations of 3 and more elements with the "candidate more 3" function. I ran the program with two different data and there was no bug.But I realized,if suppor count is low,integrity decreases. The program separates the elements of the data and subtracts the binary combinations.Then, it finds combination’s rates in transactions.And,it compares to “support_count” and lists the larger ones.Later, it performs these operations as triple, quadruple, etc.Some examples of outputs :
This algoritm works with 0.3 support count.

F1 : ['BREAD', 'BISCUIT', 'TEA', 'COFFEE']

F2 :  [{'BREAD', 'BISCUIT'}, {'BREAD', 'TEA'}, {'BISCUIT', 'TEA'}]

and more :  [{'BREAD', 'BISCUIT', 'TEA'}]

and more :  [ ]
