# Test Cases

These are the test cases I plan to use for the box selection system.

## Test Case 1 - Suitable Box

### Input

Create a product which can fit inside a box and create an order with that product.

### Expected Result

The API should return a suitable box.

---

## Test Case 2 - Multiple Quantity

### Input

Create an order with one product and quantity greater than 1.

### Expected Result

The total weight and volume should include the quantity.

---

## Test Case 3 - Product Too Heavy

### Input

Create a product whose weight is more than the maximum weight of the available boxes.

### Expected Result

The system should say that there is no suitable box.

---

## Test Case 4 - Product Does Not Fit

### Input

Create a product where one or more dimensions are bigger than the box dimensions.

### Expected Result

The box should not be selected even if the total volume looks large enough.

---

## Test Case 5 - Product Rotation

### Input

Create a product which does not fit in its original orientation but fits after rotation.

### Expected Result

The system should be able to find the suitable orientation.

---

## Test Case 6 - Empty Order

### Input

Create an order without any items.

### Expected Result

The API should return a validation error.

---

## Test Case 7 - Order Does Not Exist

### Input

Request box recommendation for an order ID which does not exist.

### Expected Result

The API should return HTTP 404.

---

## Test Case 8 - Multiple Suitable Boxes

### Input

Create more than one box which can hold the order.

### Expected Result

The system should select the box according to the selection rule implemented in the service.
