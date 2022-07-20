* The solution ijs pretty simple, but the **trick** here is
* Th main point of solution is to **create a hash map**  where the **key** is a **dictionary** itself.
* But in python **we counldn't hash dictionaries**.
* In python, **hashable data types** are the **immutable data types** such as **tuple**, and **not list**.
* For this reason, instead of hashing the dictionary itself, we are going to hash the **sorted strring**.