from .models import Box


# Get all possible orientations of a product
def getOrientations(length, width, height):

    orientations = [
        (length, width, height),
        (length, height, width),
        (width, length, height),
        (width, height, length),
        (height, length, width),
        (height, width, length)
    ]

    return orientations


# Check whether product can fit inside available space
def canPlace(productSize, spaceSize):

    productLength = productSize[0]
    productWidth = productSize[1]
    productHeight = productSize[2]

    spaceLength = spaceSize[0]
    spaceWidth = spaceSize[1]
    spaceHeight = spaceSize[2]

    if (
        productLength <= spaceLength
        and productWidth <= spaceWidth
        and productHeight <= spaceHeight
    ):
        return True

    return False


# Calculate remaining spaces after placing product
def splitSpace(space, product):

    spaceLength = space[0]
    spaceWidth = space[1]
    spaceHeight = space[2]

    productLength = product[0]
    productWidth = product[1]
    productHeight = product[2]

    remainingSpaces = []

    # Right side
    if spaceLength - productLength > 0:

        remainingSpaces.append(
            (
                spaceLength - productLength,
                spaceWidth,
                spaceHeight
            )
        )

    # Front side
    if spaceWidth - productWidth > 0:

        remainingSpaces.append(
            (
                productLength,
                spaceWidth - productWidth,
                spaceHeight
            )
        )

    # Top side
    if spaceHeight - productHeight > 0:

        remainingSpaces.append(
            (
                productLength,
                productWidth,
                spaceHeight - productHeight
            )
        )

    return remainingSpaces


# Check whether all products can fit inside one box
def productFitsInBox(products, box):

    availableSpaces = [
        (
            box.internal_length,
            box.internal_width,
            box.internal_height
        )
    ]

    for product in products:

        productPlaced = False

        orientations = getOrientations(
            product.length,
            product.width,
            product.height
        )

        for spaceIndex in range(len(availableSpaces)):

            space = availableSpaces[spaceIndex]

            for orientation in orientations:

                if canPlace(orientation, space):

                    availableSpaces.pop(spaceIndex)

                    newSpaces = splitSpace(
                        space,
                        orientation
                    )

                    availableSpaces.extend(newSpaces)

                    productPlaced = True

                    break

            if productPlaced:
                break

        if not productPlaced:
            return False

    return True


# Find the most suitable box
def findPerfactBox(order):

    productVolume = 0
    totalWeight = 0

    products = []
    boxes = []

    orderItems = order.items.select_related("product").all()

    if not orderItems.exists():

        return {
            "error": "Order does not contain any products"
        }

    for items in orderItems:

        product = items.product

        if items.quantity <= 0:

            return {
                "error": "Product quantity must be greater than 0"
            }

        totalWeight = (
            totalWeight
            + product.weight * items.quantity
        )

        productVolume = (
            productVolume
            + (
                product.length
                * product.width
                * product.height
            ) * items.quantity
        )

        for i in range(items.quantity):

            products.append(product)

    availableBoxes = Box.objects.filter(
        max_weight__gte=totalWeight
    )

    for box in availableBoxes:

        boxVolume = (
            box.internal_length
            * box.internal_width
            * box.internal_height
        )

        if boxVolume < productVolume:
            continue

        if productFitsInBox(products, box):

            boxes.append({
                "id": box.id,
                "volume": boxVolume,
                "weight": box.max_weight,
                "cost": box.cost
            })

    if not boxes:

        return {
            "error": "You don't have any suitable box"
        }

    # First select lowest cost box
    # If cost is same, select smaller box

    perfectBox = min(
        boxes,
        key=lambda box: (
            box["cost"],
            box["volume"]
        )
    )

    return {
        "box_id": perfectBox["id"],
        "box_volume": perfectBox["volume"],
        "box_max_weight": perfectBox["weight"],
        "box_cost": perfectBox["cost"],
        "product_volume": productVolume,
        "product_weight": totalWeight,
    }