# What I Learned

This assignment helped me understand Django and Django REST Framework better.

Before starting this assignment, I knew the basic Django and DRF concepts, but I had not worked much on a problem where the main logic is not only CRUD.

## 1. Django Models

I learned how to create models for different things in a project.

In this project I created models for:

- Product
- Box
- Order
- OrderItem

I also understood how ForeignKey relationships work.

## 2. Order and OrderItem

I learned why an order and its products are better stored using an OrderItem model.

For example, one order can have:

```text
Product A - quantity 2
Product B - quantity 3
```

So the OrderItem model stores the product and its quantity.

## 3. Product Dimensions

I learned that checking only volume is not enough.

A product also needs to physically fit inside the box.

This made me think about length, width and height separately.

## 4. Product Rotation

I learned that a product can sometimes fit if it is rotated.

For example:

```text
Length × Width × Height
```

can be checked in different orientations.

This was one of the main logic parts of this assignment.

## 5. Validation

I learned that API input should be checked before saving it into the database.

For example:

- Quantity should be greater than zero.
- Product dimensions should be positive.
- Box dimensions should be positive.
- An order should contain products.

## 6. Testing

I learned that writing one test is not enough.

Different situations should be tested, such as:

- A box is available
- A box is too small
- Weight is too high
- Multiple quantities are used
- A product does not physically fit

## 7. Debugging

I also learned that code can look correct but still have logical problems.

For example, checking total volume alone looked reasonable at first, but it does not prove that the products can physically fit inside the box.

## Final Learning

The main thing I learned from this assignment is that solving a programming problem is not only about writing code.

I also need to think about:

```text
Input
    ↓
Validation
    ↓
Business Logic
    ↓
Edge Cases
    ↓
Testing
```

**I will add or change this section with my own words before submitting the assignment so that it accurately describes what I personally learned.**
