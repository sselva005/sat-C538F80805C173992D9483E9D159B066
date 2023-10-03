Certainly! Here's a Python function called `linear_search_product` that performs a linear search to find a target product in a list of products and returns a list of indices of all occurrences of that product, or an empty list if the product is not found:

```python
def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices
```

You can use this function by passing your list of products and the target product name as arguments. It will return a list of indices where the target product is found in the input list or an empty list if it's not found.