function addToCart(product_id, quantity, color) {
    // console.log(product_id)
    $.ajax({
        type: 'POST',
        url: "{% url 'add_to_cart' %}",
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin',
        data: {
            "product_id": product_id,
            "quantity": quantity,
            "category": category
        },
        success: function(response) {
            success = processResponse(response)
            if (success == true) {
                if ($(".abscence-text").length) {
                    $(".abscence-text").remove()
                    console.log($(".save-cart"))
                    $(".save-cart").removeClass("remove")
                }
                if ($(`.item${product_id}`).length) {
                    console.log("This is processed")
                    quantity_field = $(`.number-cart${product_id}`)
                    current_value = quantity_field.val()
                    newValue = parseInt(current_value) + quantity
                    quantity_field.val(newValue)
                    console.log(quantity_field)
                } else {
                    prefix = "pro" + product_id
                    imgUrl = $(`.${prefix}-image`).attr("src")
                    prevPrice = $(`.${prefix}-prevPrice`).text()
                    price = $(`.${prefix}-price`).text()
                    name = $(`.${prefix}-name`).text()
                    // console.log(imgUrl, prevPrice, price, name)
                    $(`<div class='mb-4 d-flex item${product_id}'><a onclick='removeFromCart(${product_id})' class='cursor-pointer d-flex align-items-center mr-2 text-muted'><i class='fal fa-times'></i></a><div class='media w-100'><div class='w-60px mr-3'><img src='${imgUrl}' alt='${name}'></div><div class='media-body d-flex'><div class='cart-price pr-6'><p class='fs-16 font-weight-bold text-secondary mb-1'><span class='font-weight-500 fs-13 text-line-through text-body mr-1'>${prevPrice}</span>${price}</p><a href='#' class='text-secondary'>${name}</a></div><div class='position-relative ml-auto'><div class='input-group'><a href='#' class='down position-absolute pos-fixed-left-center pl-2'><i class='far fa-minus'></i></a><input type='number' class='number-cart${product_id} w-90px px-6 text-center h-40px bg-input border-0' value='${quantity}'><a href='#' class='up position-absolute pos-fixed-right-center pr-2'><i class='far fa-plus'></i></a></div></div></div></div></div>`).insertBefore($(".save-cart"))
                }
            }
        },
        error: function(response) {
            processResponse(response)
        }
    })
}

const notyf = new Notyf({
    duration: 10000,
    position: {
        x: 'center',
        y: 'top',
    },
    // dismissible: true,
    types: [
        {
           type: 'warning',
            background: '#cea605',
            icon: "<span class='material-symbols-outlined' style='color:white;vertical-align:middle'>warning</span>",
            duration: 3000,
            dismissible: true
        },
        {
            type: 'info',
            background: '#2d2dbf',
            icon: "<span class='material-symbols-outlined' style='color:white;vertical-align:middle'>info</span>",
            duration: 3000,
            dismissible: true
        },
        {
            type: 'error',
            background: 'indianred',
            duration: 2000,
            dismissible: true
        },
        {
            type: 'success',
            duration: 2000,
            dismissible: true
        }
    ]
});