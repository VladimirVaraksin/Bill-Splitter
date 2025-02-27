# Bill Splitter  

This Python script helps split a bill among a group of friends fairly. It also includes an optional "Who is lucky?" feature that allows one person to be exempted from paying.  

## How It Works  

1. The user inputs the number of friends joining (including themselves).  
2. If no one is joining, the program exits.  
3. Each friend's name is entered and stored in a dictionary with an initial bill amount of 0.  
4. The total bill amount is entered, and the bill is equally split among all friends.  
5. The user is asked whether they want to use the "Who is lucky?" feature:  
   - If **Yes**, a random person is chosen, and their share becomes 0 while the bill is redistributed among the remaining friends.  
   - If **No**, the bill remains evenly split.  
6. The final bill distribution is printed.  

## Example Run  

```
Enter the number of friends joining (including you): 3  
Enter the name of every friend (including you), each on a new line:  
Alice  
Bob  
Charlie  
Enter the total bill value: 150  
Do you want to use the "Who is lucky?" feature? Write Yes/No: Yes  
Bob is the lucky one!  
{'Alice': 75.0, 'Bob': 0, 'Charlie': 75.0}  
```

## Requirements  
- Python 3.x  
- No external dependencies (uses built-in `random` module)  

This script is useful for evenly splitting expenses among friends while adding a bit of fun! 🎉
