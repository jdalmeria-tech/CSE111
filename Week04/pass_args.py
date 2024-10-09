"""
Demonstrate that numbers are passed to a function by value
and lists are passed to a function by reference.
"""

def main():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"    Before calling modify_args(): x {x}  lx {lx}")

    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)

    print(f"    After calling modify_args():  x {x}  lx {lx}")


def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("    modify_args(n, alist)")
    print(f"        Before changing n and alist: n {n}  alist {alist}")

    # Change the values of both parameters.
    n += 1
    alist.append(4)

    print(f"        After changing n and alist:  n {n}  alist {alist}")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()

# REMEMBER:
"""Pass by Value:

This is like making a photocopy of a page from your magical notebook and giving it to a friend.
Your friend can read and even change the photocopy, but your original notebook page stays the same.

Pass by Reference:

Now imagine you give your friend a magical key to your toy box. Your friend can open the toy box and play with the toys,
add new toys, or remove some. Whatever they do with the toys affects your toy box because they’re not dealing with a copy—they’re dealing with your actual toy box.

In programming:

Pass by Value is like giving a photocopy (a separate copy of the original value).

Pass by Reference is like giving the magical key (a way to access and modify the original)."""